---
title: 'Preference Learning: Aligning AI to Human Preferences'
summary: 'Preference-based alignment for speech and audio: how people judge generated output, and whether annotation protocols validated on text transfer to what they hear.'
authors:
  - Nadir Weibel
  - Aaron Broukhim

tags:
  - AI
  - Language

show_related: false

date: '2026-09-15T00:00:00Z'
external_link: ''
image:
  focal_point: Smart
  placement: 1
links: null
slides: ''
design:
  columns: '2'

weight: 17
---

------

### Overview

Preference-based reinforcement learning aligns AI systems to human judgment by showing annotators two outputs and asking which is better. The annotation protocols, agreement statistics, and training objectives supporting this approach were designed and validated on text.

Much of what this lab builds produces speech rather than text, where timing, prosody, and tone carry meaning alongside the words. While preference learning is well established for language models, its transfer to audio is largely untested: a PRISMA-guided review of roughly 500 papers found that only 6% apply it to audio tasks.

Modality also changes the judgment itself. In a controlled cross-modal study of human and synthetic annotation, identical content produced different preference ratings depending on whether raters read it or heard it. Agreement statistics imported from the text literature can therefore measure something other than what they report.

This work supports the lab's speech and conversation projects, where feedback on how a clinician sounded, an AI persona that adapts its affect, and a simulated patient whose tone shifts all rest on defensible judgments that one generated utterance is better than another.

------

### Collaborations

This work is carried out with collaborators across UC San Diego, including [Prithviraj Ammanabrolu](https://prithvirajva.com/) in Computer Science and Engineering, and with Eshin Jolly.
