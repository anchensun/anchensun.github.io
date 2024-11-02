---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a Ph.D. candidate and RA&TA at the University of Miami College of Engineering Electrical and Computer Engineering Department.

My research interest includes Deep Learning, Bioinformatics, Artificial Intelligence, Engineering Management. I have published some papers at conferences and journals with total <a href='https://scholar.google.com/citations?user=369nl3gAAAAJ'>google scholar citations <strong><span id='total_cit'>6</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=369nl3gAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).


# 🔥 News
- *2024.10*: &nbsp;🎉🎉 [Deep Contrastive Learning for Predicting Cancer Prognosis Using Gene Expression Values](https://doi.org/10.1093/bib/bbae544) is got accepted by Briefings in Bioinformatics (BIB)
- *2024.11*: &nbsp;🎉🎉 Assessing Sustainable Practices in Architecture: A Data-Driven Analysis of LEED Certification Adoption and Impact in Top Firms from 2000 to 2023 is got accepted by Frontiers of Architectural Research (FoAR)
# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Briefings in Bioinformatics</div><img src='images/Figure3.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Deep Contrastive Learning for Predicting Cancer Prognosis Using Gene Expression Values](https://doi.org/10.1093/bib/bbae544)

**Anchen Sun**, Elizabeth J. Franzmann, Zhibin Chen, Xiaodong Cai

**Abstract** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
Recent advancements in image classification have demonstrated that contrastive learning (CL) can aid in further learning tasks by acquiring good feature representation from a limited number of data samples. In this paper, we applied CL to tumor transcriptomes and clinical data to learn feature representations in a low-dimensional space. We then utilized these learned features to train a classifier to categorize tumors into a high- or low-risk group of recurrence. Using data from The Cancer Genome Atlas (TCGA), we demonstrated that CL can significantly improve classification accuracy. Specifically, our CL-based classifiers achieved an area under the receiver operating characteristic curve (AUC) greater than 0.8 for 14 types of cancer, and an AUC greater than 0.9 for 3 types of cancer. We also developed CL-based Cox (CLCox) models for predicting cancer prognosis. Our CLCox models trained with the TCGA data outperformed existing methods significantly in predicting the prognosis of 19 types of cancer under consideration. The performance of CLCox models and CL-based classifiers trained with TCGA lung and prostate cancer data were validated using the data from two independent cohorts. We also show that the CLCox model trained with the whole transcriptome significantly outperforms the Cox model trained with the 16 genes of Oncotype DX that is in clinical use for breast cancer patients. The trained models and the Python codes are publicly accessible and provide a valuable resource that will potentially find clinical applications for many types of cancer.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE ICDL 2024 Full Oral Presentation</div><img src='images/ICDL2024Workflow.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Who Said What? An Automated Approach to Analyzing Speech in Preschool Classrooms](https://ieeexplore.ieee.org/document/10644508/)

**Anchen Sun**, Juan J Londono, Batya Elbaum, Luis Estrada, Roberto Jose Lazo, Laura Vitale, Hugo Gonzalez Villasanti, Riccardo Fusaroli, Lynn K Perry, Daniel S Messinger

**Abstract** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
Young children spend substantial portions of their waking hours in noisy preschool classrooms. In these environments, children's vocal interactions with teachers are critical contributors to their language outcomes, but manually transcribing these interactions is prohibitive. Using audio from child- and teacher-worn recorders, we propose an automated framework that uses open source software both to classify speakers (ALICE) and to transcribe their utterances (Whisper). We compare results from our framework to those from a human expert for 110 minutes of classroom recordings, including 85 minutes from child-word microphones (n=4 children) and 25 minutes from teacher-worn microphones (n=2 teachers). The overall proportion of agreement, that is, the proportion of correctly classified teacher and child utterances, was .76, with an error-corrected kappa of .50 and a weighted F1 of .76. The word error rate for both teacher and child transcriptions was .15, meaning that 15% of words would need to be deleted, added, or changed to equate the Whisper and expert transcriptions. Moreover, speech features such as the mean length of utterances in words, the proportion of teacher and child utterances that were questions, and the proportion of utterances that were responded to within 2.5 seconds were similar when calculated separately from expert and automated transcriptions. The results suggest substantial progress in analyzing classroom speech that may support children's language development. Future research using natural language processing is under way to improve speaker classification and to analyze results from the application of the automated framework to a larger dataset containing classroom recordings from 13 children and 3 teachers observed on 17 occasions over one year.
</div>
</div>

**Journal and Conference Full Paper**
- Assessing Sustainable Practices in Architecture: A Data-Driven Analysis of LEED Certification Adoption and Impact in Top Firms from 2000 to 2023, Jingyi Xu, Minghui Chen, **Anchen Sun**. **Accepted by Frontiers of Architectural Research**
- [Who Said What? An Automated Approach to Analyzing Speech in Preschool Classrooms](https://arxiv.org/abs/2401.07342), **Anchen Sun**, et al. **2024 IEEE International Conference on Development and Learning (ICDL)** 
- [Dynamic Analysis of Corporate ESG Reports: A Model of Evolutionary Trends](https://arxiv.org/abs/2309.07001), Ziyuan Xia, **Anchen Sun**, Xiaodong Cai, Saixing Zeng.
- [Deep Contrastive Learning for Predicting Cancer Prognosis Using Gene Expression Values](https://doi.org/10.1093/bib/bbae544), **Anchen Sun**, Elizabeth J. Franzmann, Zhibin Chen, Xiaodong Cai. **Briefings in Bioinformatics**
- [Rip Current Detection in Nearshore Areas through UAV Video Analysis with Almost Local-Isometric Embedding Techniques on Sphere (Extended Paper)](https://arxiv.org/abs/2304.11783), **Anchen Sun**, Kaiqi Yang
- [Contemporary Recommendation Systems on Big Data and Their Applications: A Survey](https://arxiv.org/abs/2206.02631), Ziyuan Xia, **Anchen Sun**, Jingyi Xu, Yuanzhe Peng, Rui Ma, Minghui Cheng
- [Multimodal Data Integration and User Interaction for Avatar Simulation in Augmented Reality](https://www.igi-global.com/article/multimodal-data-integration-and-user-interaction-for-avatar-simulation-in-augmented-reality/304391), **Anchen Sun**, et al. **International Journal of Multimedia Data Engineering and Management (IJMDEM)**
- [Florida public hurricane loss model: Software system for insurance loss projection](https://onlinelibrary.wiley.com/doi/abs/10.1002/spe.3086), Yudong Tao, Tianyi Wang, **Anchen Sun**, et al. **Software: Practice and Experience**
- [Multimodal Data Integration for Interactive and Realistic Avatar Simulation in Augmented Reality](https://ieeexplore.ieee.org/abstract/document/9598519), **Anchen Sun**, et al. **2021 IEEE 22nd International Conference on Information Reuse and Integration for Data Science (IRI), Las Vegas, NV, USA**
- [Mining the relationship between COVID-19 sentiment and market performance](https://arxiv.org/abs/2101.02587), Ziyuan Xia, Jeffery Chen, **Anchen Sun**, **PloS one**
- [UAV-Video-Based Rip Current Detection in Near-Shore Areas](https://scholarship.miami.edu/view/pdfCoverPage?instCode=01UOML_INST&filePid=13356639800002976&download=true), **Anchen Sun**, **Master Thesis**

**Symposium, Conference Poster, and Presentation**
- [Automated measurement of child MLU in a preschool classroom predicts assessed language ability](), **Anchen Sun**, Juan J Londoño, Batya Elbaum, Luis Estrada, Sophia Meibohm, Roberto Jose Lazo, Laura Vitale, Riccardo Fusaroli, Lynn K Perry, Daniel S Messinger, **International Congress of Infant Studies (ICIS) 2024 Pre-Conference in Developmental Research using Machine Learning and Computer Vision**
- [Understanding Emotion Language in Linguistically Diverse Inclusion Classrooms](), Eraine Leland, **Anchen Sun**, Kenyon Page, Daniel S. Messinger, Lynn K. Perry. **2024 Conference of the International Society for Research on Emotion (ISRE) Emotional Development Preconference**
- [Adult-Child Linguistic Interaction in Early Child Care: An Initial View from Reliable Automated Speech Transcription](), Juan Londoño, Batya Elbaum, **Anchen Sun**, Riccardo Fusaroli, Sophia Meibohm, Roberto Lazo, Luis Estrada, Laura Vitale, Lynn K. Perry, Daniel S. Messinger **International Congress of Infant Studies(ICIS) 2024**
- [Busy Preschool Classrooms: A Test Case for Assessing Reliability of Automated Speech Transcription](), Londoño, J., Elbaum, B., **Sun, A**., et al. **Florida Psycholinguistics Meeting**
- [Dynamic Analysis of Corporate ESG Reports: a Study Based on Knowledge Management Model](), Ziyuan Xia, **Anchen Sun**, Xiaodong Cai, Saixing Zeng. **2023 IEEE International Conference on Industrial Engineering and Engineering Management (IEEM)**

# 🎖 Honors and Awards
- *2024.11* Eliahu I and Joyce Jury Award, the best graduate in the Electrical and Computer Engineering department on 2025!
- *2022.03* [Anchen Sun is 2022 Research Day Poster Session Winners in Machine Learning and Computer Science Category.](https://news.miami.edu/coe/stories/2022/03/college-of-engineering-faculty-and-students-present-groundbreaking-research-on-research-day.html) 
- *2016 - 2017* [2016-17 Frost Institute for Date Science & Computing Fellows, University of Miami](https://idsc.miami.edu/2016-2017-idsc-fellows-present-interdisciplinary-projects/)

# 📖 Educations
- *2020.08 - Present*, University of Miami, Doctor of Philosophy (Ph.D.) in Electrical and Computer Engineering (Advisor: Dr. Xiaodong Cai)
- *2019.01 - 2020.05*, University of Miami, Master of Science (M.S.) with thesis option in Electrical and Computer Engineering.
- *2014.08 - 2017.12*, University of Miami, Bachelor of Science (B.S.) in Marine Science and Computer Science with Minor in Mathematics

# 💬 Invited Talks
- *2023.03*, AI module, ECE114 Global Challenges addressed by Engineering and Tech.

# 💻 Internships
- *2018.04 - 2018.08*, Statistical Programmer, [Biorasi LLC](https://biorasi.com/), FL, U.S.