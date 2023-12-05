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
- [2. Abstract](#2-abstract)
- [3. Introduction](#3-introduction)<br><br>

#### **1. Terminology**
  
<br>

**1) 전사함수(surjection)**
- ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/54f77377-725f-421f-84c6-2d271ff8075e) 에서 f(x) (치역, range)와 Y (공역, codomain)가 일치할 때 f는 전사함수라 함<br>

**2) 단사함수(injection)**
- ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/54f77377-725f-421f-84c6-2d271ff8075e) 에서 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/427b2c2e-02db-4833-86d2-519e2baacc86) 에 대해,
![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/bc78d3c8-9b4d-4495-b7b6-1079218e7a6e), 즉 일대일 함수인 경우 단사함수라 함<br>

#### **2. Abstract**

<br>

- Visualization을 위한 low-dimensional autoencoders에서 latent representation에서 distortion이 발생해도 낮은 reconstruction loss를 가지는 문제를 해결하고자 함<br>
  1) Generalized Jacobian determinant를 활용하여 local expansion, contraction을 측정하는 것을 제안<br>
  2) Generalized Jacobian dterminant의 log variance를 regularizer로 활용하여 이 값을 최소화함으로써 local expansion 및 contraction이 없는 즉, distortion이 발생하지 않도록 규제<br>
  3) Generalized Jacobian determinant는 undirected contraction만 측정하기에, indicatrices를 활용하여 latent space 위 각 점의 anisotropy를 시각화 함<br>
 


<br>

