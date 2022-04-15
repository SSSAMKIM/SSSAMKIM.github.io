---
layout: post
title: "Meta/Few-shot Learning 기본 개념 정리"
summary: "메타러닝 및 퓨샷러닝 관련 개념 정리"
author: taehun
date: '2022-03-17 23:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: Meta-learning, Few-shot learning, Learn to learn
permalink: /12
mathjax: true
use_math: true
---

> `메타러닝 기본 개념 정리`

#### Index
---

- [1. Concept](#1-concept)
- [2. Dataset](#2-dataset)


#### **1. Concept**
  
<br>

**Meta-learning의 목적은 fast adaptation이 가능한,** 즉, 어떤 클래스 조합의 데이터가 들어오더라도 빠르게 수렴하는 모델의 **initial parameter ϕ를 찾아내는 것.**<br>
Few-shot learning과 결합하여, 적은 양의 데이터로 빠르게 수렴하는 모델(정확하게는 Feature extractor)의 paramter를 찾는 것이 목적

- **메타러닝은 크게 outer-level과 inner-level**로 나뉜다. 의미적으로 보면,
  - **inner-level은 큰 범주(ex. 자동차 종류 구분)에서 일반적인 지식을 습득하는 과정**(feature extractor의 initial parameter에 해당)<br>
  - **Outer-level은 작은 범주에서(ex. 5가지 자동차에 대한 분류) 특정 지식을 습득하는 과정**(feature extractor의 updated된 parameter에 해당)<br><br>

- 각각의 역할을 조금 더 자세히 정리하면,
  - **Inner-level**
    - learning strategy 학습. **Feature extractor의 initial parameter ϕ를 구하는 과정**
    - 학습에 참여하지 않은 validation dataset을 활용하여 meta loss를 구하고, 이를 통해 initial parameter ϕ를 구함
      (prototypcal network의 경우 prototype을 만들지 않는 query set이 initial parameter ϕ를 만들어내는 데 사용됨)
    - 이 때 initial parameter ϕ는 큰 범주의 feature를 추출하는 것이 목적<br><br>

  - **Outer-level**
    - **task-wise parameter** 학습. 예를 들어 분류 문제의 경우, 주어진 데이터셋의 class 수에 맞게 분류가 가능하도록 feature를 추출하는 과정
    - **Inner-level에서 계산된 initial parameter ϕ에서 시작**해서, **parameter update를 통해 현재 수행하고자 하는 문제의 parameter θ를 찾아냄**
      (prototypical network의 경우 support set이 prototype을 만들고, 모델 성능 계산에 사용되며, task-wise parameter를 구하는 데 사용됨)<br><br>
      
  - 따라서, 메타러닝 자체의 목적은 Inner-level에서 구한 initial parameter(=meta knowledge, meta parameter)이며, 큰 범주의 지식인 initial parameter를 활용해서 작은 범주의 다양한 문제에 적용했을 때 fast adaptation을 달성할 수 있게 된다.<br><br>


#### **2. Dataset**

<br>
