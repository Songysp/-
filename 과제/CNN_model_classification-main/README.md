# **데이터셋**
사용한 데이터셋은 o, x, △ 각각 50개씩 이루어진 손그림 데이터를 이용하였습니다.

# **모델**
```
model = nn.Sequential(
    nn.Conv2d(3, 32, kernel_size=3, padding='same'),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2),

    nn.Conv2d(32, 64, kernel_size=3, padding='same'),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2),

    nn.Conv2d(64, 64, kernel_size=3, padding='same'),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2),

    nn.Flatten(),
    nn.Linear(64 * 8 * 8, 64),
    nn.ReLU(),
    nn.Linear(64, 3)
).to(device)
```
해당 모델을 정의하여 사용했습니다

# 학습 평가

테스트 정확도는 83.33%
Epoch   50/50 Loss: 0.002929 Accuracy: 83.33%

![image](https://github.com/Songysp/CNN/assets/156406181/cf66e529-8718-4e8d-ab13-44edb3e28d8b)
