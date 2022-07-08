---
layout: post
title: "Rolling element bearing diagnostics using the Case Western Reserve University data: A benchmark study 리뷰"
summary: "CWRU bearing dataset에 대한 적합성 검증 논문"
author: taehun
date: '2022-07-08 21:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: Rolling element bearing, CWRU, PHM
permalink: /17
mathjax: true
use_math: true
---

Last update: 2022.07.08<br>

> `Rolling element bearing diagnostics using the Case Western Reserve University data: A benchmark study 리뷰'<br>
> > Mechanical Systems and Signal Processing Journal (IF: 8.934, rank: 97.45%, 2022.07.08 기준)

#### Index
---

- [1. Introduction](#1-introduction)
- [2. Bearing diagnosis fundamentals](#2-bearing-diagnosis-fundamentals)<br><br>

#### **1. Introduction**
  
<br>

- **Summary of introduction**
  - CWRU 데이터의 경우 어떤 신호는 고전적인 베어링 고장 특성이 두드러지게 보이나, 또다른 데이터들은 그런 특성들이 보이지 않고, 다른 고장 증상들도 보임
    - 이러한 이유로 benchmark study를 이 논문에서 진행하게 됨<br><br>

#### **2. Bearing diagnosis fundamentals**

<br>

- **Impressive parts**
  - 고장이 발생한 위치(내륜, 외륜, 볼베어링 등)가 impulse response의 특성을 결정 짓는다고 볼 수 있음. 즉, 고장 위치에 따른 신호 차이가 발생
  - 베어링 진단에서 핵심은 포락선 신호로, 진폭 복조(amplitude demodulation)를 통해 얻을 수 있으며 원신호보다 더 선명한 고장 신호를 보임
  - ![LF](https://latex.codecogs.com/svg.image?BPFO=\frac{nf_r}{2}(1-\frac{d}{D}cos\phi))
  - ![fffd](https://user-images.githubusercontent.com/86653075/177991220-ad0fb6db-5f22-4900-b2bd-0eda7d849f33.gif)


<br>

