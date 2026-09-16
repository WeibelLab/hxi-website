---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Context recognition in-the-wild: Unified model for multi-modal sensors and
  multi-label classification'
subtitle: 'IMWUT 2018'
summary: '<b>IMWUT 2018</b><br>Automatic recognition of behavioral context (location, activities, body-posture etc.) can serve health monitoring, aging care, and many other domains.'
authors:
- Yonatan Vaizman
- Nadir Weibel
- Gert Lanckriet
tags: []
categories: []
date: '2018-01-01'
lastmod: 2021-09-23T15:50:49-07:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2021-09-23T22:50:48.719389Z'
publication_types:
- '2'
abstract: 'Automatic recognition of behavioral context (location, activities, body-posture etc.) can serve health monitoring, aging care, and many other domains. Recognizing context in-the-wild is challenging because of great variability in behavioral patterns, and it requires a complex mapping from sensor features to predicted labels. Data collected in-the-wild may be unbalanced and incomplete, with cases of missing labels or missing sensors. We propose using the multiple layer perceptron (MLP) as a multi-task model for context recognition. Based on features from multi-modal sensors, the model simultaneously predicts many diverse context labels. We analyze the advantages of the model''s hidden layers, which are shared among all sensors and all labels, and provide insight to the behavioral patterns that these hidden layers may capture. We demonstrate how recognition of new labels can be improved when utilizing a model that was trained for an initial set of labels, and show how to train the model to withstand missing sensors. We evaluate context recognition on the previously published ExtraSensory Dataset, which was collected in-the-wild. Compared to previously suggested models, the MLP improves recognition, even with fewer parameters than a linear model. The ability to train a good model using data that has incomplete, unbalanced labeling and missing sensors encourages further research with uncontrolled, in-the-wild behavior.'
publication: '*Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous
  Technologies*'
---
