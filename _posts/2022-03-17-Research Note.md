---
layout: post
title: "연구 노트 - Signal generation, Latent space analysis of GAN"
summary: "신호 생성 및 분석 관련 연구 노트"
author: taehun
date: '2022-03-17 23:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: GAN, PHM, Latent space analysis, Signal Generation, Digital twin, DeepLearning
permalink: /11
mathjax: true
use_math: true
---

> `신호 생성 및 분석 관련 연구 노트`

#### Index
---

- [1. Motivation](#1-motivation)
- [2. Idea](#2-idea)


#### **1. Motivation**
  
<br>

- Digital Twin의 용도 중 하나는 현실에서 발생할 수 있는 다양한 케이스를 시뮬레이션 하기 위함으로, 부족한 데이터를 활용하기보다는 생성을 통해 다양한 모델을 실험해볼 수 있음<br>
- 실제 산업에서는 완전한 고장 데이터는 거의 존재하지 않고, 서서히 고장으로 가는 것을 detection 하여 방지하는 것이 중요.
  - 테스트베드에서는 해당 데이터를 얻기 힘드므로, 정상 & 고장 데이터를 통해 고장의 level에 따른 데이터 생성할 수 있다면 현장 적용이 용이하지 않을지?<br>


#### **2. Idea**

<br>

- Feature generation 관련
  - Fault diagnosis model에서 어떤 feature가 유의미한지 확인 후 신호 생성보다는 feature를 생성하는 것이 더 나을지?<br><br>
- Quantitative metric 관련
  - Time domain에서는 차이가 커지도록, frequency domain에서는 차이가 작아지도록 adversarial하게 학습하는 방법? (loss는 미분가능한 함수로 선택)
  - Multivariate에서는 제곱의 평균 = 평균의 제곱 + 공분산인데, 공분산이 커질 경우 제곱의 평균 즉, L2 norm도 커지므로 high dimensional feature space에서 둘 간 거리도 멀어질 것이고, 이를 통해 uncertainty나 similarity를 측정할 수 있을지도.
  - 이미지의 diversity의 경우에는 Learned Perceptual Image Patch Similarity (LPIPS)를 이용하여 측정함
  - 신호처리를 가미한 positional encoding 방식 찾아보기<br><br>
- Compound fault 관련
  - KAMP data에서 looseness & unbalance 이용하여 compound fault<br><br>
- Semi-supervised 관련
  - 생성된 신호중 quality가 떨어지는 것들을 활용한 semi-supervised learning으로 feature를 학습한 다음 knowledge transfer으로 부족한 데이터들에 대한 classification 진행<br><br>
