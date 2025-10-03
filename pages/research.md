---
title: Research
layout: page
permalink: /research/
---

## PhD Research

### Title

Measuring Parametric Knowledge in Large Language Models: Datasets, Benchmarks, and Decoding Protocols

### Summary

Large Language Models (LLMs) exhibit an emergent ability to store and retrieve factual knowledge, motivating their study as Language Models as Knowledge Bases (LM-as-KB). Yet, their practical deployment is hindered by unreliable evaluation metrics, poor calibration, and ambiguity in free-form generation. This thesis addresses these limitations through a three-part empirical investigation. First, we construct novel benchmark datasets—CASE (law), MUSART (multi-domain), and YAGO-QA (high-quality subsets)—to provide scalable and diverse ground truth for factuality evaluation. Second, we conduct large-scale experiments mapping the factual recall of LLMs across domains, model scales, and prompting strategies, revealing that standard exact-match metrics systematically underestimate knowledge and that factual performance is highly domain-dependent. Third, we analyze model calibration, demonstrating that verbalized confidence yields more reliable uncertainty estimates than token probabilities and enables selective question answering to trade coverage for accuracy. Finally, to overcome the ambiguities of free-form generation, we introduce Retrieval-Constrained Decoding (RCD), a novel evaluation protocol that constrains model output to a set of valid candidate entities. Collectively, these contributions provide a more complete and trustworthy understanding of the capabilities and limitations of modern LMs as knowledge repositories, offering a comprehensive framework for mapping, measuring, and managing the uncertainty of their knowledge.

## Publications

{% raw %}
Here's a list of my publications:

{% endraw %}

{% for publication in site.data.scholar_publications %}

### {{ publication.title }}

**Authors:** {{ publication.authors }}

**Conference:** {{ publication.conference }}

**Year:** {{ publication.year }}

**Abstract:** {{ publication.abstract }}

[Link to Publication]({{ publication.pdf_url }})

{% endfor %}