---
layout: post
title: "Signal processing 관련 정리"
summary: "신호처리 관련 내용 정리"
author: taehun
date: '2022-08-16 12:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: Signal processing, STFT, Spectrogram, Wavelet, Scalogram
permalink: /19
mathjax: true
use_math: true
---

Last update: 2022.08.16<br>

> `Signal processing 관련 내용 정리'<br>

#### Index
---

- [1. Time & frequency domain](#1-time-&-frequency-domain)<br><br>

#### **1. Time & frequency domain**
  
<br>

- Spectrogram
  - STFT의 <br><br>

#### **2. Problem Formulation**

<br>

- 시계열 데이터의 일반적 세팅은 두가지 elements를 가짐: gender 같은, 시간에 무관한 static features와 vital signs과 같이 시간에 따라 변하는 temporal features
- 본 논문의 목적은 static feature와 temporal feature 쌍에 대해 실제 density function에 근사하도록 밀도 함수![Lf](https://latex.codecogs.com/svg.latex?\small&space;(\hat{p}(\mathbf{S},\mathbf{X}_{1:T})))를 학습하는 것
- Feature 쌍은 시계열의 길이, 차원, 데이터의 분포 등에 depend 하므로 일반적인 GAN에서 수행하기 어렵기에 autoregressive decomposition을 
- ![Lf](https://latex.codecogs.com/svg.latex?\small&space;p(\mathbf{S},\mathbf{X}_{1:T})=p(\mathbf{S})\prod&space;_{t}p(\mathbf{X_{t}}|\mathbf{S},\mathbf{X_{1:t-1}})) 을 통해 추가함

<br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/86653075/179837645-66b3ebc3-a259-4fca-93ae-4f4064c942eb.png" width="400" height="auto">
</p>
