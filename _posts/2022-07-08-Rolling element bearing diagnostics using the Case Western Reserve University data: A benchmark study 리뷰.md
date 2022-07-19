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

Last update: 2022.07.20<br>

> `Rolling element bearing diagnostics using the Case Western Reserve University data: A benchmark study 리뷰'<br>
> > Mechanical Systems and Signal Processing Journal (IF: 8.934, rank: 97.45%, 2022.07.08 기준)

#### Index
---

- [1. Introduction](#1-introduction)
- [2. Bearing diagnosis fundamentals](#2-bearing-diagnosis-fundamentals)
- [3. CWRU testbed](#3-cwru-testbed)<br><br>

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
  - Ball pass frequency (outer race): ![LF](https://latex.codecogs.com/svg.image?BPFO=\frac{nf_r}{2}(1-\frac{d}{D}cos\phi))
  - Ball pass frequency (inner race): ![LF](https://latex.codecogs.com/svg.image?BPFI=\frac{nf_r}{2}(1&plus;\frac{d}{D}cos\phi))
  - Fundamenttal train frequency (cage speed): ![LF](https://latex.codecogs.com/svg.image?FTF=\frac{f_r}{2}(1-\frac{d}{D}cos\phi))
  - Ball (roller) spin frequency: ![LF](https://latex.codecogs.com/svg.image?BSF=\frac{Df_r}{2d}(1-[\frac{d}{D}cos\phi]^2))
    - Ball pass frequency는 ball (roller)가 inner race, 혹은 outer race에서 defect가 있는 부분과 접촉하는 주파수를 의미한다.
    - 위 식에서 ![LF](https://latex.codecogs.com/svg.image?f_r)은 shaft speed, ![LF](https://latex.codecogs.com/svg.image?n)은 rolling elements의 개수, 즉, ball의 수, ![LF](https://latex.codecogs.com/svg.image?\phi)는 radial plane을 기준으로 load가 걸린 angle, ![LF](https://latex.codecogs.com/svg.image?D,d)는 아래 그림 참고
    - 위 고장 주파수 관련 식들은 no slip을 가정하여 kinematic relationship을 세운 것이지만, 실제로는 slip이 항상 발생하기에, 계산된 frequency에서 1-2%의 variation이 있다고 봐야한다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/86653075/179837645-66b3ebc3-a259-4fca-93ae-4f4064c942eb.png" width="400" height="auto">
</p>

#### **3. CWRU testbed**

- 아래는 fault type별 envelope 적용 후 예상 발생 frequency에 관한 table

<p align="center">
  <img src="https://user-images.githubusercontent.com/86653075/179839488-f5625fee-66a1-42da-8d8a-295289c6dd47.png" width="1200" height="auto">
</p>

<br>

