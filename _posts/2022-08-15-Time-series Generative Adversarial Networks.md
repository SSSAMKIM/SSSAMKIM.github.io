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
> > 2019 NeurIPS Conference

#### Index
---

- [1. Abstract](#1-abstract)
- [2. Problem Formulation](#2-problem-formulation)
- [3. TimeGAN](#3-timegan)<br><br>

#### **1. Abstract**
  
<br>

- 시계열 데이터에 대한 좋은 생성 모델은 temporal dynamics를 잘 보존하는 것이라 함
  - 이 때 temporal dynamics는 학습 이후 시간대의 sequence들이 시간에 따라 변하는 변수들 사이의 original relationship을 잘 따르는 것을 의미
- 이전까지의 시계열 생성 모델들은 temporal correlation을 충분히 반영하지 못하고, 지도 학습 모델들은 deterministic하다는 문제점도 있음
- 따라서, 본 논문에서는 비지도 학습 모델의 flexibility와 지도 학습 모델의 control 능력을 결합한 방식을 제안하고자 함
- 방식은 지도 학습 기반과 적대적 방식의 목적 함수로 jointly 최적화하여 학습된 embedding space를 통해서 모델이 학습 데이터의 dynamics를 잘 반영하도록 함<br><br>

#### **2. Problem Formulation**

<br>

- 시계열 데이터의 일반적 세팅은 두가지 elements를 가짐: gender 같은, 시간에 무관한 static features와 vital signs과 같이 시간에 따라 변하는 temporal features
- 본 논문의 목적은 static feature와 temporal feature 쌍에 대해 실제 density function에 근사하도록 밀도 함수![Lf](https://latex.codecogs.com/svg.latex?\small&space;\hat{p}(\mathbf{S},\mathbf{X}_{1:T}))를 ![Lf](https://latex.codecogs.com/svg.latex?\small&space;p(\mathbf{S},\mathbf{X}_{1:T}))에 근사하도록 학습하는 것
- Feature 쌍은 시계열의 길이, 차원, 데이터의 분포 등에 depend 하므로 일반적인 GAN에서 수행하기 어렵기에 autoregressive decomposition을 
![Lf](https://latex.codecogs.com/svg.latex?\small&space;p(\mathbf{S},\mathbf{X}_{1:T})=p(\mathbf{S})\prod&space;_{t}p(\mathbf{X_{t}}|\mathbf{S},\mathbf{X_{1:t-1}})) 을 통해 추가함
- Two obejectives<br>
![Lf](https://latex.codecogs.com/svg.latex?\small&space;1.\underset{\hat{p}}{min}D(p(\mathbf{S},\mathbf{X_{1:T})||\hat{p}(\mathbf{S},\mathbf{X_{1:T})))<br>: Real/synthetic feature의 distribution의 차이를 줄이고자 하는 objective function으로, Jensen-Shannon divergence를 활용한다. D는 distributions 사이 거리를 측정하는 적절한 방법.<br>
![Lf](https://latex.codecogs.com/svg.latex?\small&space;2.\underset{\hat{p}}{min}D(p(\mathbf{X_{t}}|\mathbf{S},\mathbf{X_{1:T})||\hat{p}(\mathbf{X_{t}}|\mathbf{S},\mathbf{X_{1:T})))<br>: 길이 (t-1)에 대한 feature가 주어졌을 때 t번째 time step의 temporal feature에 대한 distribution 차이를 학습하는 objective function으로, Kullback-Leibler divergence를 활용한다.<br>

#### **3. TimeGAN**

- TimeGAN은 4개의 네트워크로 이루어짐: embedding function, recovery function, sequence generator, and sequence discriminator.
  - Embedding function은 feature space to latent space mapping function, recovery function은 latent space to feature space mapping function.
    - Embedding, recovery function은 architecture에 따라 parameterized 될 수 있음. 단지 autoregressive하고, causal ordering 하다는 것만 지키면 됨.
    - 이 때 autoregressive는 temporal convolution, causal ordering은 attention-based decoder를 사용.
  - Generator와 discriminator는 feature space가 아닌, embedding된 latent space에서 실행됨.

<p align="center">
  <img src="https://user-images.githubusercontent.com/86653075/184839646-f7cee316-ffea-4cb4-a1f5-46f473f49ba8.png" width="800" height="auto">
</p>

- 3가지 Loss function<br>
![Lf](https://latex.codecogs.com/svg.latex?\small&space;1.L_{R}=\mathbb{E}_{\mathbf{s},\mathbf{x}_{1:T}\sim p}[||\mathbf{s}-\mathbf{\tilde{s}||_{2}+\sum_{t}||\mathbf{x}_{t}-\mathbf{\tilde{x}_{t}}||_2])<br>
![Lf](https://latex.codecogs.com/svg.latex?\small&space;2.L_{U}=\mathbb{E}_{\mathbf{s},\mathbf{x}_{1:T}\sim&space;p}[logy_{\mathbf{S}}&plus;\sum_{t}log{y_{t}}]&plus;\mathbb{E}_{\mathbf{s},\mathbf{x}_{1:T}\sim&space;\hat{p}}[log(1-\hat{p}_{\mathbf{S}})&plus;\sum_{t}log(1-\hat{y}_{t})])<br>
![Lf](https://latex.codecogs.com/svg.latex?\small&space;3.L_{\mathbf{S}}=\mathbb{E}_{\mathbf{s},\mathbf{x}_{1:T}\sim p}[\sum_{t}||\mathbf{h}_{t}-g_{\chi}(\mathbf{h}_{\mathbf{S}},\mathbf{h}_{t-1},{mathb{z}_{t})||_{2}])

