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

I am an AI/ML Software Engineer at Google LLC. I awarded my Ph.D. degree at the University of Miami College of Engineering Electrical and Computer Engineering Department.

My research interest includes Deep Learning, Bioinformatics, Artificial Intelligence, Engineering Management. I have published some papers at conferences and journals with total <a href='https://scholar.google.com/citations?user=369nl3gAAAAJ'>google scholar citations <strong><span id='total_cit'>87</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=369nl3gAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).


# 🔥 News
- *2024.12*: &nbsp;🎉🎉 [Contemporary Recommendation Systems on Big Data and Their Applications: A Survey](https://ieeexplore.ieee.org/document/10798416) is got published by IEEE Access
- *2024.12*: &nbsp;🎉🎉 Eliahu I and Joyce Jury Award, the best graduate in the Electrical and Computer Engineering department on 2024!
- *2025.05*: &nbsp;🎉🎉 EPIC 2025 Pitch and Innovation Challenge Finalist!
- *2025.06*: &nbsp;🎉🎉 [Assessing Sustainable Practices in Architecture: A Data-Driven Analysis of LEED Certification Adoption and Impact in Top Firms from 2000 to 2023](https://doi.org/10.1016/j.foar.2024.10.002) is online with the final version on Frontiers of Architectural Research (FoAR)
- *2025.10*: &nbsp;🎉🎉 [Who Said What (WSW2.0)? Enhanced Automated Analysis of Preschool Classroom Speech](https://ieeexplore.ieee.org/document/11204438) is got published by 2025 IEEE International Conference on Development and Learning (ICDL 2025), Prague
- *2025.10*: &nbsp;🎉🎉 [Analyzing Corporate ESG Reporting Through Data Mining: Evolutionary Trends and Strategic Model](https://doi.org/10.1080/23270012.2025.2563507) is got published by Journal of Management Analytics
- *2025.10*: &nbsp;🎉🎉 [Global Evolution of Social Responsibility in Smart-Service Industries: Insights From a Cross-Sector Hybrid Large Language Models Approach](https://onlinelibrary.wiley.com/doi/10.1002/csr.70257) is got published by Corporate Social Responsibility and Environmental Management


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
- [Global Evolution of Social Responsibility in Smart-Service Industries: Insights From a Cross-Sector Hybrid Large Language Models Approach](https://onlinelibrary.wiley.com/doi/10.1002/csr.70257), Ziyuan Xia, Saixing Zeng, **Anchen Sun**, Huabin Sun, Xiaodong Cai, **Corporate Social Responsibility and Environmental Management**, 2025
- [Analyzing Corporate ESG Reporting Through Data Mining: Evolutionary Trends and Strategic Model](https://doi.org/10.1080/23270012.2025.2563507), Ziyuan Xia, **Anchen Sun**, Xiaodong Cai, Saixing Zeng, **Journal of Management Analytics**, 2025
- [Who Said What (WSW 2.0)? Enhanced Automated Analysis of Preschool Classroom Speech](https://ieeexplore.ieee.org/document/11204438), **Anchen Sun**, Tiantian Feng, Gabriela Gutierrez, Juan J Londono, Anfeng Xu, Batya Elbaum, Shrikanth Narayanan, Lynn K Perry, Daniel S Messinger **2025 IEEE International Conference on Development and Learning (ICDL 2025)**
- [Assessing Sustainable Practices in Architecture: A Data-Driven Analysis of LEED Certification Adoption and Impact in Top Firms from 2000 to 2023](https://www.sciencedirect.com/science/article/pii/S2095263524001481), Jingyi Xu, Minghui Chen, **Anchen Sun**. **Frontiers of Architectural Research (FoAR)**, 2025
- [Who Said What? An Automated Approach to Analyzing Speech in Preschool Classrooms](https://arxiv.org/abs/2401.07342), **Anchen Sun**, et al. **2024 IEEE International Conference on Development and Learning (ICDL 2024)** 
- [Deep Contrastive Learning for Predicting Cancer Prognosis Using Gene Expression Values](https://doi.org/10.1093/bib/bbae544), **Anchen Sun**, Elizabeth J. Franzmann, Zhibin Chen, Xiaodong Cai. **Briefings in Bioinformatics (BIB)**, 2024
- [Rip Current Detection in Nearshore Areas through UAV Video Analysis with Almost Local-Isometric Embedding Techniques on Sphere (Extended Paper)](https://arxiv.org/abs/2304.11783), Kaiqi Yang, Stephen B. Leatherman, **Anchen Sun**, **PloS one**, Major Revision
- [Contemporary Recommendation Systems on Big Data and Their Applications: A Survey](https://arxiv.org/abs/2206.02631), Ziyuan Xia, **Anchen Sun**, Jingyi Xu, Yuanzhe Peng, Rui Ma, Minghui Cheng, **IEEE Access**, 2024
- [Mining the relationship between COVID-19 sentiment and market performance](https://arxiv.org/abs/2101.02587), Ziyuan Xia, Jeffery Chen, **Anchen Sun**, **PloS one**, 2024
- [Multimodal Data Integration and User Interaction for Avatar Simulation in Augmented Reality](https://www.igi-global.com/article/multimodal-data-integration-and-user-interaction-for-avatar-simulation-in-augmented-reality/304391), **Anchen Sun**, et al. **International Journal of Multimedia Data Engineering and Management (IJMDEM)**, 2022
- [Florida public hurricane loss model: Software system for insurance loss projection](https://onlinelibrary.wiley.com/doi/abs/10.1002/spe.3086), Yudong Tao, Tianyi Wang, **Anchen Sun**, et al. **Software: Practice and Experience**, 2022
- [Multimodal Data Integration for Interactive and Realistic Avatar Simulation in Augmented Reality](https://ieeexplore.ieee.org/abstract/document/9598519), **Anchen Sun**, et al. **2021 IEEE 22nd International Conference on Information Reuse and Integration for Data Science (IRI 2021), Las Vegas, NV, USA**
- [UAV-Video-Based Rip Current Detection in Near-Shore Areas](https://scholarship.miami.edu/view/pdfCoverPage?instCode=01UOML_INST&filePid=13356639800002976&download=true), **Anchen Sun**, **Master Thesis**, 2020

**Symposium, Conference Poster, and Presentation**
- [The role of teacher language in preschool language development](), Messinger, D. S., **Sun, A.**, Drye, M., Elbaum, B., Gutierrez, G., Londoño, J., Vitale, L., & Perry, L. K. (2025, August) **Symposium 11: Naturalistic observation of language development outside the home** (**Recipient of the Disciplinary Diversity & Integration Award in Cognitive Science**), **Annual Meeting of the Cognitive Science Society**, San Francisco, CA.
- [Understanding Emotion Words in Linguistically Diverse Preschool Classrooms](), Leland, E., **Sun, A.**, Londono, J., Gutierrez, G., Shearer, R., Messinger, D.S., & Perry, L.K. **(2025, May) Symposium to be presented at Society for Research in Child Development Biennial Meeting, Minneapolis, MN.**
- [Automated measurement of child MLU in a preschool classroom predicts assessed language ability](), **Anchen Sun**, Juan J Londoño, Batya Elbaum, Luis Estrada, Sophia Meibohm, Roberto Jose Lazo, Laura Vitale, Riccardo Fusaroli, Lynn K Perry, Daniel S Messinger, **International Congress of Infant Studies (ICIS) 2024 Pre-Conference in Developmental Research using Machine Learning and Computer Vision**
- [Understanding Emotion Language in Linguistically Diverse Inclusion Classrooms](), Eraine Leland, **Anchen Sun**, Kenyon Page, Daniel S. Messinger, Lynn K. Perry. **2024 Conference of the International Society for Research on Emotion (ISRE) Emotional Development Preconference**
- [Adult-Child Linguistic Interaction in Early Child Care: An Initial View from Reliable Automated Speech Transcription](), Juan Londoño, Batya Elbaum, **Anchen Sun**, Riccardo Fusaroli, Sophia Meibohm, Roberto Lazo, Luis Estrada, Laura Vitale, Lynn K. Perry, Daniel S. Messinger **International Congress of Infant Studies(ICIS) 2024**
- [Busy Preschool Classrooms: A Test Case for Assessing Reliability of Automated Speech Transcription](), Londoño, J., Elbaum, B., **Sun, A**., et al. **Florida Psycholinguistics Meeting**
- [Dynamic Analysis of Corporate ESG Reports: a Study Based on Knowledge Management Model](), Ziyuan Xia, **Anchen Sun**, Xiaodong Cai, Saixing Zeng. **2023 IEEE International Conference on Industrial Engineering and Engineering Management (IEEM)**

# 🎖 Honors and Awards
- *2025.05* EPIC 2025 Pitch and Innovation Challenge Finalist!
- *2024.12* Eliahu I and Joyce Jury Award, the best graduate in the Electrical and Computer Engineering department on 2024!
- *2022.03* [Anchen Sun is 2022 Research Day Poster Session Winners in Machine Learning and Computer Science Category.](https://news.miami.edu/coe/stories/2022/03/college-of-engineering-faculty-and-students-present-groundbreaking-research-on-research-day.html) 
- *2016 - 2017* [2016-17 Frost Institute for Date Science & Computing Fellows, University of Miami](https://idsc.miami.edu/2016-2017-idsc-fellows-present-interdisciplinary-projects/)
- *2007.07* National Olympiad in Informatics in Provinces (NOIP) Jiangsu 1st Award

# 📖 Educations
- *2020.08 - 2025.08*, University of Miami, Doctor of Philosophy (Ph.D.) in Electrical and Computer Engineering (Advisor: Dr. Xiaodong Cai)
- *2019.01 - 2020.05*, University of Miami, Master of Science (M.S.) with thesis option in Electrical and Computer Engineering.
- *2014.08 - 2017.12*, University of Miami, Bachelor of Science (B.S.) in Marine Science and Computer Science with Minor in Mathematics

# 💬 Invited Talks
- *2023.03*, AI module, ECE114 Global Challenges addressed by Engineering and Tech.

# 💻 Internships
- *2018.04 - 2018.08*, Statistical Programmer, [Biorasi LLC](https://biorasi.com/), FL, U.S.