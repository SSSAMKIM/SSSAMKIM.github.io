---
layout: post
title: "Review of ODR Article"
summary: "ODR논문 Review"
author: taehun
date: '2021-04-15 11:00:00 +0900'
category: Study
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: ODR, PHM
permalink: /7
use_math: true
mathjax: true
---

> `Omni-Directional Regeneration(ODR)` 논문 리뷰

#### Index
---

- [RK4 Testbed and Health State](#rk4-testbed-and-health-state)
- [Dataset](#dataset)
- [Fault Diagnosis](#fault-diagnosis)
- [Reference](#reference) <br>


#### RK4 Testbed and Health State
---

**RK4 Testbed**

- RPM : 3,600 in steady-state condition

- Sampling Frequency : 8,500Hz

- Sensor : Proximity sensor(measured in a voltage form)

  - AC component : Relative vibration of the shaft

  - DC component : Motion of the centerline of the shaft

  - Properties
  
    - 근접 센서(Proximity sensor)는 vibration signal을 voltage form으로 취득하며, 이 voltage는 센서와 rotor 사이의 gap에 비례한다.

    - 2개의 근접 센서는 직각으로 설치하여 각각 독립적인 진동 신호를 취득할 수 있으며, 직접 rotating shaft의 움직임을 측정하기에, 진동 신호가 rotor system의 물리적 특성을 보존할 수 있다.

    - 또한 2개의 근접 센서로 추출한 진동 신호를 사용하여 shaf centerline position의 orbit이 결정된다.

- Health State

  - **Misalignment** : RK4 testbed는 두 개의 shaft(each long, short one)가 coupling으로 연결되어 있는데, misalignment state를 위해 short shaft를 수평적으로 20um만큼 이동시킨다.

  - **Rubbing** : 정확하게는 impact rubbing이며, rubbing screw를 shaft에 직접 contact하여 rubbing state를 만들어낸다.

  - **Oil Whirl** : 베어링 틈새(*Bearing clearance)내에서 외부에서 가해지는 load(externel load, force)와 유막(oil film)의 압력간의 상호작용으로 발생. Bearing과 shaft는 동심원으로 회전하는데, shaft의 하중으로 인해 shaft의 중심이 약간 기울어져서 회전하게 되는 것으로, 균형이 맞지 않는 문제가 생기는 것이다. (Oil Whirl data are acquired at an oil pressure of 35kPa)

    ***Bearing clearance** : 전체 bearing의 지름에서 journal(or shaft)의 지름을 뺀 값으로, bearing과 shaft 사이의 마찰을 줄이기 위해 oil이 들어가는 공간
    
    - Oil whirl anomaly state 생성 과정 : 과도 응답 상태에서는 *oil whip을 방지하기 위해 압력이 상승된다. 3,600rpm의 정상 상태에서만 압력은 떨어지고 oil whirl anomaly state가 만들어진다.
    
    - Oil whirl은 oil이 shaft 원주 전체에 유막을 생성하는 것이므로 방향과는 무관한 특성을 가지게 된다.

    - cf) *Oil whip : Oil whirl frequency가 shaft의 natural frequency와 같을 때 발생하는 공진 현상으로, 이 진동수에 도달하면 rotor speed와 무관하게 oil whip frequency에 머물게 되어 journal bearing의 failure를 유발하게 된다.
  
<center>
  <img src = "/public/img/clearance.jpg" style = "width : 50%; height = auto;">
</center>

- Directional/Non-Directional Health State

  - 구분 기준 : 센서의 방향과 무관/유관한 신호 특성을 가지는 health state

  - Directional Health State

    - Misalignment, Rubbing

  - Non-Directional Health State

    - Normal, Oil Whirl

<br>
#### Dataset
---

- **Dataset**

  - 각 health state에 대하여 초당 60 cycles의 진동 신호를 60초동안 측정하므로 총 60개의 데이터, 3,600 cycles가 되고, 전체 데이터셋은 3개의 60-s의 data를 이용하여 각 state에 대해 test한다.

  > 즉, **`각각(총 3개)의 dataset`**은 **`health states에 대하여 60cycles/s의 진동신호를 60초간 측정한 데이터이다.`**


#### Fault Diagnosis
---

- Rotor system의 fault diagnosis에 가장 흔히 사용되는 방식은 vibration signal을 이용한 방식

- Orbit image를 이용한 Rotor system의 fault diagnosis 연구도 있었으나, orbit graph는 vibration signal에 대한 detailed physical interpretation이 부족

**1. Feature Generation**

  - **1)Preprocessing**
    
    - Reason and Purpose
    
      - Raw vibration signal의 uncertainties를 줄이기 위함

      - RPM은 steady-state condition에서도 약간의 variation을 가지는데, rpm의 variation은 feature extraction에서 일관성(consistency)을 떨어뜨린다.

    - How to

      - RPM의 variance를 줄이기 위해서 raw vibration signal이 resampled되며,이 논문에서는 angular resampling을 사용하는데, 이는 keyphasor signal을 reference로 해서 raw signal이 각 회전마다 같은 숫자의 point를 가지도록 만들어주는 방법이다.<br><br>

  - **2)Feature Extraction**

    - RK4 testbed는 steady-state condition에서 작동되므로, time-frequency domain features보다는 time- and frequency-domain feature가 사용된다.

    - Energy-related feature인 8개의 time-domain feature들과, fundamental, harmonic, sub-harmonic frequency 등의 정보를 포함하는 11개의 frequency-domain feature들이 사용된다.

    - Time-domain feature는 1 cycle based datum unit을, Frequency-domain featrue는 60 cycle based datum units를 사용한다.

  - **3)Feature Selection**

    - Featrue selection은 feature들중 진단 성능을 향상시킬 수 있는 최적의 feature subset을 결정한다.<br>

