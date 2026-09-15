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

# [text](target.md) -- group 1 is the link text, group 2 the target.  The
# lookbehind keeps ![image](...) out of it.
MD_LINK = re.compile(r"(?<!!)\[([^\]\[]*)\]\((?!https?:|/{2})([^)\s#]+\.md)\)")


def rewrite(text, is_index):
    """Apply the staging-only rewrites to one markdown file.

    Returns (text, notes); `notes` names every rewrite that fired, so the build
    log states the full delta between a source file and its staged copy instead
    of leaving a reader to diff for it.
    """
    notes = []
    # README.md is staged as index.md, so links pointing at it must follow.
    # This one is repo-wide: glossary.md and the translated READMEs link back
    # to README.md too, not just index.md itself.
    # `((?:\.\./)*)` captures the whole prefix.  A repeated capturing group
    # keeps only its last repetition, which silently ate a level: the old
    # `(\.\./)*` turned ../../README.md into ../index.md.
    text, n = re.subn(r"\]\(((?:\.\./)*)README\.md\)", r"](\1index.md)", text)
    if n:
        notes.append("{} link(s) README.md -> index.md".format(n))
    if is_index:
        # Python-Markdown leaves markdown inside a raw HTML block unparsed
        # unless the tag opts in via md_in_html.
        text, n = re.subn("<details>", '<details markdown="1">', text)
        if n:
            notes.append('{} <details> -> <details markdown="1">'.format(n))
        # GitHub reads `../../x` in a repo-root file as the repo's own URL;
        # on the site that would resolve against the Pages domain instead.
        text, n = re.subn(r"\]\(\.\./\.\./", "](" + REPO + "/", text)
        if n:
            notes.append("{} link(s) ../../ -> {}/".format(n, REPO))
    return text, notes


def source_path(rel):
    """The repo file behind a staged path.

    Every staged path keeps its repo-relative name except README.md, which is
    staged as index.md.
    """
    return Path("README.md") if rel.as_posix() == "index.md" else rel


def source_exists(rel):
    """Does a staged path have a source file behind it in the repo?"""
    return (ROOT / source_path(rel)).exists()


def repoint_unstaged(path):
    """Fix links whose target was never staged.

    The Spanish translation ships 2 of its 14 chapters but its chapter footers
    still link to the siblings.  A target that exists in the repo but not in
    the staging dir goes to GitHub; one that is missing from the repo as well
    would only mint a GitHub 404, so the link is dropped to plain text.  The
    source files are not ours to edit either way.  Returns (target, action)
    pairs so the caller can report them.
    """
    moved = []

    def swap(match):
        target = match.group(2)
        base = DOCS if target.startswith("/") else path.parent
        full = Path(str(base) + "/" + target.lstrip("/")).resolve()
        try:
            rel = full.relative_to(DOCS)
        except ValueError:
            return match.group(0)  # escapes the site; leave it for mkdocs
        if full.exists():
            return match.group(0)
        if not source_exists(rel):
            moved.append((target, "plain text (absent from the repo too)"))
            return match.group(1)
        moved.append((target, "GitHub"))
        return "[" + match.group(1) + "](" + BLOB + rel.as_posix() + ")"

    text = path.read_text(encoding="utf-8")
    new = MD_LINK.sub(swap, text)
    if moved:
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(new)
    return moved


def copy_one(src, dst, is_index=False):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.suffix != ".md":
        shutil.copy2(src, dst)
        return []
    text, notes = rewrite(src.read_text(encoding="utf-8"), is_index)
    with open(dst, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return notes


def self_check():
    assert rewrite("[a](../README.md) [b](README.md)\n", False) == (
        "[a](../index.md) [b](index.md)\n",
        ["2 link(s) README.md -> index.md"],
    )
    # every ../ survives; a repeated capturing group would keep only the last
    assert rewrite("[a](../../../README.md)\n", False)[0] == "[a](../../../index.md)\n"
    assert rewrite("<details>\n", True)[0] == '<details markdown="1">\n'
    assert rewrite("<details>\n", False) == ("<details>\n", [])
    assert rewrite("[p](../../pulls)\n", True)[0] == "[p](" + REPO + "/pulls)\n"
    assert rewrite("[d](../../diagrams/x.png)\n", False)[0] == "[d](../../diagrams/x.png)\n"
    assert [m[1] for m in MD_LINK.findall("[a](a.md) [x](https://e.com/b.md) [y](c.md#h)")] == [
        "a.md"
    ]
    assert MD_LINK.findall("![fig](a.md)") == []
    # a dead link degrades to its own text, nothing else on the line moves
    assert MD_LINK.sub(lambda m: m.group(1), "*next: [Ch 2 -- x](02.md)*") == "*next: Ch 2 -- x*"
    assert source_exists(Path("index.md")) and not source_exists(Path("chapters/99-no.md"))
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
    rewrites = 0

    def stage(src, dst, is_index=False):
        nonlocal count, rewrites
        for note in copy_one(src, dst, is_index):
            print("  rewrote in {}: {}".format(dst.relative_to(DOCS), note))
            rewrites += 1
        count += 1

    for src, dst in FILES.items():
        stage(ROOT / src, DOCS / dst, is_index=(dst == "index.md"))
    for src, dst in TREES.items():
        base = ROOT / src
        for path in sorted(base.rglob("*")):
            if path.is_file():
                stage(path, DOCS / dst / path.relative_to(base))

    repointed = 0
    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(DOCS)
        for target, action in repoint_unstaged(path):
            print("  -> {}: {} in {}".format(action, target, rel))
            # Also as a GitHub Actions annotation, so a repoint shows up in the
            # PR's checks UI instead of only in the log.  Harmless locally.
            print(
                "::warning file={}::staged link to {} repointed: {}".format(
                    source_path(rel).as_posix(), target, action
                )
            )
            repointed += 1

    print(
        "staged {} files into {} ({} staging rewrite(s), {} unstaged link(s) fixed)".format(
            count, DOCS, rewrites, repointed
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
