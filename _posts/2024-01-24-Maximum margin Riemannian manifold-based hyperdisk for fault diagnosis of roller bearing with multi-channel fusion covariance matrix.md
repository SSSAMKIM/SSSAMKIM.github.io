---
layout: post
title: "Maximum margin Riemannian manifold-based hyperdisk for fault diagnosis of roller bearing with multi-channel fusion covariance matrix 리뷰"
summary: "Riemannian manifold-based 고장 진단 논문 리뷰"
author: taehun
date: '2024-01-24 09:50:00 +0900'
category: Review
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
- [3. Background theory](#3-background-theory)
- [4. Proposed method](#4-proposed-method)<br><br>

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

<br>

2) Hyperdisk

<p align = "center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/a2fb7765-5645-4a6a-ad7c-599af53f758d">
</p>

> - Hyperdisk는 affine hull과 hypersphere의 교집합임
> - Hyperdisk는 sample region 근사에 대해 affine hull 보다는 tight하고, conve hull 보다는 loose한 근사를 제공함
> - Sample dataset ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/8dcb3881-f724-43b5-a3b6-96f23c317bb3)에 대해, hyperdisk는 다음과 같이 정의됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/30e60a12-f3f3-4bb9-96e9-65256e6a5fa5)
> - 이 때 r은 hyperdisk의 반지름, c는 중심을 의미하며 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/43ed32dc-f101-45b9-ac5b-0654f7c99293)는 각 sample ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/c5f6c472-ec60-4fc6-a22a-257eaaea3b34)에 대한 combination coefficient임
> - c와 r은 다음 식을 통해 결정됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/c8b97a14-a8d1-4000-ae16-c4bda82b99d2)
> - ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/5dc7b486-f67f-4112-8b51-d51f81afbaf8)
는 trade-off parameter로, over-distant한 points (outliers)를 제거하는 역할을 함(아마 s.t. 이후 constraint에서 sample들이 hypersphere 안으로 들어가기 위해 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/74983bcc-0c65-4153-84fb-f0bf541e83dd) 값을 키우는데, minimizaiton 관점에서 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/75cbb607-fc40-4587-bed3-86d9e94b282f)의 영향을 낮추기 위해 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/e386bddb-1387-43d5-8d08-f801fb5e13ff) 값을 줄이는 방식으로 outlier의 영향을 줄이려는 것 같음
> - Hyperdisk를 기반으로 MMHD classifier는 postiive sample dataset ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/f3cc9256-2e0f-4778-b5b8-013ff1d25032)와 negative sample dataset ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/bc393b9e-7743-49ef-ab8e-6fb652c12480)에 대해 MMHD의 objective function은 다음과 같이 작성됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/19515bd9-614f-4c62-a737-b3b7d0ba30c7)<br>

<br>

**4. Proposed method**

<br>

1) Multi-channel fusion covariance matrix (MFCM)
ddd
