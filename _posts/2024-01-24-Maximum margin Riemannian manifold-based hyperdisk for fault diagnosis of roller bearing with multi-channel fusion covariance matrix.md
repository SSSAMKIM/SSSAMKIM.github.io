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
> - SPD 행렬의 행렬 로그 도메인 flat tangent-vector space에서는 Euclidean 기하학의 다양한 계산 규칙이 적용될 수 있음 
> - **SPD matrices 간 거리**를 계산하기 위해서는 **Euclidean metric을 활용하는 것이 불가, geodesic metric을 활용**해야 함<br>

<br>

1-1) AIRM
> - Riemannian manifold에서 흔히 활용되는 geodesic metric으로, ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/6694df2d-7766-49db-9e47-1e0b34637ce4)로 계산되며, ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/073ccbf2-cb5c-49b4-bf24-3a10175eeee3)는 Frobenius norm을 의미, log는 matrix logarithm operator를 의미
> - 이 때 Frobenius norm은 다음과 같다: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/8c2e6e07-5d93-4829-99f6-ee8ad88ebde0)<br>


1-2) matrix logarithm and exponential operator
> - Logarithm operator: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/ee6a7e24-1126-427a-a07b-d7c76353cc12)
> - Exponential operator: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/296a178a-3501-4fc1-9c85-3707f90a85d9), log(Z)의 inverse transofrm<br>

1-3) Loarithm product operation과 LEM-based geodesic metric
> - SPD matrices 간 logarithm product operation: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/31eaac37-6dca-4e82-b228-d1fdd76fc2c4)
> - LEM-based geodesic metric: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/869badf9-a556-487b-b6fe-ef3e8494f467)
> - LEM-based로 non-smooth Riemannian manifold에서 relatively flat tangent vector space로 mapping이 되며, 이 경우 Euclidean geometry의 여러 계산 규칙 적용할 수 있음
 <br>

<br>

2) Hyperdisk

<p align = "center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/a2fb7765-5645-4a6a-ad7c-599af53f758d">
</p>

> - Hyperdisk는 affine hull과 hypersphere의 교집합임
> - Hyperdisk는 sample region 근사에 대해 affine hull 보다는 tight하고, conve hull 보다는 loose한 근사를 제공함
> - Sample dataset ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/916ddc3e-0bc1-4413-925a-8e61318ae19a)에 대해, hyperdisk는 다음과 같이 정의됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/990176b4-7440-468b-8bce-d03f0221f56d)
> - 이 때 r은 hyperdisk의 반지름, c는 중심을 의미하며 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/1fc7ac9f-c8f1-439b-8b92-31d28df1c41c)는 각 sample ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/404e084e-b989-4148-839c-0984adc2913e)에 대한 combination coefficient임
> - c와 r은 다음 식을 통해 결정됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/4494523f-0936-4227-bf79-26961558c2b9)
> - ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/9a91d013-b892-4c8a-8ecb-d379a51c313d)는 trade-off parameter로, over-distant한 points (outliers)를 제거하는 역할을 함(아마 s.t. 이후 constraint에서 sample들 중 outlier들이 hypersphere 안으로 들어가기 위해 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/f9a3acf5-92e5-4cee-ad9a-bbae66442ad6) 값을 키우는데, minimizaiton 관점에서 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/ffb87a6f-9436-48ab-a3d7-d0cb62019c5b)
의 영향을 낮추기 위해 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/1cd9a271-0470-47ec-a922-9476e1bd6de1) 값을 줄이는 방식으로 outlier의 영향을 줄이려는 것 같음
> - Hyperdisk를 기반으로 MMHD classifier는 postiive sample dataset ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/22899298-cb44-4bcf-ac54-bc61fa03ff85)
와 negative sample dataset ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/e8302169-2182-4350-80dc-0eea214b4160)
에 대해 MMHD의 objective function은 다음과 같이 작성됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/19515bd9-614f-4c62-a737-b3b7d0ba30c7)<br>

<br>

**4. Proposed method**

