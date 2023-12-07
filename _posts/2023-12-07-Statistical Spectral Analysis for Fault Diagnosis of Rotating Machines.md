---
layout: post
title: "Statistical Spectral Analysis for Fault Diagnosis of Rotating Machines 논문 리뷰"
summary: "Statistical Spectral Analysis for Fault Diagnosis of Rotating Machines 논문 리뷰"
author: taehun
date: '2023-12-07 12:00:00 +0900'
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

- 제안 방법 3가지 4개의 main steps<br>
> [1] Time segmentation
> - 다양한 길이(fixed periodic Hamming window로 segmentation)로 이루어진 진동 신호의 time segments들을 randomly divde<br>

> [2] Statistical spectral image construction
> - x축은 주파수 영역대, y축은 time segment<br>

> [3] ECDF calculation
> - 각 주파수 영역대의 amplitudes가 sorted 되고, 이 sort operation은 각 주파수 영역대의 amplitude distribution의 statistical information을 얻기 위해 필요<br>
> - Sort operation을 통해 univariate ECDF obtain하며, ECDF는 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/83e7ec8f-ead3-43eb-a3b5-9184b5d9c2ee)로 정의됨<br>
> - 이 때 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/3d401909-672d-4f35-a85e-4431f587eada)는 Bernoulli distribution이고 F(x)를 parameter로 가짐, 즉 P(X=1)=F(x), P(x=0)=1-F(x)<br>
> - ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/6336c7e7-6dc5-42cf-8933-33f31bf8a351)은 Bernoulli distribution을 n번 시행한 것과 같으므로 결국 binomial distribution이며, ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/d65da1ea-51f1-4cf7-ad23-393e8ea6810b)는 표본평균에 해당하므로 unbiased estimator가 됨<br>
> - n개의 time segments에 frequency amplitude들을 대해 평균낸 것이 ECDF(?)<br>
> - 다양한 운행 조건 및 SNR 각각에서 얻은 frequency amplitude를 오름차순 혹은 내림차순 정렬하게 되면 여러 운행 조건/SNR에서 얻은 분포가 기존 CDF에 비해 유사하며, 이 ECDF를 가지고 distribution discrepancy를 측정하는 metric을 활용해서 진단 및 분류함<br>

> [4] Distance calculation
> - Training ECDFs의 outcomes ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/42c75dfe-b655-43a1-895a-b45c0ff945aa)와 testing ECDFs의 outcomes D에 대해 두 ECDFs의 dissimilarity에 대한 측정은 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/aa7e6100-6c75-403c-9482-067befe8321a)로 계산하며, 이 때 distance는 approximate Bayesian computation (ABC) theory 기반임<br>

<br>

#### **2-1. Statistical spectral analysis**<br>

- Metrics이 만족해야 할 3가지 (in)equalities<br>
> [1] d(x,y) = 0 iff x = y (the identity axiom)<br>
> [2] d(x,y) = d(y,x) (the symmetry axiom)<br>
> [3] d(x,y) <= d(x,z) + d(z,y) (the triangle inequality)<br>

<br>

#### **2-2. Symmetric Kullback-Leibler Divergence**<br>
- 먼저 Kullback-Leibler Divergence ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/973ca2a8-94ea-46da-bc01-c12dab2587f7)
는 cross-entropy H(p,q)로부터 유도됨(H(p)는 entropy)
<p align = "center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/2e6082c6-e914-402d-8bd9-ee107858da15">
</p>
- 즉, Cross-entropy H(p,q)는 p의 엔트로피 H(p)와 그 차이로 decompose 될 수 있고, 그 차이를 확률 밀도 함수 p와 q의 차이인 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/f06e1f08-b3c4-4458-95d3-1f303dad11db)
로 정의함

<br>

- Symmetric KLD는 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/c9d3580e-bdba-4e15-a199-ed51fde920ee)
+![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/5d77b827-07b2-49f6-b1f6-eb8691023177)
로 정의되며, 수식은 아래와 같음

<p align = "center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/eb45590e-66e3-4279-bf39-325c3f9919d1">
</p>

<br>

#### **2-3. Hellinger distance**<br>
- Hellinger distance는 두 분포가 Gaussian distribution을 따를 때 유사도를 측정하는 방법으로 아래와 같이 정의됨<br>

<p align = "center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/d58f8758-9f72-456e-9bfc-d731701b07d2">
</p>

<br>

#### **2-4. Kolomogorov distance**<br>

<p align = "center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/cd479944-21a8-4f7e-8939-6a580e575c0b">
</p>

