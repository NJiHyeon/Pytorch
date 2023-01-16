### 데이터 전처리하기
    # X data : [ [학생1 데이터], [학생2 데이터], [], [] ]
    # Y data : [정답1, 정답2, 정답3, ...] or [ [정답1], [정답2], ...]
# 파이썬으로 엑셀처럼 데이터 다루고 싶을 때 쓴다.
import pandas as pd
data = pd.read_csv('score.csv')

# NA값 처리
    # 평균값
    # 행 삭제
# print(data.isnull().sum())
data = data.dropna()
# data = data.fillna(100) # 빈칸을 채워줌

# 유용한 pandas 사용법들
    # data['gpa']
    # data['gre'].min()
    # data['gre'].count()


# 본격적인 전처리
    # values
    # data.iterrow() : data라는 데이터프레임을 가로 한줄씩 출력해주라
        # i : 행 번호
        # rows : 값들
y데이터 = data['admit'].values

x데이터 = []

for i, rows in data.iterrows() :
    # [ rows['gre'], rows['gpa'], rows['rank'] ]  # 이거를 x데이터 칸 안에 넣기 !
    x데이터.append([ rows['gre'], rows['gpa'], rows['rank'] ]) 
    
# print(x데이터)



### (참고) 텐서플로우 안의 keras 쓰면 딥러닝이 쉬워진다.
    # keras를 안쓰면, w = tf.Variable() 이거부터 직접 해야한다.

import tensorflow as tf

# 1. 딥러닝 모델 
    # Sequential을 쓰면 신경망 레이어들을 쉽게 만들어준다.
        # 레이어 안에 숫자 = 노드의 개수 
        # activation function 넣기
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),  
    tf.keras.layers.Dense(128,activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
]) 

# 2. 모델 완성 단계
    # 옵티마이저 
        # 경사하강법으로 w값을 수정하는데, 기울기를 뺄 때 learning rate를 곱해서 빼는데, 빼는 값을 어떤 식으로 정할 지?
        # 항상 균등하게 빼면 학습이 잘 안될 수 있기 때문
        # 상황에 맞게 learning rate를 조정해서 ~
    # 손실함수
        # binary_crossentropy : 확률 예측 때, loss function
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 3. 모델 학습(fit) 시키기
    # data 집어넣기
    # epoch
# model.fit(x데이터, y데이터, epochs=10)


## 여기까지 실행시키면 에러 발생
    # 파이썬 리스트를 넣으면 X
    # numpy array , tf tensor
    # 일반 리스트를 numpy array로 변환하기 (그래야 fit에 집어넣기 가능)
    # 넘파이 ? : 파이썬으로 행렬, 벡터를 만들 때 / 리스트안에 리스트를 만들 때 사용

import numpy as np
model.fit( np.array(x데이터), np.array(y데이터), epochs=1000 )


### 그 이후, 예측 ?
    # 테스트해볼 x 데이터
예측값 = model.predict([[750, 3.70, 3], [400, 2.2, 1]])
print(예측값)


### 정리하자면,
    # 모델 만들기
    # 데이터집어넣고 학습
    # 새로운 데이터 예측
    # + 데이터 전처리
    # + 하이퍼 파라미터 튜닝