---
layout: post
title: "Maximum margin Riemannian manifold-based hyperdisk for fault diagnosis of roller bearing with multi-channel fusion covariance matrix 리뷰"
summary: "Riemannian manifold-based 고장 진단 논문 리뷰"
author: taehun
date: '2024-01-24 09:50:00 +0900'
category: Literature_review
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null  
keywords: Python
permalink: /27
mathjax: true
use_math: true
---

Last update: 2024.01.24<br>

> `Maximum margin Riemannian manifold-based hyperdisk for fault diagnosis of roller bearing with multi-channel fusion covariance matrix 리뷰'
> > Advanced Engineering Informatics (IF: 8.8, rank: 96.1%, 2024.01.24 기준)<br>

<br>

#### Index
---

- [1. Abstract](#1-abstract)
- [2. Introduction](#2-introduciton)
- [3. Background theory](#3-background-theory)<br><br>

#### **1. Abstract**

<br>

> Sensor 위치에 따라 진동 신호의 시간 영역 표현이 달라지기에, single-channel data보다는 채널 간 관계성을 분석할 수 있는 multi-channel data를 활용함<br>

<br>

- **Proposed method 요약**

1) Multi-channel fusion covariance matrix (MFCM)

> - Multi-channel data로부터 22개(14개의 시간 영역, 8개의 주파수 영역 features)의 통계적 features를 기반으로 구성되며, MFCM의 각 element는 채널 간 correlation information을 나타냄
> - MFCM이 symmetric positive definite (SPD) 행렬이고, 이는 Riemannian manifold에 속함<br>

<br>

2) Riemannian manifold-based hyperdisk (MMRMHD)

> - MFCM이 Riemannian manifold에 속하므로 Riemannian metric을 정의해야 하며, 보통 2가지가 사용됨
> - [1] Affine-invariant Riemannian metric (AIRM), [2] Log-Euclidean metric (LEM)
> - **AIRM의 경우 eigenvalue decomposition을 진행하며, Riemannian manifold의 curvature 때문에 computationally expensive한 문제점**이 있음
> - 반면에 **LEM은 non-flat Riemannian manifold를 상대적으로 flat tangent-vector space로 확장**함으로써 연산량을 줄여줌(Riemannian manifold로 근사)
> - 결론적으로, **LEM-based kernel function으로 MFCM을 고차원의 Hilbert space로 사상**하고, (kernelized) MMRMHD를 classifier로 사용<br>

<br>

#### **2. Introduction**

<br>

- Manifold learning은 고차원 데이터를, 원 데이터에 embedded 된 내재적 특성을 보존하는 저차원 특성 공간에 사상할 수 있음<br>

- Manifold learning 기반 방식의 이점
> - 데이터의 국부적 정보가 유지됨
> - 복잡한 데이터에 embedded된 nonlinear freedom degrees가 발견될 수 있음<br>

- 기존 feature-level fusion 방법 기반의 manifold learning 연구는 multi-channel features를 하나의 log vector로 변환하기에, 채널 간 상관관계를 학습하지는 못함<br>

- MMRMHD의 목적
> - Riemannian manifold 공간 상에서 다른 MFCMs을 maximum margin을 가지면서 분류할 수 있는 hyperplane을 찾는 것<br>

<br>

#### **3. Background theory**<br>

1) Riemannian manifold
> - **SPD matrix는 Euclidean이 아닌 non-smooth Riemannian manifold에 위치**함
> - SPD에 의해 구성된 Riemannian manifold는 **locally smooth linear structure**를 가지며, 따라서 Euclidean space의 기하학적 특성을 만족하지 않음
> - **SPD matrices 간 거리**를 계산하기 위해서는 **Euclidean metric을 활용하는 것이 불가, geodesic metric을 활용**해야 함<br>

<br>

1-1) AIRM
> - Riemannian manifold에서 흔히 활용되는 geodesic metric으로, ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/e5bc1387-b5c3-4b2c-a799-760f96d40719)로 계산되며, ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/b822ec94-41e1-496c-bfbf-678fdb9e9e35)는 Frobenius norm을 의미, log는 matrix logarithm operator를 의미
> - 이 때 Frobenius norm은 다음과 같다: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/51cf39d2-35d5-4716-b8f3-aeecf8d2fe31)<br>


1-2) matrix logarithm and exponential operator
> - Logarithm operator: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/d71f7e8b-47a6-4dd5-a973-36d73d37c5cb)
> - Exponential operator: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/810a10dd-3a10-4fd0-9b85-3ae53810c5c7), log(Z)의 inverse transofrm<br>

1-3) Loarithm product operation과 LEM-based geodesic metric
> - SPD matrices 간 logarithm product operation: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/41e1fe3a-add5-45ba-a83b-c08af55c3d9e)
> - LEM-based geodesic metric: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/e889c20d-4aca-4b64-b264-5aa10af2ab17)
> - LEM-based로 non-smooth Riemannian manifold에서 relatively flat tangent vector space로 mapping이 되며, 이 경우 Euclidean geometry의 여러 계산 규칙 적용할 수 있음
 <br>



2) Hyperdisk

<p align = "center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/a2fb7765-5645-4a6a-ad7c-599af53f758d">
</p>




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

