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
  - STFT의 squared modulus를 계산하여 windowed signal에 대한 spectral energy density를 구하는 것이 spectrogram<br><br>
  ![Lf](https://latex.codecogs.com/svg.latex?\small&space;S_x(t,\nu)=\left|\int_{-\infty}^{&plus;\infty}x(u)h^*(u-t)e^{-j2\pi\nu&space;u}du&space;\right|^2)
  - STFT의 window h는 unit energy로 가정했기에, time-domain, frequency-domain 전 영역에 대한 적분을 통해 신호의 전체 에너지를 얻을 수 있음
  ![Lf](https://latex.codecogs.com/svg.latex?\small&space;\int_{-\infty}^{&plus;\infty}\int_{-\infty}^{&plus;\infty}S_x(t,\nu)dtd\nu=E_x)
  - 따라서, spectrogram은 time-frequency domain에서 신호의 (t,v)에 centered 된 격자들에 대한 에너지 측정 수단으로 해석할 수 있음<br>
  - Properties
    - Time and frequency covariance: spectrogram의 정의로 인해 time, frequency shifts가 보존됨
    - Time-frequency resolution: spectrogram은 STFT의 squared modulus이므로 time, frequency resolution 또한 STFT와 동일
    - Interference structure: spectrogram은 quadratic form이므로, 두 신호 합의 spectrogram과 각 신호의 spectrogram의 합은 다름. Interference term이 추가 돼야 함

#### **2. Problem Formulation**

<br>

- 시계열 데이터의 일반적 세팅은 두가지 elements를 가짐: gender 같은, 시간에 무관한 static features와 vital signs과 같이 시간에 따라 변하는 temporal features
- 본 논문의 목적은 static feature와 temporal feature 쌍에 대해 실제 density function에 근사하도록 밀도 함수![Lf](https://latex.codecogs.com/svg.latex?\small&space;(\hat{p}(\mathbf{S},\mathbf{X}_{1:T})))를 학습하는 것
- Feature 쌍은 시계열의 길이, 차원, 데이터의 분포 등에 depend 하므로 일반적인 GAN에서 수행하기 어렵기에 autoregressive decomposition을 
![Lf](https://latex.codecogs.com/svg.latex?\small&space;p(\mathbf{S},\mathbf{X}_{1:T})=p(\mathbf{S})\prod&space;_{t}p(\mathbf{X_{t}}|\mathbf{S},\mathbf{X_{1:t-1}})) 을 통해 추가함

<br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/86653075/179837645-66b3ebc3-a259-4fca-93ae-4f4064c942eb.png" width="400" height="auto">
</p>
