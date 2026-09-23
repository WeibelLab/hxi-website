#!/usr/bin/env python3
"""Add lab members to a project's author list based on its publications.

A publication declares which projects it belongs to in its `projects:` front
matter. This walks that link backwards: for every project, it collects the
authors of the publications attached to it and adds the ones that are lab
members but are not yet on the project page.

A lab member is someone with a profile directory under content/authors/. The
`_alumni` and `_undergrad` group pages are not people and are skipped. Authors
without a profile (external co-authors) are never added, because Hugo would
render them as plain text and the project page already names its external
collaborators in prose.

New names are inserted after the last lab member already listed, so the lab
stays grouped ahead of entries like "Andrea Hartzler (UW)".

Rerun it after adding publications or profiles:

    python3 scripts/sync-project-authors.py --dry-run
    python3 scripts/sync-project-authors.py

--check reports drift and exits 1 without writing. scripts/deploy-manual.sh runs
it that way, so a deploy cannot publish project pages that are out of step with
the publications.
"""

import collections
import glob
import os
import re
import sys

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def front_matter(path):
    text = open(path, encoding="utf-8").read()
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not match:
        return None, text
    return match.group(1), text


def get_list(block, name):
    """Read a YAML list written either as a block or inline."""
    match = re.search(r"^%s:[ \t]*\n((?:[ \t]*-[ \t].*\n?)+)" % name, block, re.M)
    if match:
        return [
            re.sub(r"^\s*-\s*", "", line).strip().strip("\"'")
            for line in match.group(1).splitlines()
            if line.strip()
        ]
    match = re.search(r"^%s:[ \t]*\[(.*?)\]" % name, block, re.M)
    if match:
        return [x.strip().strip("\"'") for x in match.group(1).split(",") if x.strip()]
    return []


def lab_members():
    """Map each person's display name to their profile slug."""
    people = {}
    for directory in sorted(glob.glob(os.path.join(REPO, "content/authors/*/"))):
        slug = os.path.basename(directory.rstrip("/"))
        if slug.startswith("_"):
            continue
        index = os.path.join(directory, "_index.md")
        if not os.path.exists(index):
            continue
        block, _ = front_matter(index)
        if not block:
            continue
        match = re.search(r"^title:\s*(.+)$", block, re.M)
        if match:
            people[match.group(1).strip().strip("\"'")] = slug
    return people


def authors_by_project():
    seen = collections.defaultdict(list)
    # sorted(): glob returns filesystem order, which differs between macOS and the
    # Linux CI runner, and that would change the order names are inserted in.
    for path in sorted(glob.glob(os.path.join(REPO, "content/publication/*/index.md"))):
        block, _ = front_matter(path)
        if not block:
            continue
        authors = get_list(block, "authors")
        for project in get_list(block, "projects"):
            for author in authors:
                if author not in seen[project]:
                    seen[project].append(author)
    return seen


def insert(text, additions, members):
    """Put the new names after the last lab member already in the list."""
    match = re.search(r"^(authors:[ \t]*\n)((?:[ \t]*-[ \t].*\n)+)", text, re.M)
    if not match:
        return None
    lines = match.group(2).rstrip("\n").split("\n")
    last_member = -1
    for i, line in enumerate(lines):
        if re.sub(r"^\s*-\s*", "", line).strip().strip("\"'") in members:
            last_member = i
    at = last_member + 1 if last_member >= 0 else len(lines)
    for offset, name in enumerate(additions):
        lines.insert(at + offset, "  - %s" % name)
    return text[: match.start(2)] + "\n".join(lines) + "\n" + text[match.end(2):]


def main():
    check = "--check" in sys.argv
    dry_run = check or "--dry-run" in sys.argv
    members = lab_members()
    changed = added = 0

    for project, authors in sorted(authors_by_project().items()):
        path = os.path.join(REPO, "content/project/%s/index.md" % project)
        if not os.path.exists(path):
            print("  no project page for %r, referenced by a publication" % project)
            continue
        block, text = front_matter(path)
        if not block:
            continue
        listed = get_list(block, "authors")
        additions = [a for a in authors if a in members and a not in listed]
        if not additions:
            continue
        print("%-22s + %s" % (project, ", ".join(additions)))
        changed += 1
        added += len(additions)
        if dry_run:
            continue
        updated = insert(text, additions, members)
        if updated is None:
            print("%-22s   could not parse its authors list, skipped" % "")
            continue
        open(path, "w", encoding="utf-8").write(updated)

    if check:
        if changed:
            print("\n%d projects are missing %d lab members." % (changed, added))
            print("Run: python3 scripts/sync-project-authors.py")
            sys.exit(1)
        print("project authors are in step with the publications")
        return

    print("\n%d projects, %d names%s" % (changed, added, " (dry run)" if dry_run else ""))


if __name__ == "__main__":
    main()
