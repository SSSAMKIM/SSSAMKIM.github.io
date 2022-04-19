---
layout: post
title: "Spectral Temporal Graph Neural Network for Multivariate Time-series Forecasting 리뷰"
summary: "GNN, Meta-learning 활용한 다변수 시계열 예측"
author: taehun
date: '2022-04-19 21:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: GNN, Meta-learning, Time-series, Forecasting
permalink: /14
mathjax: true
use_math: true
---

> `NeurIPS 2020 Spectral Temporal Graph Neural Network for Multivariate Time-series Forecasting 리뷰`

#### Index
---

- [1. Introduction](#1-introduction)
- [2. Problem Definition](#2-problem-definition)


#### **1. Introduction**
  
<br>

- **Research gap**
  - 대부분의 previous research들은 inter-class correlation을 고려하지 않는다.<br>
  - GNN을 활용하기 위해서는 prior 정보를 알아야 한다는 제약이 있다.<br><br>

- **Brief explanation for the proposed method**
  - 제안하는 Spectral Temporal Graph Neural Network(약칭 StemGNN)는 spectral domain에서 inter-series correlation과 temporal dependecy(intra-series)를 jointly 하게 capture<br>
  - Inter-series correlation은 Graph Fourier Transform(GFT)로, temporal dependcy는 Discrete Fourier Transform(DFT)로 파악<br>
    - 순서는 GFT가 먼저 적용. 다변수 입력이 spectral time-series 표현으로 변경되고, 다른 경향들은 orthogonal time-series로 분해됨<br>
    - DFT는 각각의 단일 시계열 변수들을 frequency domain으로 변경하는 역할을 함<br>
  - StemGNN layer로 들어가기 전에 latent correlation layer도 사용되는데, 이는 입력 변수들의 inter-series correlation을 파악하기 위함<br>
    - Latent correlation layer의 사용으로 prior 정보인 multivariate dependency가 필요하지 않게 됨<br>
    - Latent correlation layer는 graph structure와 weight matrix W를 구하는 layer<br><br>

#### **2. Spectral Temporal Graph Neural Network**

- **More details**
  - Graph Fourier Transform(GFT)
    - Graph G를 spectral matrix representation으로 변환하는 operator<br>
    - 각 노드마다 단일 시계열 변수들이 linearly independent 하도록 만드는 역할<br>
  - Discrete Fourier Transform(DFT)
    - 각 단일 시계열 변수들을 frequency domain으로 변환하는 역할<br>
    - Frequency domain에서 representation은 1d convolution과 GLU sub-layer를 통해 feature pattern을 찾아냄<br>
    - 이후 inverse DFT(IDFT)를 통해 다시 time domain으로 변환되고, 마지막으로 inverse GFT(IGFT) 적용<br>
  - Additional layer
    - StemGNN layer 이후 GLU layer와 FC layer를 추가하여 두 가지 output ![Lf](https://latex.codecogs.com/svg.latex?\small&space;Y_i,\widehat{X_i})를 얻음<br>
    - ![Lf](https://latex.codecogs.com/svg.latex?\small&space;Y_i)는 future value를 estimation하기 위함 output이며, ![Lf](https://latex.codecogs.com/svg.latex?\small&space;\widehat{X_i})는 backcasting output을 estimation<br>
    - Final loss<br>
      ![Lf](https://latex.codecogs.com/svg.latex?\small&space;L(\widehat{X},X;\Delta_\theta)=\sum_{t=0}^T||\widehat{X_t}-X_t||_2^2+\sum_{t=K}^T\sum_{i=1}^K||B_{t-i}(X)-X_{t-i}||_2^2)<br>
      - First term: forecasting loss, last term: backcasting loss<br><br>

- **Latent Correlation Layer**
  - GNN 기반의 방식은 graph structure를 필요로 하며, 보통 human knowledge를 prior로 활용한다.<br>
  - 하지만, prior로 pre-defined graph structure가 없는 경우들이 있으므로 self-attention을 활용해서 다변수 시계열 입력의 latent correlation을 학습한다.<br><br>

- **StemGNN Block**
  - StemGNN layer는 StemGNN block + skip connection을 활용한 layer<br>
    - Skip connection(=residual connection)은 StemGNN block을 stack 하기 위해 사용됨<br>
  - StemGNN block은 Spectral Sequential(Spe-Seq) cell을 spectral graph convolution module에 embedding 시키는 block<br>
  - Spectral domain에서 다변수 시계열 입력의 latent representation을 학습하는 능력이 우수하다고 함<br>
  - Key는 inter-series 관계를 파악하는 GFT를 적용하는 것. 이 때 output 역시 다변수 시계열이지만, intra-series temporal relationship은 학습하지 않음<br>
  - 따라서, GFT 적용 후 Spe-Seq cell 내에 DFT를 적용하여 intra-series relationship을 파악하고자 하는 것<br><br>

- **Spectral Sequential Cell(Spe-Seq Cell)**
  - Spe-Seq cell은 DFT -> 1d-conv -> GLU -> IDFT로 이루어짐<br>
  - 1d-conv, GLU layer는 DFT 이후 frequency domain에서 feature representation을 학습하기 위함<br><br>

- **Spectral Graph Convolution**
  - GFT는 Spectral Graph Convolution의 basic operator이며, bases가 normalized graph Laplacian의 eigenvector로 구성된 orthonormal space에 input graph를 사영시킴<br>
  - Normalized graph Laplacian은 아래와 같이 계산됨<br>
    - ![Lf](https://latex.codecogs.com/svg.latex?\small&space;L=I_N-D^{-1/2}WD^{-1/2})<br>
  - Graph convolution operator는 ![Lf](https://latex.codecogs.com/svg.latex?\small&space;g_\Theta(\Lambda)) 함수를 통해 연산됨<br><br>

<br>
