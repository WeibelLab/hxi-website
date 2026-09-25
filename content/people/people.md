---
# An instance of the People widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: people

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 68

title: Meet the Team
subtitle: The HXI Team is composed by an interdisciplinary crew of students and researchers spanning engineering, design, and health sciences.<br/>Previous members of the lab are listed in our <a href="/alumni">Alumni page</a>.


content:
  # Choose which groups/teams of users to display.
  #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
  user_groups:
  - Director
  - Ph.D Students
  - Researchers
  - Postdocs
  - Master Students
  - Undergraduate Students

  # Render several groups under one heading. The groups themselves stay
  # separate, so each person's user_groups still records their cohort; this
  # only avoids headings with one or two people under each.
  #
  # A group with nobody in it is skipped, heading and all, so "Postdocs" can sit
  # here and appear the moment someone is filed under it.
  #
  # These names are finer-grained than the alumni page's, which still lumps
  # postdocs and senior researchers into one group.
  merge_groups:
    - heading: Ph.D Students, Researchers, and Postdocs
      groups:
        - Ph.D Students
        - Researchers
        - Postdocs
    - heading: Master and Undergraduate Students
      groups:
        - Master Students
        - Undergraduate Students

  # Current members carry only a start year in `years`; "present" is implicit.
  # Longest-serving first.
  years_order: asc

design:
  show_interests: false
  show_role: true
  show_social: true
---
