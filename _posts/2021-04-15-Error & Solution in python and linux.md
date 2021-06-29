---
layout: post
title: "Error & Solution in python and linux"
summary: "python, linux에서 발생하는 오류에 대한 해결책 정리"
author: taehun
date: '2021-04-15 10:46:00 +0900'
category: python
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: python, linux, error
permalink: /6
use_math: true
mathjax: true
---

> `python, linux에서 발생하는 오류에 대한 해결책` 정리, 계속 업데이트

#### Error & Solution
---

**1. unexpected indent**
  - 잘못된 들여쓰기로 인한 오류 발생<br>

**2. /.DS_Store 관련 not directory error**
  - os.listdir에서 list 만드는 도중에 생긴 DS_Store는 pop method로 삭제. - cannot identify image file ~~ /.DS_Store는 rm 명령어 사용해서 해당 경로의 .DS_Store file 삭제<br>

**3. OMP: Error #15: Initializing libiomp5.dylib, but found libiomp5.dylib already initialized**
  - conda install nomkl 이후 다시 실행하면 해결됨<br>

**4. PIL.UnidentifiedImageError: cannot identify image file <_io.BytesIO object at 0x7f1e96964db0> 에러**
  - .jpg 파일을 이용해서 model test 도중 발생한 에러. 입력 데이터로 사용하는 이미지 파일 중에 문제가 있는 파일이 있는 것으로, 해당 파일을 수정해야 함<br>

**5. ValueError: too many values to unpack (expected 2)**
  - 이 문제 말고 다른거 해결하다보니 해결됨..<br>

**6. dict.iteritems() error**
  - dict형 변수의 경우 python2.x에서는 iteritems()를 사용하지만 python3.x에서는 사라짐. 대신 items()를 사용하면 key, value를 얻을 수 있음 <br>

**7. Can't locate attribute: 'nb_layers'**
  - nb_layers는 number of layers 인 듯<br>

**8. write() argument must be str, not bytes**
  - with open(‘path’,’w’) as f: ~~~~ code에서 발생한 에러. - bytes는 8bit(=binary)이고, str은 unicode. -‘w’ 즉 문자 쓰기 모드로 실행시 str 형태로 작성되는 것 같음. 따라서 ‘wb’, 바이너리 쓰기 모드로 저장하면 위 문제가 해결됨 <br><br>

**9. ‘utf-8' codec can't decode byte 0x93 in position 0: invalid start byte**
  - np.load(open())에서 open()을 없애고 난 후에는 사라짐. 원인을 모르겠음 <br>

**10. Keyword argument not understood:’,’W_regularizer’ 에러**
  - Keras2에서는 W_regularizer 대신 kernel_regularizer를 사용 <br>

**11. Data cardinality is ambiguous error**
  - model.fit(train_data, train_data_labels, …)에서 data(input x)와 label(output y)의 갯수가 맞지 않아서 발생한 문제. 각각 어디서 문제가 발생했는지 확인한 후 해결했음 <br>

**12. a bytes-like object is required, not ‘str’**
  - python3에서는 2에서 없던 바이트 스트림 문자열 상수가 존재한다고 함. - with open(filename, ‘wb’) as f: 과정에서 발생한 에러인데, ‘wb’를 ‘w’로 바꾸면 해결됨 <br>

**13. Keyerror : ‘acc’**
  - tensorflow2.x 버전에서는 acc대신 accuracy를 사용 <br>

**14. Keyerror : ‘val_acc’**
  - 마찬가지로 tensorflow2.x에서는 val_accuracy를 사용 <br>

**15. TypeError: fit_generator() got an unexpected keyword argument 'samples_per_epoch'**
  - steps_per_epoch로 변경 <br>

**16. Typeerror : fit_generator() got an unexpected keyword argument ‘nb_val_samples’**
  - validation_steps로 변경 <br>

**17. x and y must have same first dimension, but have shapes (50,) and (1,) error**
  - 갯수 달라서 발생한 문제라 대강 해결했는데 근본적인 해결인지 모르겠음 <br>

**18. AttributeError: module 'urllib' has no attribute 'urlretrieve'**
  - urllib.urlretrieve —> urllib.request.urlretrieve로 변경 <br>

**19. ValueError: Input arrays should have the same number of samples as target arrays. Found 9480 input samples and 600 target samples.**
  - model.predict_generator(generator, nb_validation_samples) 코드 실행 과정에서 colab은 아무런 문제가 발생하지 않는데, aws에서 실행 결과 문제가 발생함. predict_generator 두번째 인자에 nb_train_samples 가 아닌 steps(=nb_train_samples/batch_size)가 들어가야 정상적으로 처리가 됨 <br><br>

**20. TypeError: Object of type 'float32' is not JSON serializable**
  - dict 변수 안에 numpy의 float class의 value 값을 가질 때 json.dumps를 이용해서 저장하면 에러가 발생함(colab에서는 발생하지 않고 aws에서만 발생함) —> 근데 해결 안됨. with open(‘filename’,’w’) as f:  json.dump(output) 에서 발생한 error인데 ‘w’를 그냥 ‘wb’로 변경하면 해결되는 문제.. <br><br>

**21. AttributeError: '_io.TextIOWrapper' object has no attribute 'items'**
  - <br>

