---
layout: post
title: "PyTorch 및 DeepLearning 관련 자주 사용하는 코드"
summary: "PyTorch 및 DeepLearning 관련 자주 사용하는 코드"
author: taehun
date: '2021-12-03 15:00:00 +0900'
category: Python
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: DeepLearning, PyTorch, CNN, GPU
permalink: /9
mathjax: true
use_math: true
---

> `PyTorch Framework로 DeepLearning 학습시 자주 사용하는 코드 `

#### Index
---

- [1. FFT](#1-fft)
- [2. matplotlib.pyplot params](#2-matplotlib-pyplot-params)
- [3. 신호에 SNR 값에 따른 노이즈 추가](#3-신호에-snr-값에-따른-노이즈-추가)
- [4. Bayesian Optimization](#4-bayesian-optimization)


#### **3. FFT**
  
<br>
  
  - FFT Code

Version 1

```python
def fft_th(data, sampling_frequency, label, mode = 1):
    y =data-np.mean(data)
    yf = np.abs((np.fft.fft(y)/len(y)).real)
    xf = np.fft.fftfreq(len(y))
    xf=xf*sampling_frequency
    xf_=xf[:np.argmax(xf)]
    yf_=yf[:np.argmax(xf)]
    
    if mode==1:
        plt.plot(xf_, np.abs(yf_), label = label)
        plt.legend(loc = 'upper right')
    return xf_, yf_
```

Version 2

```python
def fft(data, sampling_rate):
    tmp_data = data - np.mean(data)
    n = len(tmp_data)
    y = np.fft.fft(tmp_data)/n
    y = y[range(int(n/2))]
    y = abs(y.real)
    k = np.arange(n)
    
    x = np.fft.fftfreq(n, d = 1/sampling_rate)
    x = x[range(int(n/2))]
    return x, y
```

   **적절히 설정해서 사용**

<br>

#### **2. matplotlib pyplot params**

```python
params = {'axes.labelsize' : 16,
         'axes.titlesize' : 18,
         'xtick.labelsize' : 14,
         'ytick.labelsize' : 14,
         'legend.fontsize' : 14,
         'font.family' : 'Times New Roman'}
plt.rcParams.update(params)
```

#### **3. 신호에 SNR 값에 따른 노이즈 추가**

```python
def SNR(snr, signal):
    power = np.mean(signal ** 2)
    power_db = 10 * np.log10(power)
    
    noise_power_db = power_db - snr
    noise_power = 10 ** (noise_power_db / 10)
    
    mean_noise = 0
    noise = np.random.normal(mean_noise, np.sqrt(noise_power), len(signal))
    
    return signal+noise
```

<br>

#### **4. Bayesian Optimization**

```python
from bayes_opt import BayesianOptimization

def black_box_function(x,y):
  ...
  return output
```

```python
pbounds = {'x': (0,1), 'y': (1,10)}
  
optimizer = BayesianOptimization(
  f = black_box_function,
  pbounds = pbounds,
  random_state = 1
  )
```
  
  optimizer.maximize(
    init_points = 2,
    n_iter = 5
)
```
