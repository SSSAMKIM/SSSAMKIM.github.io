---
layout: post
title: "Invariance와 equivariance 정리"
summary: "Invariance와 equivariance 정리"
author: taehun
date: '2023-10-31 17:30:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: Python
permalink: /22
mathjax: true
use_math: true
---

Last update: 2023.10.31<br>

> Invariance와 equivariance 정리<br>

#### Index
---

- [1. Operator](#1-operator)<br><br>

#### **1. Invariance and equivariance**
  
<br>

![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/bbc02a77-ae17-48ee-9023-702dc1eb3ca6)

**요약**<br>
Invariance: 입력 변수 x에 rotation, translation (g(ㆍ))의 변형을 하더라도 변형 전과 결과가 동일 <br>
Equivariance: 입력 변수 x에 rotation, translation과 같은 g(ㆍ)의 변형을 한 후 f(ㆍ)를 적용한 결과와 f(ㆍ) 적용 후 g(ㆍ)의 변형을 한 결과가 동일 <br>

![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/18321569-e079-4d0f-a979-5ece50b15db8)
**Invariance**: y<sub>g</sub>와 x<sub>f</sub>가 동일한 공간에 있어야 함, 출력(f(x))의 경우 가정이나 제약이 없음<br>
![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/8cefd2c0-35c1-47fc-902c-f98c1d82b232)


![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/d1f75362-f66a-4361-bc86-2016cd111229)
**Equivariance**: equivariance가 성립하기 위해 f의 input과 g의 output이 같은 공간, g의 input과 f의 output이 같은 공간에 있어야 함. 엄밀하게는 동일한 것이 아니라 g의 output이 x input의 부분집합이 될 수 있음<br>
![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/560518bc-f57f-425b-903b-e24936782715)
