---
title: 'Designing Smart and Autonomous Vehicles'
summary: Understanding and designing the interaction between people and increasingly automated vehicles, from calibrating trust in autonomous vehicle decisions, to VR simulation and sensing of driver behavior, to coaching human drivers at fleet scale.
authors: 
  - Nadir Weibel
  - Robert Kaufman
  - Matin Yarmand
  - Nishanth Chidambaram
  - Weichen Liu
  - Gabriella Strudler
  - Vivian Xiang
  - Huimeng Lu
  - Pari Hathiram
  - Emi Lee
tags:
  - Mobility
  - Society
  - AI
  - XR
show_related: false
date: '2023-05-25T00:00:00Z'
external_link: ''
image:
  focal_point: Smart
  placement: 1
links: null
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
slides: ''
lastmod: '2025-07-11T00:00:00Z'
design:
  columns: '2'

weight: 40
---
 
------
### Overview
Despite huge advancements in Autonomous Vehicle (AV) technology, real-world adoption is hindered by a lack of calibrated passenger trust in vehicle decisions. In this research agenda, we combine Virtual Reality (VR), biometric measurement, human-centered design, and data science methods to uncover factors impacting trust with Autonomous Vehicles (AVs) at the level of the individual as opposed to taking a one-size-fits-all approach.

We aim to establish a generalizable theory connecting personal characteristics to AV communications in realistic driving contexts as well as underpin why certain designs are more effective than others at eliciting calibrated trust, improving driving outcomes through enhanced situational awareness, and alleviating stress. This research agenda will inform future driver-AV interactions and impact important design decisions for the automotive and self-driving car industry in the years ahead.

------
### Calibrating Trust in Autonomous Vehicles

Trust in an AV is not uniform across passengers, so we study it at the level of the individual. Surveying 1,457 young adults across psychosocial traits, cognitive attributes, driving style, prior experience, and perceived risks and benefits, and modeling the results with machine learning and SHAP, we find that perceptions of AV risks and benefits, attitudes toward feasibility and usability, institutional trust, prior experience, and mental models predict trust far better than psychosocial traits or driving style do.

How the vehicle communicates matters just as much as who is listening. In a simulated driving study with 232 participants, errors in an AV's explanations reduced comfort in relying on the vehicle, confidence in its ability, and explanation satisfaction, even though the driving itself was identical. Perceived harm and driving difficulty amplified the damage, so the contexts where an explanation matters most are also the ones where getting it wrong costs most.

Together these results argue against one-size-fits-all AV communication, and toward explanations matched to the passenger and the situation.

------
### Simulating and Sensing the Driver

Studying any of this requires being able to observe a driver closely without putting anyone on a real road. Head-mounted VR makes that possible, but existing simulators tend to track only eye movement, and their bulky outside-in rigs and Unreal-based architectures put them out of reach for most interaction researchers.

**DriveSimQuest** is our answer: a VR driving simulator and research platform built on the Meta Quest Pro and Unity, capturing gaze, facial expression, hand activity, and full-body gesture in real time. It is deliberately easy to deploy, so that studying drivers' affective states becomes a matter of designing the study rather than building the rig.

That platform is what lets the rest of this work ask sharper questions, about what a driver is attending to, what they are feeling, and when a system should intervene.

------
### Coaching Human Drivers at Fleet Scale

The same safety-critical setting looks different when the driver is a person rather than a system. Fleet drivers are involved in collisions that impose severe financial costs and endanger lives, and fleet companies lean on one-to-one coaching to prepare them. Yet the people, practices, and technologies that shape that coaching have remained largely unexamined.

We characterize fleet coaching from both sides, surveying coaches about current practice and interviewing drivers about how coaching actually lands. Manager-led coaching outperforms self-coaching across experiential outcomes, and the reasons why point toward what would have to be true for coaching to scale without losing the relationship that makes it work.

------
### Funding and External Collaborations

The autonomous vehicle trust work is a collaboration between the UCSD departments of Cognitive Science, Computer Science and Engineering, and external industry partners. The fleet driver coaching research is conducted with [Lytx](https://www.lytx.com/).

<div style="display: flex; justify-content:space-around; align-items: center;">
<img src="/images/CSE.jpg" style="height: 90px;">
<img src="/images/lytx.svg" style="height: 55px;">
</div>

------

### Publications

{{< cite page="/publication/2025-chidambaram-uist-drivesimquest" view="1" >}}
{{< cite page="/publication/2025-weibel-escholarship-fleet-coaching" view="1" >}}
{{< cite page="/publication/2025-weibel-escholarship-coaching-methodologies" view="1" >}}
{{< cite page="/publication/2025-kaufman-chi-predictingtrust" view="1" >}}
{{< cite page="/publication/2025-kaufman-chi-whatdidmycarsay" view="1" >}}
