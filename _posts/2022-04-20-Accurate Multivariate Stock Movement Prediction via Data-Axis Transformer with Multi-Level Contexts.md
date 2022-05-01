---
layout: post
title: "Accurate Multivariate Stock Movement Prediction via Data-Axis Transformer with Multi-Level Contexts 리뷰"
summary: "다변수 입력에 대한 주가 예측 관련 논문 리뷰"
author: taehun
date: '2022-04-20 22:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: Time series, Transformer, Forecasting, Attention mechanism
permalink: /16
mathjax: true
use_math: true
---

Last update:2022.05.02<br><br>

> 'ACM SIGKDD Conference on Knowledge Discovery and Data Mining Proceeding 리뷰`

#### Index
---

- [1. Introduction](#1-introduction)
- [2. Related Works](#2-related-works)
- [3. Proposed Approach](#3-proposed-approach)<br><br>

- **Research gap**
  - Stock prediction에 대한 정확도를 높이기 위해서는 stock 간 correlation을 활용할 필요가 있다.
  - 그러나 Stock은 시장의 세계적이 흐름에 영향을 받기에, 비대칭성이 크고 유동적이므로 stock 간에 correlation을 정확히 얻는 것이 힘들다.<br><br>

- **Brief explanation for the proposed method**
  - Data-axis Transformer with Multi-Level contexts(DTML)으 활용항 비대칭적, 동적 상관관계를 아래 3가지를 활용하여 구한다.<br>
    1. 각 stock 내에서 temporal correlation을 계산한다.<br>
    2. Global market context에 기반하여 multi-level contexts를 구한다.<br>
    3. Inter-stock correlation을 계산하기 위해 transformer encoder를 활용한다.<br><br>
  
#### **1. Introduction**

- **Summary of introduction**
  - 대부분의 stock은 같은 산업군에 속한 sector로 cluster 되는 경향이 있다.<br>
  - Stock 간에 correlation을 활용하는 이전 연구들은 대체로 미리 정의된 sector list에 의존하나, 아래와 같은 한계점이 존재한다.<br>
    1. 특히 학습 데이터를 긴 기간에 걸쳐 학습할 수록 시간이 흐름에 따라 자연스럽게 변하는 stock correlation의 dynamic property를 알 수 없다는 문제가 있다.<br>
      (투자 확대 등으로 전체 stock이 상승하는 경우 그 correlation의 의미가 흐려질 수 있다는 의미?)<br>
    2. Sector가 모호하거나, sector 정보가 없는 경우 prediction model이 적용될 수 없다.<br>
    3. 예측 성능이 prediction model이 아닌, sector information의 quality에 강하게 의존한다.<br>
  - Data-axis Transformer with Multi-Level contexts(DTML) 요약<br>
    1. temporal attention을 활용하여 multivariate historical price를 요약하는 comprehensive context vector를 생성해 낸다.<br>
    2. 생성된 context vector를 시장의 global movement와 결합하여 multi-level로 확장시킨다.<br>
    3. Transformer encoder를 활용해서 multi-level context로부터 stock 간에 비대칭적, 동적 attention score를 학습한다.<br><br>


#### **2. Related Works**

- **Correlated Stock Prediction**

  - Closing price(종가)만 입력 데이터 활용하는 것은 제한적이며, opening price(시가), highest price(고가), 그리고 lowest price(저가) 또한 주가 예측에 중요한 변수이 수 있음<br>
  - GNN을 활용하는 모델의 경우, stock 간 graph를 구하기 위해 prior knowledge를 이용하기도 하고, 예측 모델로부터 학습된 graph와 prior knowledge를 모두 사용하기도 하나, 이 경우 사전에 이미 고정적으로 정의된 prior knowledge를 이용한다는 단점이 있음. 실제 stock 간 correlation은 계속 변화함.<br>
  - 따라서, 이 논문에서는 보다 정확한 correlation을 사저 지식 없이 학습을 통해 계산하고자 함.<br><br>

### **3. Proposed Approach**

- **Overview**

  - Considering multivariate features: 주가 예측에서 price=feature로 활용되며, opening, highest, lowest, closing price를 입력 변수로 활용<br>
  - Capturing global movements: Stock 간 correlation이 bull market(강세장)인지, bear market(약세장)인지에 따라서도 큰 영향을 받기에, market index를 활용하여 global trend는 따로 학습을 할 수 있도록 설계<br>
  - Modeling asymmetric and dynamic relationships: 정보 확산 속도가 상이한 이유로 주가는 asynchronous(비동시성)한 방식으로 변화하기에 stock 간의 실제 correlation에는 asymmetric(비대칭성)한 특징을 가진다. 따라서, 실제 상관관계의 비대칭성과 동적 특성을 모두 고려할 수 있어야 한다.<br><br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/86653075/165923568-49c9d7b5-f680-497a-966f-071e522cfce9.png" width="800" height="auto">
</p>

- **Descriptions of Figure**
  - Time Axis Attention
    - Attentive context generation: Temporal attention을 활용하여 각 stock 혹은 market index에 대한 context vector를 계산하는 과정<br>
  - Context Aggregation
    - Multi-level context aggregation: 계산된 market index의 context vector와 각 stock의 context vector를 combining하여 multi-level context vector를 계산하는 과정<br>
  - Data-Axis Attention
    - Data-axis self-attention: Multi-level context vector를 활용하여 서로 다른 stock 간의 correlation을 transformer encoder가 multi-head attention으로 attention map을 만들고, 이르 활용하여 최종적으로 각 stock에 대한 final prediction을 만드는 과정.  이를 통해 시간에 따라 동적으로 변화하는 해석 가능한 상관관계를 얻을 수 있음.<br><br>

- **[1] Attentive Context Generation**
  - 첫 번째는 각 stock의 multivariate historical prices를 single context vector로 summarize 하는 것. 
![Lf](https://latex.codecogs.com/svg.latex?\small&space;\left\{z_{ut}\right\}\leq T) (l은 (아마) multivariate으로 사용하려는 prices의 개수, u는 stocks, t는 time indices를 의미)를 input으로 받아서, 현재 time step T까지의 local movements를 summarize 하는 comprehensive context vector 
![Lf](https://latex.codecogs.com/svg.latex?\small&space;h_u^c)를 학습하는 것이 목적.<br>
  - **[1-1] Feature Transformation**: ![Lf](https://latex.codecogs.com/svg.latex?\small&space;\tilde{z_{ut}}=tanh(W_sz_{ut}+b_s))
    - 위 식과 같이 모든 feature vector ![Lf](https://latex.codecogs.com/svg.latex?\small&space;z_{ut})를 tanh을 activation으로 하는 single layer로 transform 한다.<br> 
  - **[1-2] Attention LSTM**: ![Lf](https://latex.codecogs.com/svg.latex?\small&space;\alpha_i = \frac{exp(h_i^Th_T)}{\sum_{j=1}^Texp(h_i^Th_T)})
    - LSTM의 output인 ![Lf](https://latex.codecogs.com/svg.latex?\small&space;h_T)대신 위 식과 같이 attention score을 활용하여 context vector
![Lf](https://latex.codecogs.com/svg.latex?\small&space;\tilde{h^c}=\sum_{i}\alpha_ih_i)를 계산. Query vector로는 마지막 hidden state인
![Lf](https://latex.codecogs.com/svg.latex?\small&space;h_T)를 사용. Attention score ![Lf](https://latex.codecogs.com/svg.latex?\small&space;\alpha_i)는 현재 step T에 관한 step i의 중요도를 의미.<br>
  - **[1-3] Context Normalization**:![Lf](https://latex.codecogs.com/svg.latex?\small&space;h_{ui}^c=\gamma_{ui}\frac{\tilde{h_{ui}^c}-mean(\tilde{h_{ui}^c})}{std(\tilde{h_{ui}^c})}+\beta_{ui})
    - 각 stock이 다양한 범위의 feature를 가지고, historical prices의 pattern 또한 다양하기에 attention LSTM에 의해 만들어진 context vector는 다양한 범위의 값을 가지게 될 것이며, 이는 추후 학습 과정의 불안정성을 야기할 것. 따라서, 위 식과 같이 layer normalization의 변형인 context normalization을 활용하며, i는 context vector에 있는 요소들의 index, mean과 std는 모든 주식과 요소들에 대해 계산된 값이고, ![Lf](https://latex.codecogs.com/svg.latex?\small&space;\gamma_{ui})와 ![Lf](https://latex.codecogs.com/svg.latex?\small&space;\beta_{ui})는 학습되는 파라미터이다.<br>

- **[2] Multi-Level Context Aggregation**
  - 미국 주식 시장에서는 NDX100, 중국 시장에서는 CSI300과 같은 market index를 사용함으로써 short-term fluctutation이나 개별 주식의 properties와 무관한, long-term perspective인 market movement를 따를 수 있도록 하는 과정. 여기에서는 개별 주식들의 time range와 같은 SNP500에 대한 데이터를 활용하고(물론 중국의 경우 CSI300 활용), attention LSTM을 사용하여 market context ![Lf](https://latex.codecogs.com/svg.latex?\small&space;h^i)를 출력.
    - Q. 각 국가의 주식들 또한 다른 market index에 영향을 받을텐데 이는 어떻게 고려할지?
  - [2-1] Multi-Level Contexts: ![Lf](https://latex.codecogs.com/svg.latex?\small&space;h_u^m=h_u^c+\beta h^i)
    - 각 

<br>
