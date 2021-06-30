---
layout: post
title: "GAN기반 이상 탐지 논문 리뷰"
summary: "GAN기반 이상 탐지 논문 Review"
author: taehun
date: '2021-05-24 12:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: GAN, Anoamly Detection, Class Imbalance, AutoEncoder
permalink: /8
mathjax: true
use_math: true
---

> `A GAN-Based Anomaly Detection Approach for Imbalanced Industrial Time Series
` 논문 리뷰

#### Index
---

- [Anomaly Detection](#anomaly-detection)
- [Class Imbalance Problem](#class-imbalance-problem)
- [Dataset](#dataset)
- [Model Architecture and Training](#model-architecture-and-training)
- [Evaluation Metrics](#evaluation-metrics)
- [Reference](#reference) <br><br>

#### Anomaly Detection
---

  - 이상 탐지는 Time-series(시계열) 데이터를 입력을 받으며, **모델 학습 과정은 보통 1) feature extraction, 2) fault recognition 2단계**로 나뉜다.

  - 이상 탐지를 위한 패턴 인식 도구로, **Bayesian classifier, Support Vector Machine, Neural Networks, 그리고 DL methods**가 사용된다.

  - 하지만 **이 모델들은 class-balanced hypothesis 하에서 도입되었다.**

  - 따라서, 이상 탐지 알고리즘은 아래와 같이 몇가지 문제점을 가지게 된다.

  > 1) **Class Imbalanced Problem** : ML/DL 학습 알고리즘은 class-balanced 가정 하에 도입되었기에, 클래스 불균형 데이터로 학습하는 것은 문제를 일으킬  있다.<br><br>
  > 
  > 2) **Insufficient Labeled Data** : 클래스 불균형 이외에, 이상 탐지를 위해서 정상/고장 상태에 대한 라벨링이 된 데이터가 필요한데, 라벨링 된 데이터 또한 부족하다.<br><br>
  > 
  > 3) **Ambiguity of Starting Time of Abnormality** : 어느 시점부터 고장으로 지칭할 것인지에 대해 라벨링 이슈가 있기에, 고장을 판단하는 Threshold 설정에 대한 모호함으로 mis-labeled 문제가 있을 수 있다.

<br>

#### Class Imbalance Problem
---

  - 실제 산업 현장에서 얻을 수 있는 데이터는 normal states의 데이터에 비해 fault states의 데이터가 현저하게 부족함.

  - SVM, CNN과 같은 알고리즘의 경우 majority class에 편중하는 경향이 있기에 즉, 정상 상태 데이터쪽으로 편향(bias)을 가질 것이기에, 클래스 불균형 문제는 Classification task에서 진단 성능에 악영향을 끼치게 된다.

  - 기존에 클래스 불균형 문제에 접근하는 Two key methods는 보통 아래와 같다.

  > 1) **Data-level methods** : 불균형 데이터 분포를 해소하기 위해 under-sampling or over-sampling을 사용하는 방법.<br><br>
  > 2) **Algorithm-level methods** : Bagging, Boosting ensemble-based methods 등을 이용하여 classifier를 불균형 데이터에 맞게 fitting 시키도록 변형하는 방법.

<br>

#### Dataset
---

  - 1) **CWRU Rolling Bearing Dataset**

  - 2) **Testbed Dataset of Rolling Bearing of the author's laboratory**

  - **Training/Test Dataset**

    - Time-series dataset D = [X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>n</sub>] ∈ R<sup>t×n</sup>, X<sub>i</sub> = [x<sub>1i</sub>, x<sub>2i</sub>, ..., x<sub>ti</sub>]<sup>T</sup> ∈ R<sup>t</sup> (for i = 1, ..., n)

    - **Training Dataset**

      - Normal dataset만 사용하여 Generator/Discriminator 학습

      - D<sub>train</sub> ∈ R<sup>t×b</sup> with only normal samples, 이 때 b는 학스 데이터의 개수를 의미한다.

    - **Test Dataset**

      - Normal/Fault dataset 모두 사용하여 학습된 Discriminator가 Normal/Fault 판단

      - D<sub>test</sub> = [D<em><sub>test</sub><sup>v</sup></em>, D<sub>test</sub><sup>u</sup>] ∈ R<sup>t×(v+u)</sup>, 이 때 v, u는 각각 normal, abnormal sample들의 개수를 의미한다. (n = b + v + u)

      - Imbalanced time series data이므로, b+v >> u이 상황으로 설정한다.

<br>

#### Model Architecture and Training
---

