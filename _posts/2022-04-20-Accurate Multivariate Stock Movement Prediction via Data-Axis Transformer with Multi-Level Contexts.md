---
layout: post
title: "Accurate Multivariate Stock Movement Prediction via Data-Axis Transformer with Multi-Level Contexts 리뷰"
summary: "다변수 입력에 대한 주가 예측 관련 논문 리뷰"
author: taehun
date: '2022-04-20 22:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: Time series, Transformer, Forecasting, Attention mechanism
permalink: /16
mathjax: true
use_math: true
---

Last update:2022.04.21<br><br>

> 'ACM SIGKDD Conference on Knowledge Discovery and Data Mining Proceeding 리뷰`

#### Index
---

- [1. Introduction](#1-introduction)
- [2. Related Works](#2-related-works)<br><br>

- **Research gap**
  - Stock prediction에 대한 정확도를 높이기 위해서는 stock 간 correlation으 활용할 필요가 있다.
  - 그러나 Stock은 시장의 세계적이 흐름에 영향을 받기에, 비대칭성이 크고 유동적이므로 stock 간에 correlation을 정확히 얻는 것이 힘들다.<br><br>

- **Brief explanation for the proposed method**
  - Data-axis Transformer with Multi-Level contexts(DTML)으 활용항 비대칭적, 동적 상관관계를 아래 3가지를 활용하여 구한다.<br>
    1. 각 stock 내에서 temporal correlation을 계산한다.<br>
    2. Global market context에 기반하여 multi-level contexts를 구한다.<br>
    3. Inter-stock correlation을 계산하기 위해 transformer encoder를 활용한다.<br><br>
  
#### **1. Introduction**
  
<br>

- **Summary of introduction**
  - 대부분의 stock은 같은 산업군에 속한 sector로 cluster 되는 경향이 있다.<br>
  - Stock 간에 correlation을 활용하는 이전 연구들은 대체로 미리 정의된 sector list에 의존하나, 아래와 같은 한계점이 존재한다.<br>
    1. 특히 학습 데이터를 긴 기간에 걸쳐 학습할 수록 시간이 흐름에 따라 자연스럽게 변하는 stock correlation의 dynamic property를 알 수 없다는 문제가 있다.<br>
      (투자 확대 등으로 전체 stock이 상승하는 경우 그 correlation의 의미가 흐려질 수 있다는 의미?)<br>
    2. Sector가 모호하거나, sector 정보가 없는 경우 prediction model이 적용될 수 없다.<br>
    3. 예측 성능이 prediction model이 아닌, sector information의 quality에 강하게 의존한다.<br>
  - Data-axis Transformer with Multi-Level contexts(DTML) 요약<br>
    1. temporal attention을 활용하여 multivariate historical price를 요약하는 comprehensive context vector를 생성해 낸다.<br>
    2. 생성된 context vector를 시장의 global movement와 결합하여 multi-level로 확장시킨다.<br>
    3. Transformer encoder를 활용해서 multi-level context로부터 stock 간에 비대칭적, 동적 attention score를 학습한다.<br><br>


#### **2. Related Works**

<p align="center">
  <img src="https://user-images.githubusercontent.com/86653075/165923568-49c9d7b5-f680-497a-966f-071e522cfce9.png" width="800";height="auto";>
</p>

<br>
