---
title: Research
layout: page
permalink: /research/
---

## PhD Research

### Title

Language Models for Knowledge Extraction: From Non-Parametric Memory to Parametric Memory

### Summary

This research focuses on utilizing large language models (LLMs) for the task of knowledge extraction, addressing two distinct approaches: knowledge extraction from documents and treating LLMs themselves as knowledge bases. While factual accuracy is a significant concern, the core of the work lies in effectively extracting knowledge and ensuring its reliability. The evaluation of accuracy plays a central role, with an emphasis on assessing the performance of LLMs in specific domains and for certain relations. This research aims not only to improve the factual accuracy of LLMs but also to develop robust evaluation methodologies to measure their effectiveness in extracting knowledge across various contexts.

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