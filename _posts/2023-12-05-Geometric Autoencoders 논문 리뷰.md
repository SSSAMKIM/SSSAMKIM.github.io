---
layout: post
title: "Geometric Autoencoders 논문 리뷰"
summary: "Geometric Autoencoders 논문 리뷰"
author: taehun
date: '2023-12-05 12:00:00 +0900'
category: Literature_review
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: Python
permalink: /23
mathjax: true
use_math: true
---

Last update: 2023.12.05<br>

> `Geometric Autoencoders - What You See is What You Decode 리뷰'<br>
> > 2023 ICML Conference

<br>

#### Index
---

- [1. Terminology](#1-terminology)
- [2. Summary](#2-summary)<br><br>

#### **1. Terminology**
  
<br>

**1) 전사함수(surjection)**
- ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/54f77377-725f-421f-84c6-2d271ff8075e) 에서 f(x) (치역, range)와 Y (공역, codomain)가 일치할 때 f는 전사함수라 함<br>

**2) 단사함수(injection)**
- ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/54f77377-725f-421f-84c6-2d271ff8075e) 에서 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/427b2c2e-02db-4833-86d2-519e2baacc86) 에 대해,
![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/bc78d3c8-9b4d-4495-b7b6-1079218e7a6e), 즉 일대일 함수인 경우 단사함수라 함<br>

**3) Chart**
- ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/a46a482d-5a6c-4a41-ac50-6136efab3157) domain U에서 range V로 가는 각각의 mapping을 chart라 함<br>
- 혹은, smooth manifold에 대해, 어떤 open sets U가 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/2c55be0b-7e1d-4d90-ba1e-afb84a747c89)의 부분공간에 대해 위상동형이고, open sets U에 의해 덮을 수 있을 때 덮어서 대응되는 각 mapping이 chart<br>

**4) Differential of f at p**
- Manifold ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/1f778db5-627b-4064-b1a4-42aacf4b3808)를 만족하는 함수 f에 대해
![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/bdf40a78-d8c0-48d7-aecc-dd56dd883bb9)를 manifold M 위의 점 p에서 함수 f의 differential이라 정의하며, 이 때 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/56fb0f11-974e-46e5-be59-f6bb9a4d2528)은 manifold M 위의 점 p에서의 tangent space를 의미한다.<br>

**5) 위상동형(Homeomorphism)** 
- 함수가 전사, 단사이며 모든 점에서 연속 역함수도 전사, 단사, 연속인 경우를 의미<br>

**6) 미분동형(Diffeomorphism)**
- 함수가 homeomorphism이며 미분 가능하고, 역함수에 대해서도 미분가능한 경우를 의미<br>

**7) Immersion**
- from small space to big space<br>

#### **2. Summary**

<br>

- Visualization을 위한 low-dimensional autoencoders에서 latent representation에서 distortion이 발생해도 낮은 reconstruction loss를 가지는 문제를 해결하고자 함<br>
  1) **Generalized Jacobian determinant를 활용하여 local expansion, contraction을 측정**하는 것을 제안<br>
  2) **Generalized Jacobian dterminant의 log variance를 regularizer로 활용**하여 이 값을 최소화함으로써 local expansion 및 contraction이 없는 즉, **distortion이 발생하지 않도록** 규제<br>
  3) Generalized Jacobian determinant는 undirected contraction만 측정하기에, indicatrices를 활용하여 latent space 위 각 점의 anisotropy를 시각화 함<br>

<p align="center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/8c696d4a-80a4-4582-9427-60c48518e8a5" width = "800" height = "auto">
</p>

- 위 figure에서 세계 지도에 대한 embeddings을 확인하면 Geometric AE가 정성적인 관점에서 더 우수한 성능을 보이나, Vanilla AE의 reconstruction loss가 Geometric AE의 절반만큼 낮음(Vanilla AE는 locally stretching or contracting하기 때문)<br>

- Decoder가 하는 일은 latent space에 있는 surface를 output space로 fitting 하는 것인데 이 때 임의의 방향으로 stretching 하게 됨<br>
  -> 이 때 excessive stretching은 latent space에 불필요한 distortion을 가져 오게 됨<br>

**Generalized Jacobian determinant**



