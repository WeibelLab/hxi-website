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

Matching is by exact name, because names are close enough to collide: the lab
has both a Chen Chen and a Feng Chen. When a publication spells someone
differently from their profile title, list the variants in that profile:

    title: Vish Ramesh
    name_variants:
      - Vishwajith Ramesh

Without that, the person is silently skipped and the check stays green. Run
--report-variants to list non-member names that resemble a profile.

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
    """Map every name a person publishes under to their profile slug.

    The profile title, plus any `name_variants`, all point at the same slug.
    """
    people, canonical_for = {}, {}
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
        if not match:
            continue
        canonical = match.group(1).strip().strip("\"'")
        people[canonical] = slug
        canonical_for[slug] = canonical
        for variant in get_list(block, "name_variants"):
            people[variant] = slug
    return people, canonical_for


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


def report_variants():
    """Flag non-member author names that look like an existing profile.

    Advisory only: a close name is as likely to be a different person (Chen Chen
    and Feng Chen) as a spelling variant, so this never fails a build. A real
    match is fixed by adding `name_variants` to that person's profile.
    """
    import difflib

    members, _ = lab_members()
    unknown = set()
    for path in sorted(glob.glob(os.path.join(REPO, "content/publication/*/index.md"))):
        block, _ = front_matter(path)
        if not block or not get_list(block, "projects"):
            continue
        for author in get_list(block, "authors"):
            if author not in members:
                unknown.add(author)

    hits = 0
    for name in sorted(unknown):
        close = difflib.get_close_matches(name, members.keys(), n=1, cutoff=0.75)
        if close:
            print("  %-28s resembles %r" % (name, close[0]))
            hits += 1
    print("\n%d of %d non-member names resemble a profile." % (hits, len(unknown)))
    print("If one is the same person, add it under name_variants in their profile.")


def main():
    if "--report-variants" in sys.argv:
        report_variants()
        return

    check = "--check" in sys.argv
    dry_run = check or "--dry-run" in sys.argv
    members, canonical_for = lab_members()
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
        listed_slugs = {members[a] for a in listed if a in members}
        # Add the profile title, not the spelling the paper used: Hugo keys the
        # author taxonomy on the title, and any other spelling renders as plain
        # text and never links to the person.
        additions = []
        for author in authors:
            slug = members.get(author)
            if slug is None or slug in listed_slugs:
                continue
            listed_slugs.add(slug)
            additions.append(canonical_for[slug])
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
