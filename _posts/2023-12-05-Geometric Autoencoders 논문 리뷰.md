---
layout: post
title: "Geometric Autoencoders 논문 리뷰"
summary: "Geometric Autoencoders 논문 리뷰"
author: taehun
date: '2023-12-05 12:00:00 +0900'
category: Review
toc: true
toc_sticky: true
toc_label: "My Table of Contents"
toc_icon: "cog"
thumbnail: null
keywords: Python
permalink: /23
mathjax: true
use_math: true
---

Last update: 2023.12.05<br>

> `Geometric Autoencoders - What You See is What You Decode 리뷰'<br>
> > 2023 ICML Conference

<br>

#### Index
---

- [1. Terminology](#1-terminology)
- [2. Summary](#2-summary)<br><br>

#### **1. Terminology**
  
<br>

```markdown
1) 전사함수(surjection)
```

> ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/54f77377-725f-421f-84c6-2d271ff8075e) 에서 f(x) (치역, range)와 Y (공역, codomain)가 일치할 때 f는 전사함수라 함<br>

```markdown
2) 단사함수(injection)
```
> ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/54f77377-725f-421f-84c6-2d271ff8075e) 에서 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/427b2c2e-02db-4833-86d2-519e2baacc86) 에 대해,
  ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/bc78d3c8-9b4d-4495-b7b6-1079218e7a6e), 즉 일대일 함수인 경우 단사함수라 함<br>

```markdown
3) Chart
```

> - ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/a46a482d-5a6c-4a41-ac50-6136efab3157) domain U에서 range V로 가는 각각의 mapping을 chart라 함<br>
> - 혹은, smooth manifold에 대해, 어떤 open sets U가 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/2c55be0b-7e1d-4d90-ba1e-afb84a747c89)의 부분공간에 대해 위상동형이고, open sets U에 의해 덮을 수 있을 때 덮어서 대응되는 각 mapping이 chart<br>

```markdown
4) Differential of f at p
```

> - Manifold ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/1f778db5-627b-4064-b1a4-42aacf4b3808)를 만족하는 함수 f에 대해
  ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/bdf40a78-d8c0-48d7-aecc-dd56dd883bb9)를 manifold M 위의 점 p에서 함수 f의 differential이라 정의하며, 이 때 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/56fb0f11-974e-46e5-be59-f6bb9a4d2528)은 manifold M 위의 점 p에서의 tangent space를 의미함
> - Differential은 변수(x)의 미소 변화(dx)를 의미하며, differentiation과 동일하지는 않은 개념임
> - Coordinates에서의 differential은 Jacobian으로 계산 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/1f7db2e2-fc44-4753-9653-d8392d19707f)

<br>

```markdown
5) 위상동형(Homeomorphism)
```

> 함수가 전사, 단사이며 모든 점에서 연속 역함수도 전사, 단사, 연속인 경우를 의미<br>

```markdown
6) 미분동형(Diffeomorphism)
```

> 함수가 homeomorphism이며 미분 가능하고, 역함수에 대해서도 미분가능한 경우를 의미<br>
  
```markdown
7) Immersion
```

> from small space to big space<br>

#### **2. Summary**

<br>

- Dimensionality reduction으로 많이 사용되는 UMAP과 t-SNE는 local structure를 잘 보존하나, global structure를 보존하지는 못함<br>
- Autoencoder의 경우 encoder가 powerful하면 distortion을 유발하게 되는데, decoder도 powerful할 경우 distortion에 무관하게 reconstruction 성능은 좋지만, 이 distortion을 문제 삼는 것<br>
- 결국 visualization을 위한 low-dimensional autoencoders에서 latent representation에서 distortion이 발생해도 낮은 reconstruction loss를 가지는 문제를 decoder를 area-preserving하게 만듦으로 해결하고자 함<br>
> 1) Generalized Jacobian determinant를 활용하여 local expansion, contraction을 측정하는 것을 제안<br>
> 2) Generalized Jacobian dterminant의 log variance를 regularizer로 활용하여 이 값을 최소화함으로써 local expansion 및 contraction이 없는 즉, distortion이 발생하지 않도록 규제<br>
> 3) Generalized Jacobian determinant는 undirected contraction만 측정하기에, indicatrices를 활용하여 latent space 위 각 점의 anisotropy를 시각화 함<br>

<br>

<p align="center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/8c696d4a-80a4-4582-9427-60c48518e8a5" width = "800" height = "auto">
</p>
> 위 figure에서 세계 지도에 대한 embeddings을 확인하면 Geometric AE가 정성적인 관점에서 더 우수한 성능을 보이나, Vanilla AE의 reconstruction loss가 Geometric AE의 절반만큼 낮음<br>
  (Vanilla AE는 locally stretching or contracting하기 때문)
  
<br><br>

- Decoder가 하는 일은 latent space에 있는 surface를 output space로 fitting 하는 것인데 이 때 임의의 방향으로 stretching 하게 됨
  > 이 때 excessive stretching은 latent space에 불필요한 distortion을 가져 오게 됨


<br><br>


**2-1) 중요 수식**<br>

```markdown
1) Jacobian determinant
```

> 일반적으로 Jacobian determinant ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/45f438d8-1fea-4bbf-ade5-ff8f973d93fc)
는 pre-image 위의 점 p가 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/efa2e252-a0c5-4aa3-88d9-75dceb7aec65)를 만족시키는 함수 f에 대해 미소부피가 얼마나 변하는지를 측정하는 것<br><br>

```markdown
2) Generalized Jacobian determinant
```

> - Jacobian determinant는 동일 차원에서 미소 부피 변화를 측정하는 수식이나, 이를 확장하여 smooth immersion에서 미소 부피 변화를 tracking 하고자 하는 것이 generalized Jacobian determinant

> - ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/53ad9e56-5751-49e7-ad99-d4ab184d1668)가 smooth immersion이라 가정하고(즉, decoder 작업을 떠올리면 됨), F는 diffeomorphism이며, Euclidean metric g에 대해 (N,g)가 Riemannian manifold라 할 때, F(M) 위의 Riemannian volume form ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/000c95af-ce93-439c-937e-8c5ab810f1a9)는 아래와 같이 정의됨

<br>

  <p align="center">
    <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/479df772-a9a5-43ad-8311-51b762d76177">
  </p>
  <br>
> - 이 때 square root 안의 식인 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/7f4f4cd6-ccec-4d1d-af11-2761cfe86dd2)가 generalized Jacobian determinant이며, 이는 F에 의해 국부적으로 volumes이 얼마나 변하는지를 나타내고, 이를 통해 distortion of angles와 directed stretching에 대한 정보를 capture할 수 있음<br>
> - Generalized에서 transposed Jacobian을 곱해주는 이유는 아마 immersion 이기에 Jacobian이 square matrix가 아니라 square matrix를 만들어주기 위함으로 생각됨됨
  
<br><br>

```markdown
3) Pullback metric
```

> - Autoencoder의 latent space를 이해하기 위해서는 decoding 이후의 angles과 distances가 어떻게 나타나는지 알아야 함
> - 이 때 필요한 것이 latent space에 필요한 metric tensor이며, 그 이유는 angles와 distances들이 output manifold로 mapping 되기 때문에 metric tensor를 알아야 함
<br>(후에 metric tensor를 output manifold로 변환시켜 output manifold에서의 angles와 distances들을 구하기 위해?)
> - 이 latent space 상에 metric tensor를 pullback metric이라 정의함

<br>

> - Euclidean metric ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/fd9e4027-9f27-4dbd-a749-5495a088150a)에 대하여
 Riemannian manifold ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/20694325-14b5-420a-a250-33f3c54d91c9)가 존재할 때, decoder에 해당하는 immersion ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/fce94910-b808-4ad0-a585-5278e0af64b7)에서 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/ac5c5f12-d0c4-4094-8bbb-f787650108ce)인 점 p에서
pullback metric ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/ba1ae52d-b0a4-4188-871a-9564e64114e7)은 아래와 같이 정의됨

<p align="center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/39e4ede7-c934-4060-97d9-1a2e6e57571f">
</p>

<br>

> 이 때 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/47831d8d-1bdb-495a-b510-abc76350e4d0)이며, 점 p에서 함수 F의 differential은 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/fb202503-8d55-45e4-8a14-5edae1941f3e)로 나타남

<br>

```markdown
4) Pullback metric in coordinates
```

<p align="center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/fc8fc1e9-94d3-4787-99d0-3eba8f7b43c0">
</p>

<br>

> 위 식은 pullback metric과 generalized Jacobian과의 관련성을 나타내며, pullback metric은 실제로는 latent space에서 immersed manifold를 따르는 길이로서의 lengths를 측정함

<br><br>

<p align = "center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/86936e7e-038b-4e31-8f77-314fe39cde7e" width = "800" height = "auto">
</p>

**2-2) Regularization**

> - Generalized Jacobian determinant가 local expansion과 contraction을 측정하기에, 이 값들이 전역적으로 uniform하게 되면 distortion을 피할 수 있음
> - Minibatch B의 모든 embedding point에서 generalized Jacobian determinant를 계산하고 이 값의 variance of logarithm을 regularizer로 활용

<br>

<p align="center">
  <img src = "https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/db32992f-1ddf-455a-9354-cfb5e62b8acd">
</p>

> 위 regularizer에서, generalized Jacobian determinant 값이 1일 경우 isotropy지만, 각 지점에서 expansion도 있고 contraction도 있을 것이기에, variance가 최소화되는 방향으로 학습하면 전역적으로 isotropy에 가까워질 것을 의미

<br>

> Total loss는 ![image](https://github.com/SSSAMKIM/SSSAMKIM.github.io/assets/86653075/337dfc70-94b5-4d03-a037-24138935be7d)

