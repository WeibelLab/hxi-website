---
aliases:
  - /project/convershive/
  - /project/convershive-live/
  - /project/empathiq/
title: 'Simulated Patients for Clinical Communication Training'
summary: 'An AI training platform for clinical communication: LLM-driven simulated patients stage difficult conversations, and social signal processing turns each rehearsal into interpretable feedback.'
authors:
  - Nadir Weibel
  - Manas Bedmutha
  - Gabriella Strudler
  - Canwen Wang
  - Chen Chen
  - Maca Peralta
  - Nishanth Chidambaram
  - Kaustubh Paliwal
  - Kayla Hom
  - Steven Rick

systems:
  - ConversHIVe
  - ConversHIVe-Live
  - EmpathIQ
tags:
  - HealthCare
  - Education
  - AI
  - Language

show_related: false

date: '2026-09-14T00:00:00Z'
external_link: ''
image:
  focal_point: Smart
  placement: 1
links: null
slides: ''
design:
  columns: '2'

weight: 5
---

------

### Overview

How a clinician talks to a patient is part of the care, not a skill layered on top of it. Communication quality determines whether trust is built, whether a patient discloses what matters, and whether bias is enacted in the room. While that much is established, the opportunity to practice a difficult conversation, and to learn afterwards how it went, is scarce for clinicians and trainees alike.

Our [UnBIASED](/project/unbiased/) work established that these dynamics are measurable: dominance, warmth, engagement, interactivity, and turn-taking can be extracted from real clinical conversations and modeled against how the interaction was experienced. This project turns that measurement into a training platform. Large language models and expressive speech synthesis drive simulated patients that behave like people rather than assistants: they hold information back, and their affect shifts in response to how they are treated, so trust has to be earned before a patient's underlying needs surface. Each rehearsed conversation is analyzed with the UnBIASED pipeline and returned through [ConverSense](/publication/2024-bedmutha-chi-conversense/) feedback, pairing time-aligned visualizations of the interaction with prompts that ask the learner to interpret their own behavior.

**ConversHIVe** applies the platform to HIV care teams, where implicit bias linked to sexual orientation and race affects access to care for people who have already faced stigma, and where clinics and community-based organizations work under limited time, staffing shortages, and turnover. Its second phase, **ConversHIVe-Live**, embeds the training in routine HIV service delivery.

**EmpathIQ** applies it to pre-clinical medical students, where empathy declines during training precisely as students meet the emotional load of clinical work, and where standardized patients and faculty-led workshops are effective but too resource-intensive to scale. EmpathIQ identifies the markers that distinguish empathic communication, varies patient affect within a single encounter, and evaluates whether the resulting feedback changes measured empathy and compassion.

------

### Funding and External Collaborations

**ConversHIVe** is funded by the [California HIV/AIDS Research Program (CHRP)](https://www.californiaaidsresearch.org/) under its Low Barrier Technology Interventions for HIV Prevention and Care program, with a second phase supporting real-world implementation. It is a collaboration between the [HXI Lab](https://hxi.ucsd.edu) and the [Owen Clinic](https://health.ucsd.edu/care/hiv/) at UC San Diego, the [AntiViral Research Center (AVRC)](https://avrc.ucsd.edu/) Community Advisory Board, and San Diego community-based organizations including Christie's Place, San Ysidro Health Center, and Father Joe's Villages.

**EmpathIQ** is supported by a Sanford Research Fellowship from the [T. Denny Sanford Institute for Empathy and Compassion](https://empathyandcompassion.ucsd.edu/) at UC San Diego, awarded to Manas Bedmutha, and is conducted with Drs. Lisa Eyler and Federica Klaus of the Sanford Institute and with Dr. Charles Goldberg, Associate Dean for Graduate Medical Education.

<div style="display: flex; justify-content:space-around; align-items: center;">
<img src="/images/chrp.png" style="height: 75px;">
<img src="/images/avrc.png" style="height: 90px;">
<img src="/images/ucsd_som.jpg" style="height: 120px;">
</div>
