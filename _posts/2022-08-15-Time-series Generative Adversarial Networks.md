---
layout: post
title: "Time-series Generative Adversarial Networks 리뷰"
summary: "시계열 데이터 생성에 관한 논문"
author: taehun
date: '2022-08-15 00:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: GAN, Time-series, temporal feature, static feature
permalink: /18
mathjax: true
use_math: true
---

Last update: 2022.08.15<br>

> `Time-series Generative Adversarial Networks 리뷰'<br>
> > NeurIPS Conference

#### Index
---

- [1. Abstract](#1-abstract)
- [2. Problem Formulation](#2-problem-formulation)<br><br>

#### **1. Abstractn**
  
<br>

- 시계열 데이터에 대한 좋은 생성 모델은 temporal dynamics를 잘 보존하는 것이라 함
  - 이 때 temporal dynamics는 학습 이후 시간대의 sequence들이 시간에 따라 변하는 변수들 사이의 original relationship을 잘 따르는 것을 의미
- 이전까지의 시계열 생성 모델들은 temporal correlation을 충분히 반영하지 못하고, 지도 학습 모델들은 deterministic하다는 문제점도 있음
- 따라서, 본 논문에서는 비지도 학습 모델의 flexibility와 지도 학습 모델의 control 능력을 결합한 방식을 제안하고자 함
- 방식은 지도 학습 기반과 적대적 방식의 목적 함수로 jointly 최적화하여 학습된 embedding space를 통해서 모델이 학습 데이터의 dynamics를 잘 반영하도록 함<br><br>

#### **2. Problem Formulation**

<br>

- 시계열 데이터의 일반적 세팅은 두가지 elements를 가짐: gender 같은, 시간에 무관한 static features와 vital signs과 같이 시간에 따라 변하는 temporal features
- 본 논문의 목적은 static feature와 temporal feature 쌍에 대해 실제 density function에 근사하도록 밀도 함수![Lf](https://latex.codecogs.com/svg.latex?\small&space;\hat{p}(\mathbf{S},&space;\mathbf{X}_{1:T}))를 학습하는 것
- Feature 쌍은 시계열의 길이, 차원, 데이터의 분포 등에 depend 하므로 일반적인 GAN에서 수행하기 어렵기에 autoregressive decomposition을 추가함
  - ![Lf](https://latex.codecogs.com/svg.latex?\small&space;p(\mathbf{S},\mathbf{X}_{1:T})=p(\mathbf{S})\prod&space;_tp(\mathbf{X_t}|\mathbf{S},\mathbf{X_{1:t-1}})

https://latex.codecogs.com/svg.image?p(\mathbf{S},\mathbf{X}_{1:T})=p(\mathbf{S})\prod&space;_tp(\mathbf{X_t}|\mathbf{S},\mathbf{X_{1:t-1}})

<br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/86653075/179837645-66b3ebc3-a259-4fca-93ae-4f4064c942eb.png" width="400" height="auto">
</p>
