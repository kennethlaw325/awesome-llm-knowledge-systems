#!/usr/bin/env python3
"""Stage the repo's documentation into build/docs/ for `mkdocs build`.

mkdocs refuses a docs_dir that contains mkdocs.yml, so the site is built from a
copy.  Source files are never modified -- every rewrite below applies only to
the staged copy.  stdlib only; runs the same on Windows and Ubuntu.
"""

import os
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


def classify(rel, from_dir):
    """Decide what a link target that is not in the staging dir becomes.

    `rel` is the target as a staging-root-relative path, `from_dir` the
    staging-root-relative directory of the file holding the link.  Returns
    (action, href, is_error); `href` is None when the link is left untouched.

    Three cases, in order: the target is in the repo but out of the allowlist
    (GitHub blob URL); it is an untranslated chapter, i.e. a language ships
    fewer chapters than its footers link to, so the English original is the
    honest target; or it resolves to nothing anywhere, which is a typo and
    fails the build rather than quietly losing a hyperlink.
    """
    if source_exists(rel):
        return "GitHub", BLOB + rel.as_posix(), False
    english = Path("chapters") / rel.name
    if (ROOT / english).exists():
        href = Path(os.path.relpath(english, from_dir)).as_posix()
        return "English chapter " + href, href, False
    return "no target in the repo", None, True


def repoint_unstaged(path):
    """Fix links whose target was never staged.

    The Spanish translation ships 2 of its 14 chapters but its chapter footers
    still link to the siblings.  `classify` decides each case; the source files
    are not ours to edit either way.  Returns (target, action, is_error)
    triples so the caller can report them and fail on the errors.
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
        action, href, is_error = classify(rel, path.parent.relative_to(DOCS))
        moved.append((target, action, is_error))
        if href is None:
            return match.group(0)
        return "[" + match.group(1) + "](" + href + ")"

    text = path.read_text(encoding="utf-8")
    new = MD_LINK.sub(swap, text)
    if new != text:
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
    assert source_exists(Path("index.md")) and not source_exists(Path("chapters/99-no.md"))
    # (a) in the repo, outside the staging allowlist -> GitHub blob URL
    assert classify(Path("CITATION.cff"), Path("chapters")) == (
        "GitHub",
        BLOB + "CITATION.cff",
        False,
    )
    # (b) a chapter that language has not translated -> the English original,
    # relative to the file that holds the link
    assert classify(
        Path("translations/chapters/es/02-knowledge-layer.md"),
        Path("translations/chapters/es"),
    ) == (
        "English chapter ../../../chapters/02-knowledge-layer.md",
        "../../../chapters/02-knowledge-layer.md",
        False,
    )
    # (c) a typo resolves to nothing anywhere -> flagged, and main() exits
    # non-zero on it; asserted here as a flag so the self-check itself survives
    assert classify(Path("chapters/07-mpc.md"), Path("chapters")) == (
        "no target in the repo",
        None,
        True,
    )
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
    dead = 0
    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(DOCS)
        src = source_path(rel).as_posix()
        for target, action, is_error in repoint_unstaged(path):
            # Annotations put each one in the PR's checks UI instead of only in
            # the log.  Harmless locally.
            if is_error:
                print(
                    "::error file={}::staged link to {} has no target in the repo".format(
                        src, target
                    )
                )
                dead += 1
                continue
            print("  -> {}: {} in {}".format(action, target, rel))
            print(
                "::warning file={}::staged link to {} repointed: {}".format(
                    src, target, action
                )
            )
            repointed += 1

    print(
        "staged {} files into {} ({} staging rewrite(s), {} unstaged link(s) fixed)".format(
            count, DOCS, rewrites, repointed
        )
    )
    if dead:
        # Every dead link is reported above before the build stops, so one run
        # names them all.
        print("{} link(s) with no target in the repo".format(dead), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
