---
# An instance of the People widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: people

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 68

title: Alumni
subtitle: Since 2013 we had the honor to host at UC San Diego a number of exceptional students and researchers.<br/>Thanks a lot for the incredible contributions to our lab. You will forever be part of the Weibel-Lab Family ❤️


content:
  # Choose which groups/teams of users to display.
  #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
  user_groups:
    - Postdocs and Senior Researchers (Alumni)
    - Ph.D Students (Alumni)
    - Master Students (Alumni)
    - Undergraduate Students (Alumni)

  # One heading over the Master's and undergraduate alumni, as on /people. The
  # groups stay separate in each person's user_groups; only the heading merges.
  # The era blocks are then computed across the combined set.
  merge_groups:
    - heading: Master and Undergraduate Students (Alumni)
      groups:
        - Master Students (Alumni)
        - Undergraduate Students (Alumni)

  # Only these groups are broken into "Class of" blocks. The Ph.D. and postdoc
  # alumni render as one list ordered by the year they finished.
  era_blocks:
    - Master Students (Alumni)
    - Undergraduate Students (Alumni)

  sort_by: Params.title
  sort_ascending: true


design:
  show_interests: false
  show_role: true
  show_social: true
---
