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
    - Interference structure: spectrogram은 quadratic form이므로, 두 신호 합의 spectrogram과 각 신호의 spectrogram의 합은 다름. Interference term이 추가 돼야 함.<br> 하지만 interference term인 cross-spectrogram은 각각의 spectrogram이 겹치는 region으로 제한되기에, 두 신호 ![Lf](https://latex.codecogs.com/svg.latex?\small&space;x_{1}(t), x_{2}(t))의 spectrogram이 겹치지 않을 정도로 충분히 멀면, interference term은 0에 수렴하게 됨.

#### **2. Problem Formulation**

<br>

- 
<br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/86653075/179837645-66b3ebc3-a259-4fca-93ae-4f4064c942eb.png" width="400" height="auto">
</p>
