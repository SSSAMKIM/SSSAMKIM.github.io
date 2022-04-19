---
layout: post
title: "Alias-Free Generative Adversarial Networks 리뷰"
summary: "GAN 모델의 Aliasing 발생 분석"
author: taehun
date: '2022-04-19 15:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: GAN, Signal processing, Aliasing, Nyquist frequency, Upsampling
permalink: /13
mathjax: true
use_math: true
---

> `Alias-Free Generative Adversarial Networks 논문 리뷰`

#### Index
---

- [1. Introduction](#1-introduction)
- [2. Equivariance via continuous signal interpretation](#2-equivariance-via-continuous-signal-interpretation)


#### **1. Introduction**
  
<br>

- **Research gap**
  - Coarse, low-resolution feature들은 upsampling layer에 의해 계층적으로 다듬어지고, convolution layer에 의해 국소적으로 섞이며, 새로운 세부사항은 비선형성을 통해 추가된다.<br>
  - Coarse feature들은 coarse feature의 정확한 위치를 제어하는 것이 아니라, finer feature의 존재를 제어한다.<br>
  - 그 대신에, 많은 fine detail들이 pixel coordinates에 고정되는 것 같다는 것.<br><br>

<center>
  <img src="https://user-images.githubusercontent.com/86653075/163946229-4332c4af-da2d-4976-98f6-4b6f086f5ea0.png" "width:600; height:auto;">
</center>

- **Figure 설명**
  - Averaged는 central latent vector 근방에 있는 latent에서 생성된 이미지들을 평균낸 것으로, 이미지 전체적으로 균일하게 blurred 될 것이 기대되나, StyleGAN2의 경우 대부분의 feature들이 픽셀 좌표계에 stuck 되어 있는 것처럼 보임<br>
  - 즉, 눈동자를 제외한 detail들은 선명하게 보이며, 이 detail들을 논문에서는 "texture sticking" 이라 표현한다.<br><br>

- **Texture sticking에 대한 previous research**
  - 이미지 경계, 픽셀별 노이즈, positional encoding, 그리고 aliasing을 통해 발생하는 것으로 보임<br>
    - 이미지 경계에서 발생하는 texture sticking은 약간 더 큰 이미지(ex. padding 추가)를 통해 간단하게 해결 될 수 있다.<br>
  - 위 4가지를 통해 intermediate layer에서 접근 가능한, 전혀 의도하지 않은 positional reference가 설정됨으로써, hierarchical한 구조가 아니라, output 이미지에 우회해서 도달할 수 있는 문제점이 발생한다는 것<br>
  - 위 4가지 중에서 이 논문은 Aliasing에 초점을 둔다.<br><br>

- **GAN에서 Aliasing 발생 원인 2가지**
  - Nearest, bilinear, strided convolution 같은 이상적이지 않은 upsampling filter를 사용하게 되면 aliasing이 발생할 수 있다.<br>
  - Pointwise 즉, 각 pixel 별로 ReLU와 같은 비선형성을 적용하게 되면 강한 경계가 생기면서 high freuqency 발생으로 aliasing이 일어날 수 있다.<br><br>

- **How to eliminate the unwanted side information, aliasing?**
  - Classical한 방법으로는 Shannon-Nyquist signal processing framework를 활용<br>
  - GAN에서는 discrete sample grid에 의해 표현되는 continuous domain에서 bandlimited function에 초점을 맞추자는 것<br>
  - 논문에서 positional reference의 모든 요소들을 성공적으로 제거한다는 것은, 이미지 detail들이 pixel coordinate에 상관 없이 동등하게 생성될 수 있다는 것을 의미한다.<br>
  - 그리고 이는, sub-pixel translation이 모든 layer에서 영향을 미칠 수 있도록 만든다는 것을 의미한다. (기존 GAN은 아마 특정 layer에서 sticking 되어 있는 것과 대조적인 것을 의미하는 듯)<br><br>

#### **2. Equivariance via continuous signal interpretation**

<br>