**2. Classifier**

  - **SVM Classifier**

    - v<sub>i</sub> : feature vector

    - w : weight vector, normal vector to the hyper-plane

    - b : bias vector

    - ξ<sub>i</sub> : slack variable(i번째 sample이 마진을 얼마나 위반할지 결정)

    - Objective function and Hypothesis

  <center>
    <img src="/public/img/SVM.png" style = "width : 30%; height : auto;">
  </center><br>

  - 1) 결정 함수(Hypothesis)의 기울기 dh/dx = ∥w∥로, 가중치 벡터의 norm과 같다. 이 기울기를 2로 나누면 결정 함수의 값이 1,-1이 되는 점들이 결정 경계로부터 2배만큼 더 멀어진다.

    - 즉, 마진을 크게 하기 위해서는 ∥w∥를 최소화해야 한다.

  - 2) 결정 함수가 모든 양성 학습 샘플에서는 1보다 커야 하며, 음성 학습 샘플에서는 -1보다 작아야 한다. 
    
    - 따라서, t<sup>(i)</sup>(w<sup>T</sup>x<sup>(i)</sup> + b)가 1보다 크거나 같은 아래 조건은 음성 샘플(y<sup>(i)</sup> = 0)일 때 t<sup>(i)</sup> = -1로, 양성 샘플(y<sup>(i)</sup> = 1)일 때 t<sup>(i)</sup> = 1로 정의할 때 2.를 만족시키는 조건이 된다.<br><br>

**3. Omnidirectional Regeneration**

<div style="width:25%; height:auto; float:left; margin-left:4%;">
 <img src="/public/img/odr1.png" style="width:100%; height:auto;">
</div>
<div style="width:25%; height:auto; float:left; margin-left:2%;">
 <img src="/public/img/odr2.png" style="width:100%; height:auto;">
</div><div style="clear:both;"></div><br>

<center>
  <img src="/public/img/odr3.png" style = "width : 20%; height : auto;">
</center>

- 위 변환식을 이용하여 x<sub>1</sub>, ... , x<sub>N</sub> vector와 y<sub>1</sub>, ... , y<sub>N</sub> 벡터를 만들어내는데, 이 때 각 벡터는 n개의 component를 가진다. 

- 이 때, N은 ODR 신호의 최대값으로 실험 세팅에 따라 설정해야 할 값이며, n은 time의 길이를 의미한다.

- x<sub>n+N/2</sub>은 y<sub>n</sub>과 정확히 일치하기에 x에 대한 ODR signal만으로도 fault diagnosis에 활용할 수 있으나, ODR 신호를 만들 때 x,y raw signal 모두 필요하므로 proximity sensor는 2개를 사용해야 함

**4. Directionality Evaluation Metric, D**

  - Directional anomaly states의 진단 성능을 높이기 위해 먼저 어떤 fault class가 directionality를 가지는지 결정해야 하는데, 논문에서는 Directionality metric D를 도입하였다.

  <center>
    <img src = "/public/img/direc_metric.png" style = "width : 20%; height : auto;">
  </center>
    
  - D는 vibration의 정도(level)과 health states에 무관하게 잘 작동하며, S<sub>N</sub>(f)는 N개의 ODR 신호에 대한 power spectrum을 의미하고, f<sub>1x</sub>는 회전 속도의 주파수, 즉 fundamental frequency를 의미한다.

  - Denominator는 normalizing constant로, metric이 진도 수준이나 이상 상태와 무관하게 잘 작동할 수 있도록 해주는 값이다.

  - Threshold는 unit value(1)로 설정하는데, 그 이유는 Non-directional state의 경우 signal들의 variation이 무시할 수 있는 수준이기에 1로 설정하여도 Directional/Non-directional을 구분할 수 있다.

  - **Directionality of Health States**

    - 아래는 3개의 datasets를 이용하여 5개의 health states에 대해 D value를 측정한 결과이다.

    <center>
      <img src = "/public/img/d_dataset.png" style = "width : 75%; height : auto;">
    </center>
    
**5. Classfication & Result**

  - Classifier는 SVM을 사용했으며, feature extraction을 통해 얻은 feature를 이용하여 사전에 학습된다.

  - Directional states의 경우, N개의 ODR 신호를 생성하여 unlabeled data를 SVM Classifier로 predict한다. 즉, 각 60-cycle data에 대하여 N개의 results를 얻게 되느 것이다.

    - 이렇게 얻은 N개의 result는 majority voting을 이용하여 final prediction을 얻는다.

  - Non-directional states의 경우, 앞선 directionality metric D를 통해 non-directional로 분류되고, 방향성과 무관하기에 proximity sensor로부터 얻은 raw signal로만 predict해도 ODR 신호의 결과와 거의 동일게 나온다.


<br>

#### Reference

- Joon Ha Jung, Byung Chul Jeon, Byeng D. Youn, Myungyon Kim, Donghwan Kim, Yeonwhan Kim, Omnidirectional regeneration (ODR) of proximity sensor signals for robust diagnosis of journal bearing systems, Mech. Syst. Signal. Process. 90 (2017) 189–207.


---


