---
title: 'UnBIASED: Understanding Biased patient-provider Interactions And Supporting Enhanced Discourse'
summary: 'Social signal processing for hidden bias in primary care: automated analysis of patient-provider communication, and feedback designed together with patients and doctors.'
authors: 
  - Nadir Weibel
  - Colleen Emmenegger
  - Steven Rick
  - Naba Rizvi
  - Andrea Hartzler (UW)
  - Wanda Pratt (UW)
  - Janice Sabin (UW)

tags:
  - HealthCare
  - AI
  - Sensing
  - Language

show_related: false

date: '2021-09-23T00:00:00Z'
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
lastmod: '2021-09-21T00:21:04.720Z'
design:
  columns: '2'

weight: 35
---

[//]: # (
<small> *Artistic rendering of ARTEMIS and its features. Left: a Novice Surgeon in Augmented Reality receiving help from a remote expert. Right: a Remote Expert Surgeon in VR interacting with a 3D point-cloud of the patient, and engaging with the novice on a surgical procedure.*</small>
)

------

### Overview

Healthcare bias, based on patients’ race, gender, sexual orientation, and other factors, leads to health disparities, such as lack of appropriate treatment and inadequate pain support. Such biases are often unintentional and “hidden” in communication between patients and doctors.

Existing approaches to address hidden bias are limited because they are removed from actual patient-doctor interactions in which bias hides. Technology offers an opportunity to design new approaches that can make den bias more visible and thus addressable.

We are investigating a new approach to address hidden healthcare bias by improving patient-doctor communication in primary care. This approach monitors body language for signs of bias and provides feedback to raise awareness of patients and doctors for opportunities to adjust their communication style.

We are partnering closely with patients and doctors to ensure this approach is guided by their experiences and needs. Through this collaborative effort, we expect to gain a deep understanding of how hidden bias is experienced and how we can address it better in the future.

*More Info here:* http://unbiased.health


------


### SocialLM

Assessing communication at scale is the bottleneck. **SocialLM** asks whether large language models can track social behaviors directly from clinical transcripts without fine-tuning, and finds that they can, but unevenly: performance varies by patient race and by segment of the visit. Because that variability is itself an equity problem, the work introduces an agreement-weighted ensemble that improves both accuracy and stability, giving a practical route to social signal tracking at scale.
------

### Funding and External Collaborations

UnBIASED ia a 5-year project, funded by the National Library of Medicine (NLMR01LM013301), and it is a collaboration between the University of Washington and the [HXI Lab](https://hxi.ucsd.edu) at UC San Diego. Our ultimate goal is to create tools to support patients and the next generation of doctors to have bias-free interactions that promote healthcare access, quality, and equity.


<div style="display: flex; justify-content:space-around; align-items: center;">
<img src="/images/UW.png" style="height: 50px;"> 
<img src="/images/NIH_Logo.jpg" style="height: 80px;"> 
<img src="/images/nih-nlm.png" style="height: 50px;">
</div>