**22. WARNING:tensorflow:Your input ran out of data; interrupting training. Make sure that your dataset or generator can generate at least `steps_per_epoch * epochs` batches (in this case, 600 batches). You may need to use the repeat() function when building your dataset.**
  - model.predict_generator(generator, nb_train_samples)에서 발생한 에러로, 2번째 변수에는 nb_train_samples를 batch_size로 나눈 steps가 들어가야 함. 19번과 유사한 에러로 colab에서만 발생했음 <br><br>

**23. OOM when allocating tensor with shape[25088,4096] and type float on /job:localhost/replica:0/task:0/device:GPU:0 by allocator GPU_0_bfc [Op:Add] error**
  - colab에서 발생한 문제, 사용 GPU 비워줘야 함. aws에서 nvidia-smi 에서 sudo kill 과 유사하지만 명령어로 하는 것이 아니라, RAM, 디스크라고 보이는 용량 클릭해서 삭제할 수 있음 <br>

**24. PackagesNotFoundError: The following packages are not available from current channels:**
  - 다운받은 package들 사이에 버전이 맞지 않은 문제로 꼬인 상태. 새 가상환경 만드는게 가장 깔끔한 방법이지만, 꼬인 package들을 conda uninstall후 다시 install하면 해결될 수도, 안될 수도 있음 <br><br>

**25. Jupyter notebook에서 pip install 하는 방법**
  - 앞에 ! 를 추가하면 됨 ex) !pip install pandas <br>

**26. finished with exit code -11**
  - Jupyter notebook 다운로드하면서 가상환경에서 python 설치중 환경변수가 꼬인 것 같아 발생. python build path를 새로 깔아주면 작동은 하지만, 가상환경에서 설치한 파이썬이라 이것보다는 파이썬을 새로 설치할 필요가 있을 듯? <br><br>

**27. KeyError : 0**
  - Dict형에서 Key값이 없을 때 발생.  1) pandas.DataFrame에서 행을 선택할 때 X[0]으로 선택하면 KeyError가 발생하지만 X[:1]을 선택하면 원하는 결과를 얻을 수 있음. 2) X.loc[0] or X.iloc[0]을 사용 <br><br>

**28. KeyError : "None of [Int64Index([    1,     3,     4,     5,     7,     8,    10,    11,    12,\n               13,\n            ...\n            59984, 59985, 59987, 59988, 59989, 59991, 59993, 59994, 59996,\n            59998],\n           dtype='int64', length=40000)] are in the [columns]"**
  - DataFrame 형태가 아닌 Numpy 형태를 가져야 하므로 .values를 사용하면 해결됨 <br>

**29. 'str' object has no attribute 'reshape'**
  - pandas.DataFrame으로 되어있는 MNIST 데이터를 활용하다가 생긴 문제로, 그 dataframe의 이름이 A라면 np.array(A) 해주면 해결됨 <br>

**30. TypeError: 'list' object is not callable**
  - 보통 내장된 함수 또는 정의한 함수와 같은 이름의 변수를 사용할 경우 뜨는 에러. 내 경우 timeit을 import 하지 않은채로 timeit() 함수를 써서 문제 발생 <br>

**31. 'DType' object has no attribute 'type'**
  - <br>

**32. Excel xlsx file : not supported**
  - xlrd에서 xlsx 확장자를 읽는 기능이 불안정해서 지원을 끊음. pd.read_excel이나, openpyxl을 이용해야 함.  => 즉, pd.read_excel(“file_name.xlsx”, engine = “openpyxl”) 이나, openpyxl.load_workbook(“file_name.xlsx”)을 사용. <br><br>

**33. .csv 확장자에 ‘,’ separator로 연결하여 작성했는데 파일에 제대로 구분이 되어있지 않은 경우**
  - 예를 들어 ‘1’,’2’를 입력하여 Col1에 1, Col2에 2가 들어가야 한다. 하지만, “‘1’, ‘2’,”처럼 큰따옴표가 있다면 한 칸에 모두 들어가게 되므로, str.replace(‘“’, ‘’) 를 이용해서 큰따옴표를 제거해주어야 한다. <br><br>

**34. pd.read_csv 한글 깨짐**
  - encoding = ‘CP949’ 추가시 해결됨 <br>

**35. ValueError: expected min_ndim=3, found ndim=2**
  - dummy dimension을 추가해주면 됨 ex) X_train = X_train[…, None] <br>

**36. shapes (32,1) and (32,5) are incompatible**
  - Dense layer의 output을 5로 설정했고, class가 5개인 데이터에 대해서 categorical_crossentropy를 적용했는데, categorical_corssentropy는 one-hot encoding으로 되어 있어야 하므로 각 label 정보가 0,1,2,3,4로 설정된 상태라면 이 오류가 발생. 따라서 label 정보를 one-hot encoding 하거나, loss function을 sparse_categorical_crossentropy로 변경해야 함.<br><br>

**37. module 'numpy.linalg.lapack_lite' has no attribute '_ilp64'**
  - conda uninstall numpy후 재설치하니 완료됨<br>

**38. Warning! HDF5 library version mismatched error**
  - 특정 module 및 library를 import 할 때 발생했던 문제 => conda uninstall hdf5 이후 다시 install하면 위 warning은 뜨지 않지만, keras도 삭제됨. => hdf5 uninstall 이후 keras를 install 해야 함.
  - 위 방법 모두 해결되지 않았고, pip로 h5py uninstall후 다시 설치하면 해결됨. 이 때 현재 numpy, scipy, h5py에 대하여 tensorflow와 tensorflow-gpu가 요구하는 버전이 맞지 않다는 error문구가 뜨지만, 모든게 정상적으로 실행되긴 <br><br>
