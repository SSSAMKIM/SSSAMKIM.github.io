---
layout: post
title: "Discriminant Feature Extraction for Centrifugal Pump Fault Diagnosis 리뷰"
summary: "Pump 고장 진단을 위한 feature extraction"
author: taehun
date: '2022-04-20 11:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: Feature extraction, pump system, fault diagnosis, PHM
permalink: /15
mathjax: true
use_math: true
---

Last update: 2022.04.22<br>

> `IEEE Access Discriminant Feature Extraction for Centrifugal Pump Fault Diagnosis 논문 리뷰`

#### Index
---

- [1. Introduction](#1-introduction)
- [2. Technical background](#2-technical-background)<br><br>

- **Research gap**
  - Raw statistical feature는 약한 초기 고장(incipient fault)이나, 훨씬 심각한 고장에 사용하기에는 부적절하다.<br><br>

- **Brief explanation for the proposed method**
  - 1. 정상 진동 신호가 선정됨
  - 2. 정상 진동 신호와 다른 고장 클래스의 신호 간에 cross-correlation 계산
  - 3. 시간, 주파수, 시간-주파수 영역에서 raw hybrid features 추출
  - 4. Raw hybrid feature 간에 correlation coefficient를 조사하여 새로운 feature set을 만들고, 이 feature set들을 single feature vector로 합침<br><br>
  
  - 한 줄 정리: Two-types of correlation function utilized<br>
    (1) cross-correlation을 활용해 두 신호간 유사성 계산하여 feature , (2) feature 변수들 간에 correlation coefficient 계산으로 추가 전처리 <br><br>

#### **1. Introduction**
  
<br>

- **Terminology**
  - Mechanical seal: 회전기기에서 유체(윤활유)의 누설을 방지하는 부품으로, 회전자(shaft)와 고정자(pump body) 사이에 위치<br>
    - 유체 누설 방지를 위해 sealing은 정적인 기계 시스템의 경우 큰 압력으로 밀봉하면 되지만, 동적인 회전자의 경우 큰 압력만으로 유체 밀봉은 불가능하다.<br>
    - 회전자와 고정자 사이에 발생하는 마찰을 없애고, 대신 회전자와 mechanical seal 사이 마찰이 발생한다.<br><br>

- **Summary of introduction**
  - Centrifugal pump에서의 고장은 mechanical fault(MF)와 fluid flow related hydraulic fault(FHF)로 나뉜다.<br>
  - 펌프 고장의 39%는 mechanical seal faults 때문이며, 또다른 연구에서는 impeller imbalance가 MF, FHF를 발생시킨다고 설명한다.<br>
    - 본 논문에서는 mechanical seal과 impeller fault를 포함하는 MF를 다룬다.<br>
  - 진동 신호에서 이상 신호의 진폭이 작을 경우, 배경 소음에 묻힐 수 있음<br>
    - Time domain<br>
      - 이상 상태로 인한 impulse, shock이 결국 진동 신호의 진폭이나 분포의 변화에 영향을 끼침<br>
      - Cons: 시간 영역의 feature는 고장의 severity 변화에 sensitive 하지 않다는 단점으로, 분별력 있는 feature를 얻기 힘들다.<br>
        - (impulse, shock이 크면 시간 영역에서도 magnitude 변화에 크게 반응하는 것 아닌지?)<br>
    - Frequency domain<br>
      - Pros: 시간 영역에서 탐지되지 않는 작은 변화가 spectrum line으로 나타나기에 고장에 더욱 민감함<br>
      - Cons: 시스템의 작동 조건이 가변적인 경우(non-stationary)에 적용이 불가함<br>
    - Wavelet Transform(WT)<br>
      - Pros: 시간에 따라 변하는 non-stationary 신호에 대해서도 feature 추출 가능<br>
      - Cons: non-stationary 진동 신호에 대한 최적의 wavelet function을 찾는 것이 문제이며, 많은 실험과 주관적인 판단도 포함됨<br>
    - Empirical Mode Decomposition(EMD)<br>
      - Pros: self-adaptive signal decomposition이 가능하므로, Wavelet Transform의 단점을 극복 가능<br>
      - Cons: mode-mixing을 가지는 신호가 있는 경우 non-orthogonal한 요소들로 분해가 됨<br>
        - Mode-mixing은 intermittency signal로 인해 발생하는데, 1) EMD 과정에서 발생하거나, 2) noise 또한 intermittency signal로 간주 되어 발생<br><br>


#### **2. Technical background**



<br>
