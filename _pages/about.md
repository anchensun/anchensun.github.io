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

I am an AI/ML Software Engineer at Google LLC, where I work in the **AI2 (Artificial Intelligence & Infrastructure)** organization on **AI Infrastructure**, **AI Agents**, and **Multi-Agent Systems** — building the platforms and agentic systems that bring large-scale AI to production. I earned my Ph.D. from the University of Miami College of Engineering, Department of Electrical and Computer Engineering.

My research interests span AI Infrastructure, AI Agents and Multi-Agent Systems, Deep Learning, Computational Psychology, and Engineering Management. I have published a number of papers at conferences and journals, with total <a href='https://scholar.google.com/citations?user=369nl3gAAAAJ'>Google Scholar citations <strong><span id='total_cit'>87</span></strong></a> (you can also use the Google Scholar badge <a href='https://scholar.google.com/citations?user=369nl3gAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=1a73e8&style=flat&label=citations"></a>).


# 🔥 News
- *2025.06* &nbsp;🎉🎉 [Assessing Sustainable Practices in Architecture: A Data-Driven Analysis of LEED Certification Adoption and Impact in Top Firms from 2000 to 2023](https://doi.org/10.1016/j.foar.2024.10.002) is online with the final version on Frontiers of Architectural Research (FoAR)
- *2025.10* &nbsp;🎉🎉 [Who Said What (WSW2.0)? Enhanced Automated Analysis of Preschool Classroom Speech](https://ieeexplore.ieee.org/document/11204438) is got published by 2025 IEEE International Conference on Development and Learning (ICDL 2025), Prague
- *2025.10* &nbsp;🎉🎉 [Analyzing Corporate ESG Reporting Through Data Mining: Evolutionary Trends and Strategic Model](https://doi.org/10.1080/23270012.2025.2563507) is got published by Journal of Management Analytics
- *2026.03* &nbsp;🎉🎉 [Global Evolution of Social Responsibility in Smart-Service Industries: Insights From a Cross-Sector Hybrid Large Language Models Approach](https://onlinelibrary.wiley.com/doi/10.1002/csr.70257) is published in Corporate Social Responsibility and Environmental Management, 33(2), 1815-1831
- *2026.05* &nbsp;🎉🎉 [Smart Service Social Responsibility (SSSR) Agent for Sustainability Disclosure and Corporate Governance]() has presented at the 2026 POMS Annual Conference, Grand Sierra Resort, Reno, NV


# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Corporate Social Responsibility and Environmental Management</div><img src='images/SSSR_Figure.png' alt="Smart Service Social Responsibility framework" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Global Evolution of Social Responsibility in Smart-Service Industries: Insights From a Cross-Sector Hybrid Large Language Models Approach](https://onlinelibrary.wiley.com/doi/10.1002/csr.70257)

Ziyuan Xia, Saixing Zeng, **Anchen Sun**, Huabin Sun, Xiaodong Cai

**Abstract** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
The rapid development of smart services has driven the evolution of social responsibility among global enterprises, while also presenting new challenges to their operational management. In the continuous iterations of smart services, the emerging digital ecosystem has demonstrated multidimensional characteristics, virtual-real integration, and multi-stakeholder interactions in management practices. This study introduces smart service social responsibility (SSSR), a comprehensive framework that extends traditional CSR and ESG models by integrating multidimensional, cross-space, and multi-stakeholder panoramic analyses to address the unique ethical and operational challenges of the digital ecosystem. Using a hybrid text-analysis methodology (TF-IDF scoring and LLM-based evaluation), we analyze 7858 sustainability reports across five major sectors (consumer goods, technology, financial, healthcare, and services) to reveal how firms prioritize sustainability issues and identify sector-specific patterns in smart-service industries. Our analysis reveals that environmental topics dominate, accounting for an average of 49.0% of dimension-level mentions and leading in four of the five sectors studied, whereas legal and ethical themes receive 42.25% fewer mentions on average. Meanwhile, physical space topics constitute nearly three-quarters (76.5%) of the total, in contrast to virtual space themes, which represent approximately one-quarter (23.5%). Furthermore, analysis of stakeholder attention reveals a strong focus on platforms (42.4%) and communities (23.8%), which together account for over 66.2% of the discourse, while emerging agents, such as algorithm engineers and smart bots, remain significantly underrepresented. The novelty of our research is demonstrated through uncovering how firms prioritize topics of social responsibility in sustainability reporting and revealing sector-specific patterns that highlight prominently featured content. These insights offer important guidance for regulators, businesses, and investors seeking to align smart-service frontiers with responsible practices.

**My role:** I designed the SSSR framework and the hybrid TF-IDF + LLM methodology behind the analysis.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE ICDL 2025</div><img src='images/WSW2_Table.png' alt="WSW 2.0 classroom language feature results" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Who Said What (WSW 2.0)? Enhanced Automated Analysis of Preschool Classroom Speech](https://ieeexplore.ieee.org/document/11204438)

**Anchen Sun**, Tiantian Feng, Gabriela Gutierrez, Juan J Londono, Anfeng Xu, Batya Elbaum, Shrikanth Narayanan, Lynn K Perry, Daniel S Messinger

**Abstract** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
This paper introduces an automated framework (WSW 2.0) for analyzing vocal interactions in preschool classrooms, enhancing both accuracy and scalability through the integration of wav2vec2-based speaker classification and Whisper (large-v2 and large-v3) speech transcription. A total of 235 minutes of audio recordings (160 minutes from 12 children and 75 minutes from 5 teachers), were used to compare system outputs to expert human annotations. WSW 2.0 achieves a weighted F1 score of .845, accuracy of .846, and an error-corrected kappa of .672 for speaker classification (child vs. teacher). Transcription quality is moderate to high with word error rates of .119 for teachers and .238 for children. WSW 2.0 exhibits relatively high absolute agreement intraclass correlations (ICC) with expert transcriptions for a range of classroom language features. These include teacher and child mean utterance length, lexical diversity, question asking, and responses to questions and other utterances, which show absolute agreement intraclass correlations between .64 and .98. To establish scalability, we apply the framework to an extensive dataset spanning two years and over 1,592 hours of classroom audio recordings, demonstrating the framework's robustness for broad real-world applications. These findings highlight the potential of deep learning and natural language processing techniques to revolutionize educational research by providing accurate measures of key features of preschool classroom speech, ultimately guiding more effective intervention strategies and supporting early childhood language development.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Frontiers of Architectural Research</div><img src='images/LEED_Paper.jpg' alt="LEED project distribution among top architecture firms, 2000–2020" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Assessing Sustainable Practices in Architecture: A Data-Driven Analysis of LEED Certification Adoption and Impact in Top Firms from 2000 to 2023](https://doi.org/10.1016/j.foar.2024.10.002)

Jingyi Xu, Minghui Cheng, **Anchen Sun**

**Abstract** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
Amid increasing global environmental concerns, the architectural industry is under increasing pressure to implement sustainable practices. Leadership in Energy and Environmental Design (LEED) certification has become a crucial benchmark for assessing green building practices. This study investigates the adoption and impact of LEED-certified projects within leading architectural firms from 2000 to 2023, utilizing a novel data mining framework to scan extensive datasets on LEED projects and firm operations. We introduce two key metrics: the Weighted LEED Achieved Score (WLAS) and the Green Impact Ratio (GIR), which evaluate the sustainability efforts of firms in relation to their market size and project scale. These metrics yield insights into how firms incorporate sustainability into their business and the environmental outcomes of their projects. Our research uncovers significant trends in LEED standard adoption, illustrating a strengthening commitment to sustainable buildings. The analysis underscores the strategic importance of these practices for securing a competitive edge and aligning with global sustainability objectives. This paper contributes to the sustainable architecture discourse by providing fresh insights into the integration and effectiveness of LEED certification among top firms and offering a comprehensive framework for evaluating the environmental and economic aspects of sustainability in architecture.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE ICDL 2024 Full Oral Presentation</div><img src='images/ICDL2024Workflow.png' alt="Who Said What automated speech analysis workflow" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Who Said What? An Automated Approach to Analyzing Speech in Preschool Classrooms](https://ieeexplore.ieee.org/document/10644508/)

**Anchen Sun**, Juan J Londono, Batya Elbaum, Luis Estrada, Roberto Jose Lazo, Laura Vitale, Hugo Gonzalez Villasanti, Riccardo Fusaroli, Lynn K Perry, Daniel S Messinger

**Abstract** <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
Young children spend substantial portions of their waking hours in noisy preschool classrooms. In these environments, children's vocal interactions with teachers are critical contributors to their language outcomes, but manually transcribing these interactions is prohibitive. Using audio from child- and teacher-worn recorders, we propose an automated framework that uses open source software both to classify speakers (ALICE) and to transcribe their utterances (Whisper). We compare results from our framework to those from a human expert for 110 minutes of classroom recordings, including 85 minutes from child-word microphones (n=4 children) and 25 minutes from teacher-worn microphones (n=2 teachers). The overall proportion of agreement, that is, the proportion of correctly classified teacher and child utterances, was .76, with an error-corrected kappa of .50 and a weighted F1 of .76. The word error rate for both teacher and child transcriptions was .15, meaning that 15% of words would need to be deleted, added, or changed to equate the Whisper and expert transcriptions. Moreover, speech features such as the mean length of utterances in words, the proportion of teacher and child utterances that were questions, and the proportion of utterances that were responded to within 2.5 seconds were similar when calculated separately from expert and automated transcriptions. The results suggest substantial progress in analyzing classroom speech that may support children's language development. Future research using natural language processing is under way to improve speaker classification and to analyze results from the application of the automated framework to a larger dataset containing classroom recordings from 13 children and 3 teachers observed on 17 occasions over one year.
</div>
</div>

**Journal and Conference Full Paper**
- [Global Evolution of Social Responsibility in Smart-Service Industries: Insights From a Cross-Sector Hybrid Large Language Models Approach](https://onlinelibrary.wiley.com/doi/10.1002/csr.70257), Ziyuan Xia, Saixing Zeng, **Anchen Sun**, Huabin Sun, Xiaodong Cai, **Corporate Social Responsibility and Environmental Management**, 33(2), 1815-1831, 2026
- [Analyzing Corporate ESG Reporting Through Data Mining: Evolutionary Trends and Strategic Model](https://doi.org/10.1080/23270012.2025.2563507), Ziyuan Xia, **Anchen Sun**, Xiaodong Cai, Saixing Zeng, **Journal of Management Analytics**, 2025
- [Who Said What (WSW 2.0)? Enhanced Automated Analysis of Preschool Classroom Speech](https://ieeexplore.ieee.org/document/11204438), **Anchen Sun**, Tiantian Feng, Gabriela Gutierrez, Juan J Londono, Anfeng Xu, Batya Elbaum, Shrikanth Narayanan, Lynn K Perry, Daniel S Messinger **2025 IEEE International Conference on Development and Learning (ICDL 2025)**
- [Assessing Sustainable Practices in Architecture: A Data-Driven Analysis of LEED Certification Adoption and Impact in Top Firms from 2000 to 2023](https://www.sciencedirect.com/science/article/pii/S2095263524001481), Jingyi Xu, Minghui Cheng, **Anchen Sun**. **Frontiers of Architectural Research (FoAR)**, 2025
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
- [Smart Service Social Responsibility (SSSR) Agent for Sustainability Disclosure and Corporate Governance](), Ziyuan Xia, Saixing Zeng, Jingyi Xu, **Anchen Sun** (2026, May) **2026 POMS Annual Conference** (Abstract 148-0802), Grand Sierra Resort, Reno, NV.
- [Machine Learning Goes to Preschool: Computing Communication](), Messinger, D. S., Drye, M., **Sun, A.**, Elbaum, B., Gutierrez, G., Londoño, J., Vitale, L., & Perry, L. K. (2025, September) **IEEE International Conference on Development and Learning (ICDL) Workshop: Using machine learning to track learning through interactions with the environment**, Prague, Czech Republic.
- [Who Said What (WSW 2.0)? Enhanced Automated Analysis of Preschool Classroom Speech](), Messinger, D. S., Drye, M., **Sun, A.**, Elbaum, B., Gutierrez, G., Londoño, J., Vitale, L., & Perry, L. K. (2025, September) **Poster presented at IEEE International Conference on Development and Learning (ICDL)**, Prague, Czech Republic.
- [The role of teacher language in preschool language development](), Messinger, D. S., **Sun, A.**, Drye, M., Elbaum, B., Gutierrez, G., Londoño, J., Vitale, L., & Perry, L. K. (2025, August) **Symposium 11: Naturalistic observation of language development outside the home** (**Recipient of the Disciplinary Diversity & Integration Award in Cognitive Science**), **Annual Meeting of the Cognitive Science Society**, San Francisco, CA.
- ["I heard he wants a happy face": Understanding Emotion Words in Linguistically Diverse Preschool Classrooms](), Leland, E., **Sun, A.**, Londoño, J., Gutierrez, G., Shearer, R., Messinger, D. S., & Perry, L. K. (2025, May) In E. Leland (chair) **"Tell me how you feel": Children's Emotion Vocabulary and Caregivers' Scaffolding of Social Emotional Skills**, **Society for Research in Child Development (SRCD) Biennial Meeting**, Minneapolis, MN.
- [Adult-Child Linguistic Interaction in Preschool Settings: An Initial View from Reliable Automated Speech Transcription](), Londoño, J., Elbaum, B., **Sun, A.**, Fusaroli, R., Meibohm, S. A., Lazo, R., Estrada, L., Vitale, L., Perry, L. K., & Messinger, D. S. (2024, July) In D. Messinger (chair) **Computational Approaches to Early Language Development**, **24th Biennial International Congress of Infant Studies (ICIS)**, Glasgow, Scotland.
- [Automated measurement of child MLU in a preschool classroom predicts assessed language ability](), **Anchen Sun**, Juan J Londoño, Batya Elbaum, Luis Estrada, Sophia Meibohm, Roberto Jose Lazo, Laura Vitale, Riccardo Fusaroli, Lynn K Perry, Daniel S Messinger, **International Congress of Infant Studies (ICIS) 2024 Pre-Conference in Developmental Research using Machine Learning and Computer Vision**
- [Understanding Emotion Language in Linguistically Diverse Inclusion Classrooms](), Leland, E., **Sun, A.**, Page, K., Messinger, D. S., & Perry, L. K. (2024, July) **Flash talk, Conference of the International Society for Research on Emotion (ISRE)**, Belfast, Ireland.
- [Language development in vivo: Computation for comprehending preschool classroom interaction](), Messinger, D., **Sun, A.**, Londoño, J., & Perry, L. K. (2024) **Invited symposium, Language Development in Humans and Machines**, **IEEE International Conference on Development and Learning (ICDL)**.
- [Busy Preschool Classrooms: A Test Case for Assessing Reliability of Automated Speech Transcription](), Londoño, J., Elbaum, B., **Sun, A.**, Meibohm, S., Lazo, R., Estrada, L., Vitale, L., Messinger, D. S., & Perry, L. K. (2023, October 21) **Poster presentation, Florida Psycholinguistics Meeting**, Gainesville, FL, United States.
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