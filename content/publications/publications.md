---
# An instance of the People widget.
# Documentation: https://wowchemy.com/docs/page-builder/
title: Publications
subtitle: 
widget: pages

# This file represents a page section.
headless: false

# Order that this section appears on the page.
weight: 68

content:
  # Page type to display. E.g. post, talk, publication...
  page_type: publication
  # Choose how much pages you would like to display (0 = all pages)
  count: 0
  # Choose how many pages you would like to offset by
  offset: 0
  # Page order: descending (desc) or ascending (asc) date.
  order: desc
  # Filter on criteria
  filters:
    tag: ''
    category: ''
    publication_type: ''
    author: ''
    
  filter_button:
    - name: All
      tag: '*'
    - name: Mixed Reality
      tag: MR
    - name: Surgery
      tag: Surgery
    - name: Computer Vision
      tag: CV
    - name: Art
      tag: Art
    - name: CHI
      tag: CHI
  #  - name: IEEEVR
  #    tag: IEEEVR
    
    
design:
  # Choose a view for the listings:
  #   1 = List
  #   2 = Compact
  #   3 = Card
  #   4 = Citation (publication only)
  view: 2
  # Choose how many columns the section has. Valid values: '1' or '2'.
  columns: 1
  
---
This is a list of all publications from our lab from the latest to the first. 