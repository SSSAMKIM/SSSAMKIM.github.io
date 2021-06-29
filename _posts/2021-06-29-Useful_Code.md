---
layout: post
title: "Useful Code for DeepLearning"
summary: "딥러닝 학습시 주로 사용하는 코드 정리"
author: taehun
date: '2021-06-29 16:00:00 +0900'
category: Study, Python
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: DeepLearning, Keras, CNN, GPU
permalink: /python/2
mathjax: true
use_math: true
---

> `GPU 메모리 할당, FFT, keras 기반 딥러닝 모델 학습시 callback/learning rate decay 등 주로 사용하는 유용한 코드 정리
`

#### Index
---

- [Useful Code](#useful-code)

### Useful Code
---

#### **1. Callback, Learning rate decay 참고 코드**

<br>

  ```python
  lr_scheduler = keras.callbacks.ReduceLROnPlateau(factor = 0.5, patience = 5)

  optimizer = keras.optimizers.Adam(lr = 0.001)
  model.compile(optimizer = optimizer
               ,loss = 'categorical_crossentropy'
                ,metrics = ['accuracy'])

  callbacks = [keras.callbacks.ModelCheckpoint(filepath='best_model.h5',
                                                  monitor='val_loss',
                                                  save_best_only=True)]
  ```
  
  ```python
  hist = model.fit(X_train, y_train, epochs = 40,
                       validation_data = (X_test, y_test), callbacks = [callbacks, lr_scheduler])
  ```

<br>

#### **2. GPU 관련**

<br>

  - GPU 사용 중인지 확인

  ```python
  import tensorflow as tf
  from tf.python.client import device_lib
  print(device_lib.list_local_devices())  
  ```
  
  - GPU Memory 할당

  ```python
  config = tf.compat.v1.ConfigProto()
  config.gpu_options.per_process_gpu_memory_fraction = 0.4
  session = tf.compat.v1.Session(config = config)
  ```
  
   **0.4는 할당 비율로, 할당하고 싶은 만큼 할당하면 됨**
 
 <br>
  
#### **3. FFT**
  
  <br>
  
  - FFT Code

  ```python
  def fft_th(data, sampling_frequency, mode = 1):
    sf = sampling_frequency
    y = data - np.mean(data)
    yf = np.abs(np.fft.fft(y).real)
    xf = np.fft.fftfreq(sf, 1/sf)
    xf = xf[xf>0]
    
    if mode == 1:
        plt.plot(xf, yf[:len(xf)], label = lab)
        plt.legend(loc = 'upper right')
  ```
   **적절히 설정해서 사용**
   
   <br>
   
#### **4. Data Generator**

 <br>
 
  - Dataset 생성 코드 예시

  ```python
  def data_generator(batch_size, sample_point, root_dir, label):
      for i in range(len(label)):
          df = pd.DataFrame(columns = range(sample_point))
          data = pd.read_csv(root_dir + '\\' + label[i] +'.csv', engine = 'python', header = None)
          L = len(data)
          for n_batch in range(batch_size):
              rand = np.random.randint(L - sample_point) + 1
              df_ = pd.DataFrame(np.array(data[data.columns[0]][rand:rand + sample_point]).reshape(1,sample_point))
              df = df.append(df_)
          df.to_csv(root_dir + '\\' + 'sample_point_{}'.format(sample_point) + '\\' + '{}.csv'.format(i), header = None, index = None)
  
  batch_size = 1000
  sp = 512
  label = ['12k_OF_7_1797']
  root_dir = './'
  
  data_generator(batch_size, sp,root_dir, label)
  ```
  
  <br>
  
#### **5. 가상환경 설치 및 GPU 연결**

  <br>

- **사용환경**<br><br>
  - Intel i7-8700 CPU @3.20 GHz
  - RAM 64GB
  - GPU : Nvidia RTX 2080 Ti
  - python 3.7.9
  - tensorflow/tensorflow-gpu 2.3.0
  - CUDA 10.1(Nvidia driver의 CUDA Version과는 별개)
  - cuDNN 7.6.5

  <br>

**버전에 맞는 CUDA, cuDNN 설치 후 아래 진행**
  
  <br>

  ```
  1. conda create -n 이름 python = 3.7
  2. conda activate 이름
  3. conda install ipykernel jupyter
  4. python -m ipykernel install --user --name 이름 --display-name "이름"
  5. pip install tensorflow-gpu==2.3.0
  6. pip install keras
  7. conda install pandas
  8. conda install matplotlib
  9. pip install scikit-learn
  ```
  
  <br>
  
  **PyTorch 설치시(PyTorch 설치 후 진행)**

  <br>
  
  ```
  1. conda create -n 이름 python=3.7
  2. conda activate 이름
  3. conda install ipykernel jupyter
  4. python -m ipykernel install --user --name 이름 --display-name "이름"
  5. conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
  ```
  
  <br>

#### **6. 가상환경 삭제 및 jupyter내 가상환경 삭제**

  <br>

  ```
  1. conda remove --name 이름--all
  2. jupyter kernelspec uninstall 
  ```
