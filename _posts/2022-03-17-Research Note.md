---
layout: post
title: "연구 노트 - Signal generation, Latent space analysis of GAN"
summary: "신호 생성 및 분석 관련 연구 노트"
author: taehun
date: '2022-03-17 23:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: GAN, PHM, Latent space analysis, Signal Generation, Digital twin, DeepLearning
permalink: /11
mathjax: true
use_math: true
---
Last update: 2022.04.21<br>
> `신호 생성 및 분석 관련 연구 노트`

#### Index
---

- [1. Motivation](#1-motivation)
- [2. Idea](#2-idea)


#### **1. Motivation**
  
<br>

- Digital Twin의 용도 중 하나는 현실에서 발생할 수 있는 다양한 케이스를 시뮬레이션 하기 위함으로, 부족한 데이터를 활용하기보다는 생성을 통해 다양한 모델을 실험해볼 수 있음<br>
- 실제 산업에서는 완전한 고장 데이터는 거의 존재하지 않고, 서서히 고장으로 가는 것을 detection 하여 방지하는 것이 중요.
  - 테스트베드에서는 해당 데이터를 얻기 힘드므로, 정상 & 고장 데이터를 통해 고장의 level에 따른 데이터 생성할 수 있다면 현장 적용이 용이하지 않을지?<br>


#### **2. Idea**

<br>

**신호 생성 관련**<br><br>
- Feature generation 관련
  - Fault diagnosis model에서 어떤 feature가 유의미한지 확인 후 신호 생성보다는 feature를 생성하는 것이 더 나을지?<br><br>
- Quantitative metric 관련
  - Time domain에서는 차이가 커지도록, frequency domain에서는 차이가 작아지도록 adversarial하게 학습하는 방법? (loss는 미분가능한 함수로 선택)
  - Multivariate에서는 제곱의 평균 = 평균의 제곱 + 공분산인데, 공분산이 커질 경우 제곱의 평균 즉, L2 norm도 커지므로 high dimensional feature space에서 둘 간 거리도 멀어질 것이고, 이를 통해 uncertainty나 similarity를 측정할 수 있을지도.
  - 이미지의 diversity의 경우에는 Learned Perceptual Image Patch Similarity (LPIPS)를 이용하여 측정함
  - 신호처리를 가미한 positional encoding 방식 찾아보기<br><br>
- Compound fault 관련
  - KAMP data에서 looseness & unbalance 이용하여 compound fault<br><br>
- Semi-supervised 관련
  - 생성된 신호중 quality가 떨어지는 것들을 활용한 semi-supervised learning으로 feature를 학습한 다음 knowledge transfer으로 부족한 데이터들에 대한 classification 진행<br><br>
- 작동 조건 다른 신호 생성 관련
  - RPM이 다른 신호를 생성하기 위해 discriminator가 하나 또는 두 파장의 신호만 보고 real/fake 판별<br>
    - 하나 또는 두 파장의 신호만 보고 판별하면 고장 특성만 볼 것이라 추측할 수 있고, generator는 들어온 신호가 어떤 속도 조건으로 움직이냐와 무관하게 다양한 파장을 가지는 신호를 생성할 수 있지 않을까?<br><br>
- 신호 생성을 위한 추가 loss term 관련
  - torch.fft를 loss에 추가<br><br>
- Sequential model에 대한 네트워크 변경
  - TCN, LSTM, GRU 시도<br><br>

**신호 생성 이외 연구 관련**<br><br>
- Data Imputation 관련
  - GNN을 활용한 결측치 or meta-learning<br><br>

- Domain Shift 관련
  - 다른 도메인의 데이터들이 각각의 Encoder로 들어가서 각각의 latent들을 crossentropy로 맞춰주면 결국 domain에 관계없는 feature를 뽑을 수 있을지?<br><br>

- Question
  - Raw signal을 딥러닝 모델에 넣어서 얻을 수 있는 feature와 feature extraction을 거쳐서 딥러닝에 넣는 것의 차이?<br>
    - 딥러닝 모델을 통해서도 manual feature extraction 과정에서 얻을 수 있는 feature를 얻을 수는 있으나, 아마 특정 방향으로 학습이 되기에 manual feature extraction을 통해 얻은 feature는 포함될 수도 있고, 안될 수도 있을 듯?<br><br>

- Feedback
  - 2022 PHM Society의 경우, AutoEncoder를 학스 후 Encoder를 이용하여 classification 하느 것보다, Decoder 없이 Encoder와 Classifier를 동시에 학습하는 것이 학습하지 않은 individual의 data들도 잘 맞힘
  - 이를 통해 단순히 유사한 task를 진행한다해서 shared feature를 뽑으 수 있느 것이 아니라는 것을 알 수 있고 (실제로 각 task에 해당하는 loss를 관찰했을 때 여러 task의 합의점을 못찾는 듯 보임), Multi-task learning을 진행할 때 추가적인 장치들이 필요할 것 같음
