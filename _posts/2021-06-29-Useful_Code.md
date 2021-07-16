---
layout: post
title: "딥러닝시 자주 사용하는 코드 정리"
summary: "딥러닝 학습시 주로 사용하는 코드 정리"
author: taehun
date: '2021-06-29 16:00:00 +0900'
category: Python
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: DeepLearning, Keras, CNN, GPU
permalink: /9
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

1) Tensorflow

```python
import tensorflow as tf
from tf.python.client import device_lib
print(device_lib.list_local_devices())  
```

2) PyTorch

```python
print('cuda index:', torch.cuda.current_device())
print('gpu 개수:', torch.cuda.device_count())
print('graphic name:', torch.cuda.get_device_name())
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

Version 1

```python
def fft_th(data, sampling_frequency, label, mode = 1):
    y =data-np.mean(data)
    yf = np.abs(np.fft.fft(y).real)
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

**아래 코드는 low frequency일 경우 좀 더 깔끔하게 FFT 결과를 보여주는 코드**

```python
def fft_th_low(data, sampling_frequency, label, mode = 1):
    y =data-np.mean(data)
    yf = np.abs(np.fft.fft(y).real)
    xf = np.fft.fftfreq(len(y))
    xf=xf*sampling_frequency
    xf_=xf[:np.argmax(xf)]
    yf_=yf[:np.argmax(xf)]
  
    if mode == 1:
        plt.figure(figsize = (6,3))
        for i in range(len(xf_)):
            plt.plot([xf_[i], xf_[i]], [0,yf_[i]], 'b')
    return xf_, yf_            
```   
   
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
```
  
```python
batch_size = 1000
sp = 512
label = ['12k_OF_7_1797']
root_dir = './'
```

sp : batch 하나에 포함될 data point

```python
data_generator(batch_size, sp,root_dir, label)
```
  
  <br>
  
#### **5. 1D-CNN 10번 반복 코드 및 confusion matrix 저장 코드**

```python
def model_iterate(n_iter, X_train, y_train, X_valid, y_valid, X_test, y_test,
                     file_path, label = ['Normal', 'Misalignment', 'Oil Whirl', 'Rubbing', 'Unbalance']):

    def model_generate():
        model = Sequential()
        model.add(Conv1D(4,8, padding = 'same'))
        model.add(BatchNormalization())
        model.add(ReLU())

        model.add(Conv1D(8,4, padding = 'same'))
        model.add(BatchNormalization())
        model.add(ReLU())
        model.add(MaxPooling1D(padding = 'same'))

        model.add(Flatten())

        model.add(Dense(5))
        model.add(Softmax())

        lr_scheduler = keras.callbacks.ReduceLROnPlateau(factor = 0.5, patience = 5)

        optimizer = keras.optimizers.Adam(lr = 0.0001)
        model.compile(optimizer = optimizer
                     ,loss = 'categorical_crossentropy' #'mse', 'categoricla_crossentropy', 'binary_crossentropy', 'sparse_categorical_crossentropy'
                     ,metrics = ['accuracy'])

        callbacks = [keras.callbacks.ModelCheckpoint(filepath= file_path,
                                                        monitor='val_loss',
                                                        save_best_only=True)]
        return model, callbacks, lr_scheduler
    
    cf_stack = np.zeros([5,5], dtype = np.int32)

    for i in range(n_iter):
        print(f'----------------------------------------------------{i+1}th----------------------------------------------------')
        model, callbacks, lr_scheduler = model_generate()
        hist = model.fit(X_train, y_train,
                             epochs = 100, validation_data = (X_valid, y_valid), callbacks = [callbacks, lr_scheduler])
        model = load_model(file_path)
        y_pred = model.predict(X_test)
        cf = confusion_matrix(np.argmax(y_test, axis = 1), np.argmax(y_pred, axis = 1))
        cf_stack = cf_stack + cf
        
    return cf_stack
```
**적절한 Hyperparameter 설정 후 사용**

<br>
  
#### **6. 가상환경 설치 및 GPU 연결**

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

#### **7. 가상환경 삭제 및 jupyter내 가상환경 삭제**

  <br>

```
1. conda remove --name 이름--all
2. jupyter kernelspec uninstall 
```

<br>
  
#### **8. mat 파일 불러오기**

```python
import scipy.io
mat = scipy.io.loadmat('filepath')
```
