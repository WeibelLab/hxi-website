---
widget: portfolio
title: Current Research Projects
#headless: true  # This file represents a page section.

weight: 10
# ... Put Your Section Options Here (title etc.) ...

content:
  # Page type to display. E.g. project.
  page_type: project

  # Earlier projects render in their own section further down this page
  # (content/research/foundations.md), so keep them out of this one.
  filters:
    exclude_tags:
      - Earlier

  # Two independent axes whose selections combine, and which filter both this
  # section and the Earlier Projects section below. Rendered by the local
  # portfolio widget override; combined by assets/js/project-filters.js.
  filter_axes:
    - name: Domain
      buttons:
        - {name: All, tag: '*'}
        - {name: Health & Care, tag: HealthCare}
        - {name: Mental Health, tag: MentalHealth}
        - {name: Education, tag: Education}
        - {name: Collaboration, tag: Collaboration}
        - {name: Society, tag: Society}
        - {name: Mobility & Safety, tag: Mobility}
    - name: Technology
      buttons:
        - {name: All, tag: '*'}
        - {name: AI, tag: AI}
        - {name: XR, tag: XR}
        - {name: Sensing, tag: Sensing}
        - {name: Language, tag: Language}
        - {name: Fabrication, tag: Fabrication}

# Uncomment to only show content with specific tags
#  filters:
#    tags:
#      - featured project


design:
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns: '1'
  # Toggle between the various page layout types.
  #   1 = List
  #   2 = Compact  
  #   3 = Card
  #   5 = Showcase
  view: 3
  # For Showcase view, flip alternate rows?
  flip_alt_rows: true

---
Our work is at the intersection of Human-Computer Interaction (**HCI**), Artificial Intelligence (**AI**), eXtended Reality (**XR**) and Human-Centered Design (**HCD**). We strive to understand how pervasive and emerging technologies can help bridge the gap between the physical and digital worlds, especially in health & healthcare and education, and above all in life- and time-critical settings where the cost of a breakdown is immediate. 

HXI's work has been funded by the [National Institutes of Health (NIH)](http://nih.gov), the [National Science Foundation (NSF)](http://nsf.gov), the [Agency for Healthcare Research and Quality (AHRQ)](http://ahrq.gov), the [Department of Veteran Affairs (VA)](http://va.gov), the [Center for AIDS Research (CFAR)](https://cfar.ucsd.edu/), the [UC San Diego Office of Research Affairs](https://research.ucsd.edu/), the [Robert Wood Johnson Foundation](http://rwjf.org), the Moxie Foundation, the [Swiss National Science Foundation (SNSF)](http://snsf.ch), the [European Commission (FP6)](https://ec.europa.eu/eurostat/cros/content/fp6-projects_en), the [California HIV/AIDS Research Program (CHRP)](https://www.californiaaidsresearch.org/), the [Naval Medical Center San Diego](https://sandiego.tricare.mil/), the [T. Denny Sanford Institute for Empathy and Compassion](https://empathyandcompassion.ucsd.edu/), [Intuitive Surgical](https://www.intuitive.com/), [IBM Research](https://research.ibm.com//), [Lytx](https://www.lytx.com/), [Adobe Research](https://research.adobe.com/) and [Boeing](https://www.boeing.com/).
