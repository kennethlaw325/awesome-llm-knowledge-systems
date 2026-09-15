#!/usr/bin/env python3
"""Stage the repo's documentation into build/docs/ for `mkdocs build`.

mkdocs refuses a docs_dir that contains mkdocs.yml, so the site is built from a
copy.  Source files are never modified -- every rewrite below applies only to
the staged copy.  stdlib only; runs the same on Windows and Ubuntu.
"""

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "build" / "docs"

REPO = "https://github.com/kennethlaw325/awesome-llm-knowledge-systems"
BLOB = REPO + "/blob/master/"

# single files: source (relative to ROOT) -> destination (relative to DOCS)
FILES = {
    "README.md": "index.md",
    "glossary.md": "glossary.md",
    "CHANGELOG.md": "CHANGELOG.md",
    "CONTRIBUTING.md": "CONTRIBUTING.md",
    "LICENSE": "LICENSE",
    "docs-site/extra.css": "stylesheets/extra.css",
}

# whole trees, copied file for file
TREES = {
    "chapters": "chapters",
    "diagrams": "diagrams",
    "translations": "translations",
}

MD_LINK = re.compile(r"\]\((?!https?:|/{2})([^)\s#]+\.md)\)")


def rewrite(text, is_index):
    """Apply the staging-only rewrites to one markdown file."""
    # README.md is staged as index.md, so links pointing at it must follow.
    text = re.sub(r"\]\((\.\./)*README\.md\)", r"](\1index.md)", text)
    if is_index:
        # Python-Markdown leaves markdown inside a raw HTML block unparsed
        # unless the tag opts in via md_in_html.
        text = text.replace("<details>", '<details markdown="1">')
        # GitHub reads `../../x` in a repo-root file as the repo's own URL;
        # on the site that would resolve against the Pages domain instead.
        text = re.sub(r"\]\(\.\./\.\./", "](" + REPO + "/", text)
    return text


def repoint_unstaged(path):
    """Send links whose target was never staged to GitHub instead.

    The Spanish translation ships 2 of its 14 chapters but its chapter footers
    still link to the siblings, and the source files are not ours to edit.
    Returns the list of rewritten targets so the caller can report them.
    """
    moved = []

    def swap(match):
        target = match.group(1)
        base = DOCS if target.startswith("/") else path.parent
        full = Path(str(base) + "/" + target.lstrip("/")).resolve()
        try:
            rel = full.relative_to(DOCS)
        except ValueError:
            return match.group(0)  # escapes the site; leave it for mkdocs
        if full.exists():
            return match.group(0)
        moved.append(target)
        return "](" + BLOB + rel.as_posix() + ")"

    text = path.read_text(encoding="utf-8")
    new = MD_LINK.sub(swap, text)
    if moved:
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(new)
    return moved


def copy_one(src, dst, is_index=False):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.suffix == ".md":
        with open(dst, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(rewrite(src.read_text(encoding="utf-8"), is_index))
    else:
        shutil.copy2(src, dst)


def self_check():
    assert rewrite("[a](../README.md) [b](README.md)\n", False) == (
        "[a](../index.md) [b](index.md)\n"
    )
    assert rewrite("<details>\n", True) == '<details markdown="1">\n'
    assert rewrite("<details>\n", False) == "<details>\n"
    assert rewrite("[p](../../pulls)\n", True) == "[p](" + REPO + "/pulls)\n"
    assert rewrite("[d](../../diagrams/x.png)\n", False) == "[d](../../diagrams/x.png)\n"
    assert MD_LINK.findall("](a.md) [x](https://e.com/b.md) [y](c.md#h)") == ["a.md"]
    print("self-check ok")


def main():
    if "--self-check" in sys.argv:
        self_check()
        return 0

    missing = [s for s in list(FILES) + list(TREES) if not (ROOT / s).exists()]
    if missing:
        print("missing source(s): " + ", ".join(missing), file=sys.stderr)
        return 1

    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)

    count = 0
    for src, dst in FILES.items():
        copy_one(ROOT / src, DOCS / dst, is_index=(dst == "index.md"))
        count += 1
    for src, dst in TREES.items():
        base = ROOT / src
        for path in sorted(base.rglob("*")):
            if path.is_file():
                copy_one(path, DOCS / dst / path.relative_to(base))
                count += 1

    repointed = 0
    for path in sorted(DOCS.rglob("*.md")):
        for target in repoint_unstaged(path):
            print("  -> GitHub: {} in {}".format(target, path.relative_to(DOCS)))
            repointed += 1

    print("staged {} files into {} ({} link(s) repointed)".format(count, DOCS, repointed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
