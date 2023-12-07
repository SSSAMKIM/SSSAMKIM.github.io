---
layout: post
title: "Statistical Spectral Analysis for Fault Diagnosis of Rotating Machines 논문 리뷰"
summary: "Statistical Spectral Analysis for Fault Diagnosis of Rotating Machines 논문 리뷰"
author: taehun
date: '2023-12-06 17:00:00 +0900'
category: Literature_review
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: Python
permalink: /25
mathjax: true
use_math: true
---

Last update: 2023.12.07<br>

> `Statistical Spectral Analysis for Fault Diagnosis of Rotating Machines 논문 리뷰'
> > IEEE Transactions on Industrial Electronics (IF: 7.7, rank: 94.4%, 2023.12.07 기준)<br>

<br>

#### Index
---

- [1. Abstract](#1-abstract)
- [2. Methods](#2-methods)<br><br>

#### **1. Abstract**
  
<br>

> - 회전체 고장 진단을 위해 강건한 features를 추출하는 것이 핵심이며, 이는 신호의 품질과 연관되어 있음
>   - Quasi-stationary 특성을 보이는 진동 신호에서, 주파수 영역에서 추출한 features의 quality가 SNR, 운행 조건 변화, 데이터 segmentation 변화(sliding window size 등)에 dependency를 가짐<br>

- 이를 달성하기 위해,

> - 진동 신호의 spectral contents의 amplitudes가 정렬되고, statistical spectral images로 transformed 됨<br>
> - 위 sort operation을 통해 얻은 images들로부터 각 주파수 영역대 크기에 대한 empirical cumulative distribution function (ECDF)를 얻어서 고장 진단에 활용<br>

<br>

#### **2. Methods**

<br>

> 제안 방법 3가지 4개의 main steps
> > **1) Time segmentation**
> >    - 다양한 길이(fixed periodic Hamming window로 segmentation)로 이루어진 진동 신호의 time segments들을 randomly divde <br><br>
> > **2) Statistical spectral image construction**
> >    - x축은 주파수 영역대, y축은 time segment<br>
> > **3) ECDF calculation**
> >    - 각 주파수 영역대의 amplitudes가 sorted 되고, 이 sort operation은 각 주파수 영역대의 amplitude distribution의 statistical information을 얻기 위해 필요<br>
> >    - Sort operation을 통해 univariate ECDF obtain하며, ECDF는 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/83e7ec8f-ead3-43eb-a3b5-9184b5d9c2ee)로 정의됨<br>
> >    - 이 때 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/3d401909-672d-4f35-a85e-4431f587eada)는 Bernoulli distribution이고 F(x)를 parameter로 가짐, 즉 P(X=1)=F(x), P(x=0)=1-F(x)<br>
> >    - ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/6336c7e7-6dc5-42cf-8933-33f31bf8a351)은 Bernoulli distribution을 n번 시행한 것과 같으므로 결국 binomial distribution이며, ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/d65da1ea-51f1-4cf7-ad23-393e8ea6810b)는 표본평균에 해당하므로 unbiased estimator가 됨<br>
> > 4) Distance calculation

<br>

#### **2-1. Statistical spectral analysis**

<br>