<br>

1) Multi-channel fusion covariance matrix (MFCM)
> - 아래 table과 같이 Time-domain features 14개, frequency-domain features 8개를 활용함
> - m개의 channel vibration에 대해 구성한 feature matrix는 다음과 같이 정의됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/8896cf38-cbd6-4733-92d5-7a66fe8a32d8)
> - 이 때, 각 column은 동일한 feature를 나타내며, feature matrix로부터 MFCM Z는 다음과 같이 계산됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/32f47345-86df-4298-b838-a6800c97f0e2)<br>

<br>

![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/90ca7d08-24ca-4c30-8710-6a0d690e5ce0)
![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/8c754e68-94a6-4448-a329-adeaaaeb8107)

2) MMRMHD

> - MFCM Z 행렬을 바탕으로 Riemannian manifold-based hyperdisk (RMHD)는 다음과 같이 정의됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/96bf0d63-3ed2-4e03-b006-adf881d05a1a)
> - Euclidean space에서 hyperdisk를 정의하는 것과 유사하지만, summation이나 product operations를 Riemannian space에서 scaling 하는 것이 다름
> - 따라서, 위 RMHD를 단순화하기 위해 SPD 행렬을 matrix logarithm domain으로 사상하게 되며, matrix logarithm domain에서는 Euclidean에서의 계산 규칙과 유사함
> - 단순화된 RMHD는 다음과 같이 정의됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/34d9e784-812a-4a5f-8107-3c8c6f6f5a86)
> - log(C)와 r은 다음과 같이 계산됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/81cc7822-e491-4bde-9646-23e5c6520246)
> - 위 식을 계산하기 위해 Lagrange multipllier ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/04dfdcb7-433f-4e43-ac5f-2a54ef9c0628)와 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/e3c3a010-21e3-4df2-80a1-ade538b79df6)를 활용하여 Largrangian function을 구성: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/254855ee-891a-4107-a33c-d4e886d7e385)
> - Lagrangian function의 derivative: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/13852163-7dd6-4e7c-8dae-d2e8392c1a00)
> - Minimization 과정은 다음과 같이 대체됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/0d4fd917-87f4-461f-b0c7-fcb15f00ad8a)
> - MMRMHD의 objective function은 다음과 같이 정의됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/f08d7679-9b25-4b0b-a0cd-301499d9276b)<br>

<br>

> - 최적의 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/304dee6b-0cca-4803-92a5-6517031b1d4e)와 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/0f57ea06-101b-4a66-a2e4-3c6471917fe0)를 찾으면, 분류를 위한 hyperplane의 weight matrix W와 bias b는 다음과 같이 계산됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/4edc8b5f-25fe-4cd5-be90-3d874c52fc20)
> - 최종적으로 testing SPD matrix sample Z에 대한 MMRMHD의 decision function은 다음과 같음: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/053ddc52-65a2-45c0-a1f8-afd32313ecac)<br>

<br>

3) MMRMKHD
> - MFCMs이 Riemannian manifold space에서 linearly separable 하다면 MMRMHD로 분류가 가능하나, 비선형성이 존재하는 경우 필요함
> - Riemannian manifold-based kernel hyperdisk (RMKHD)는 mapping function ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/f4b49131-f1e7-457e-aba6-f4bf468f280c)를 활용하여 다음과 같이 정의됨: ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/8dea3fa1-0e91-4a46-bf62-17659fec4520)
> - RMKHD는 mapping function이 MFCM을 고차원의 힐버트 공간으로 직접적으로 사상함
> - Euclidean space에서 kernel functions은 MFCM에 바로 적용이 불가하나, log-E polynomial kernel, log-E exponential kernel, log-E Gaussian kernel과 같이 LEM을 활용한 Riemannian kernel function을 활용하게 되면 적용 가능함<br>

<br>

- 번외: MFCM이 아닌 기존 feature fusion 방식은 local linear embedding (LLE), locality preserving projections (LPP), 그리고 mRMR이 있음<br>