**1. Model Architecture**

  - 모델은 Feature extractor, Generator, Discriminator 3단계로 이루어진다.

  - **Feature Extractor** : 데이터가 Generator로 들어가기 전에, 학습 시간 감소를 위해 class간 구별이 쉬운 feature들을 추출한다.

    - 이 과정에서 D<sub>train</sub>은 q개의 feature를 가지는 feature matrix F로 size를 감소시킨다.

  - **Generator** : DCGAN 기반 하에서 Encoder(G<sub>e</sub>)-Decoder(G<sub>d</sub>)-Encoder(![Ghat](https://latex.codecogs.com/svg.latex?\small&space;\hat{G}))의 Three-sub-network로 이루어진다.

    - 학습 시간 및 진단 성능을 향상시키기 위해, feature extractor가 원본 데이터와 GAN 사이에 삽입된다.

    > **![Ge](https://latex.codecogs.com/svg.latex?\small&space;Z=G_e(F),Z$$\in$$R^{h\times{b}})**

    (G<sub>e</sub> downscales F into latent representation Z)

    > **![Gd](https://latex.codecogs.com/svg.latex?\small&space;\hat{F}=G_d(Z))**
    
    (G<sub>d</sub> uses Z to recreate ![Gd](https://latex.codecogs.com/svg.latex?\small&space;\hat{F}))

    > **![Gehat](https://latex.codecogs.com/svg.latex?\small&space;\hat{Z}=\hat{G_e}(\hat{F}))**
    
    (![Gehat](https://latex.codecogs.com/svg.latex?\small&space;\hat{G_e}) is the same as G<sub>e</sub> but with different parametrization and the dimension of output ![Gehat](https://latex.codecogs.com/svg.latex?\small&space;\hat{Z}) is the same as Z)

<center>
  <img src="/public/img/gan_anomaly.png" style = "width : 50%; height : auto;">
</center>

<br>

**2. Training**

  - GAN-based model은 학습시 D<sub>train</sub>으로만 학습하게 되고, 이 때 **목적은 각 training dataset에 대한 모델의 output의 variance를(추가 확인 필요) 최소화하는 것**이다.

  - 학습이 끝난 후에는, 학습된 generator에 normal, fault 데이터를 포함한 D<sub>test</sub>가 입력되고 이 데이터들이 encode, decode를 거쳐 출력된다.

  - **Normal test data(D<sub>test</sub><sup>u</sup>의 출력은 training 당시 얻었던 패턴과 유사**하겠지만, 학습이 되지 않은 **abnormal test data(D<sub>test</sub><sup>v</sup>)의 출력은 편차가 아주 클 것**이다.

**3. Objective Function**

  - 1) **Fraud Loss(L<sub>f</sub>)**

    - Discriminator가 실제 데이터와 generator를 통해 만들어낸 데이터 사이에서 잘못 판단하도록 만드는 역할을 한다.<br><br>
    - Generated samples을 discriminator에 입력으로 넣고, discriminator의 출력단에서 Fraud loss를 계산한다.

    > ![Lf](https://latex.codecogs.com/svg.latex?\small&space;L_f(F)=\sum_{i=1}^N\sigma(C(\hat{F}),\alpha))
    
    - ![sig](https://latex.codecogs.com/svg.latex?\small&space;\sigma) is the binary cross-entropy loss function, ![CF](https://latex.codecogs.com/svg.latex?\small&space;C(\hat{F})) is the probability that the sample i is predicted to be real, and define ![CF](https://latex.codecogs.com/svg.latex?\small&space;\alpha=1)<br><br>
    
    - Discriminator가 generated samples를 real sample이라고 판단내리게 만들도록, ![alpha](https://latex.codecogs.com/svg.latex?\small&space;\alpha)를 1로 설정하는 것.<br><br>

  - 2) **Apparent Loss(L<sub>a</sub>)**

    - Real sample과 Generated sample 사이의 L<sub>1</sub> distance를 구하는 것.

    - Generator가 samples을 더 사실적으로 reconstruct하기 위해서, normal condition을 potential pattern을 더 잘 학습시킬 수 있도록 만든다.

    > ![La](https://latex.codecogs.com/svg.latex?\small&space;L_a(F)=\sum_{i=1}^N\lVert{F-\hat{F}}\rVert)

  - 3) **Latent Loss(L<sub>l</sub>)**

    - Real sample과 Generated sample의 Latent representation에 대한 distance를 최소화하기 위한 loss function

  - **Loss function of the generator**

    > ![Lg](https://latex.codecogs.com/svg.latex?\small&space;L_g(F)=w_f*L_f(F)+w_a*L_a(F)+w_l*L_l(F))

  - **Loss function of the discriminator**

    > ![Ld](https://latex.codecogs.com/svg.latex?\small&space;L_d(F)=\sum_{i=1}^N\lVert{L(F)-L(G_d(G_e(F)))\rVert)

**4. Test Process**

  - 테스트시, latent loss, apprent loss를 사용하며 총 anomaly score A(F)는 아래 식으로 계산된다.

    > ![La](https://latex.codecogs.com/svg.latex?\small&space;A(F)=\lambda*L_a(F)+(1-\lambda)*L_l(F),\lambda=w_a/w_l)

    
    - 모델은 Normal data에 대해서만 학습되었기에, normal latent patten을 잘 나타낼 수 있으므로, normal sample일 경우 A(F)의 값은 0에 가까워진다.

<br>

#### Evaluation Metrics
---

<br>

#### Result
---

<center>
  <img src="/public/img/anomaly_cwru.png" style = "width : 50%; height : auto;">
</center>

<br>

#### Reference
---

- WENQIAN JIANG, YANG HONG, BEITONG ZHOU, XIN HE, AND CHENG CHENG, A GAN-Based Anomaly Detection Approach for Imbalanced Industrial Time Series
, IEEE Access, vol. 7, 2019


---


