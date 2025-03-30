---
title: Research
layout: page
permalink: /research/
---

## PhD Research

**Title:** Language Models for Knowledge Extraction: From Non-Parametric Memory to Parametric Memory

**Summary:**
This research focuses on utilizing large language models (LLMs) for the task of knowledge extraction, addressing two distinct approaches: knowledge extraction from documents and treating LLMs themselves as knowledge bases. While factual accuracy is a significant concern, the core of the work lies in effectively extracting knowledge and ensuring its reliability. The evaluation of accuracy plays a central role, with an emphasis on assessing the performance of LLMs in specific domains and for certain relations. This research aims not only to improve the factual accuracy of LLMs but also to develop robust evaluation methodologies to measure their effectiveness in extracting knowledge across various contexts.

## Publications

{% raw %}
Here's a list of my publications:

{% endraw %}

- **Title:** [A combined rule-based and machine learning approach for automated GDPR compliance checking](https://dl.acm.org/doi/abs/10.1145/3462757.3466081)
  **Authors:** Rajaa El Hamdani and Majd Mustapha and David Restrepo Amariles and Aurore Troussel and Sébastien Meeùs and Katsiaryna Krasnashchok
  **Conference:** ICAIL '21: Proceedings of the Eighteenth International Conference on Artificial Intelligence and Law
  **Year:** 2021
  **Abstract:** The General Data Protection Regulation (GDPR) requires data controllers to implement end-to-end compliance. Controllers must therefore ensure that the terms agreed with the data subject and their own obligations under GDPR are respected in the data flows from data subject to controllers, processors and sub processors (i.e. data supply chain). This paper seeks to contribute to bridge both ends of compliance checking through a two-pronged study. First, we conceptualize a framework to implement a document-centric approach to compliance checking in the data supply chain. Second, we develop specific methods to automate compliance checking of privacy policies. We test a two-modules system, where the first module relies on NLP to extract data practices from privacy policies. The second module encodes GDPR rules to check the presence of mandatory information. The results show that the text-to-text …

- **Title:** [JuriBERT: A masked-language model adaptation for French legal text](https://aclanthology.org/2021.nllp-1.9/)
  **Authors:** Stella Douka and Hadi Abdine and Michalis Vazirgiannis and Rajaa El Hamdani and David Restrepo Amariles
  **Conference:** NLLP @ EMNLP 2021
  **Year:** 2021
  **Abstract:** Language models have proven to be very useful when adapted to specific domains. Nonetheless, little research has been done on the adaptation of domain-specific BERT models in the French language. In this paper, we focus on creating a language model adapted to French legal text with the goal of helping law professionals. We conclude that some specific tasks do not benefit from generic language models pre-trained on large amounts of data. We explore the use of smaller architectures in domain-specific sub-languages and their benefits for French legal text. We prove that domain-specific pre-trained models can perform better than their equivalent generalised ones in the legal domain. Finally, we release JuriBERT, a new set of BERT models adapted to the French legal domain.

- **Title:** [Lex Rosetta: transfer of predictive models across languages, jurisdictions, and legal domains](https://dl.acm.org/doi/abs/10.1145/3462757.3466149)
  **Authors:** Jaromir Savelka and Hannes Westermann and Karim Benyekhlef and Charlotte S Alexander and Jayla C Grant and David Restrepo Amariles and Rajaa El Hamdani and Sébastien Meeùs and Aurore Troussel and Michał Araszkiewicz and Kevin D Ashley and Alexandra Ashley and Karl Branting and Mattia Falduti and Matthias Grabmair and Jakub Harašta and Tereza Novotná and Elizabeth Tippett and Shiwanni Johnson
  **Conference:** ICAIL '21: Proceedings of the Eighteenth International Conference on Artificial Intelligence and Law
  **Year:** 2021
  **Abstract:** In this paper, we examine the use of multi-lingual sentence embeddings to transfer predictive models for functional segmentation of adjudicatory decisions across jurisdictions, legal systems (common and civil law), languages, and domains (i.e. contexts). Mechanisms for utilizing linguistic resources outside of their original context have significant potential benefits in AI & Law because differences between legal systems, languages, or traditions often block wider adoption of research outcomes. We analyze the use of Language-Agnostic Sentence Representations in sequence labeling models using Gated Recurrent Units (GRUs) that are transferable across languages. To investigate transfer between different contexts we developed an annotation scheme for functional segmentation of adjudicatory decisions. We found that models generalize beyond the contexts on which they were trained (e.g., a model trained on …

- **Title:** [Performance in the courtroom: Automated processing and visualization of appeal court decisions in france](https://arxiv.org/abs/2006.06251)
  **Authors:** Paul Boniol and George Panagopoulos and Christos Xypolopoulos and Rajaa El Hamdani and David Restrepo Amariles and Michalis Vazirgiannis
  **Conference:** NLLP @ KDD 2020
  **Year:** 2020
  **Abstract:** Artificial Intelligence techniques are already popular and important in the legal domain. We extract legal indicators from judicial judgment to decrease the asymmetry of information of the legal system and the access-to-justice gap. We use NLP methods to extract interesting entities/data from judgments to construct networks of lawyers and judgments. We propose metrics to rank lawyers based on their experience, wins/loss ratio and their importance in the network of lawyers. We also perform community detection in the network of judgments and propose metrics to represent the difficulty of cases capitalising on communities features.

- **Title:** [Computational Indicators in the Legal Profession: Can Artificial Intelligence Measure Lawyers' Performance?](https://heinonline.org/HOL/LandingPage?handle=hein.journals/jltp2021&div=15&id=&page=)
  **Authors:** David Restrepo Amariles and Pablo Marcello Baquero and Paul Boniol and Rajaa El Hamdani and Michalis Vazirgiannis
  **Conference:** U. Ill. JL Tech. & Pol'y
  **Year:** 2021
  **Abstract:** The assessment of the legal professionals' performance is increasingly important in the market of legal services to provide relevant information both to consumers and to law firms regarding the quality of legal services. In this article, we explore how computational indicators are produced to assess lawyers' performance in courtroom litigation, analyzing the specific types of information they can generate. We capitalize on artificial intelligence (AI) methods to analyze a sample of 8,045 cases from the French Courts of Appeal, explore different associations involving lawyers, courts, and cases, and assess the strengths and flaws of the resulting metrics to evaluate the performance of legal professionals. The methods we use include natural language processing, machine learning, graph mining, and advanced visualization. Based on the examination of the resulting analytics, we uncover both the advantages and …

- **Title:** [Compliance generation for privacy documents under GDPR: A roadmap for implementing automation and machine learning](N/A)
  **Authors:** David Restrepo Amariles and Aurore Clément Troussel and Rajaa El Hamdani
  **Conference:** arXiv preprint arXiv:2012.12718
  **Year:** 2020
  **Abstract:** Most prominent research today addresses compliance with data protection laws through consumer-centric and public-regulatory approaches. We shift this perspective with the Privatech project to focus on corporations and law firms as agents of compliance. To comply with data protection laws, data processors must implement accountability measures to assess and document compliance in relation to both privacy documents and privacy practices. In this paper, we survey, on the one hand, current research on GDPR automation, and on the other hand, the operational challenges corporations face to comply with GDPR, and that may benefit from new forms of automation. We attempt to bridge the gap. We provide a roadmap for compliance assessment and generation by identifying compliance issues, breaking them down into tasks that can be addressed through machine learning and automation, and providing notes about related developments in the Privatech project.

- **Title:** [The Factuality of Large Language Models in the Legal Domain](https://dl.acm.org/doi/abs/10.1145/3627673.3679961)
  **Authors:** Rajaa El Hamdani and Thomas Bonald and Fragkiskos D Malliaros and Nils Holzenberger and Fabian Suchanek
  **Conference:** CIKM '24: Proceedings of the 33rd ACM International Conference on Information and Knowledge Management
  **Year:** 2024
  **Abstract:** This paper investigates the factuality of large language models (LLMs) as knowledge bases in the legal domain, in a realistic usage scenario: we allow for acceptable variations in the answer, and let the model abstain from answering when uncertain. First, we design a dataset of diverse factual questions about case law and legislation. We then use the dataset to evaluate several LLMs under different evaluation methods, including exact, alias, and fuzzy matching. Our results show that the performance improves significantly under the alias and fuzzy matching methods. Further, we explore the impact of abstaining and in-context examples, finding that both strategies enhance precision. Finally, we demonstrate that additional pre-training on legal documents, as seen with SaulLM, further improves factual precision from 63% to 81%.