# 텐서플로우에서 딥러닝이 어떻게 이루어지는가 ? 
# 딥러닝으로 간단한 수학문제 풀어보기
import tensorflow as tf

# 문제 : 키와 신발 사이즈는 어떤 관련이 있을까 ?
    # 신발 = a * 키 + b
    # a, b를 찾는게 목표
키 = [170, 180, 175, 160]
신발 = [260, 270, 265, 255]

# 데이터 1개만
키 = 170
신발 = 260

a = tf.Variable(0.1)
b = tf.Variable(0.2)

# 경사 하강법 이용
    # optimizers : 경사하강법을 이용해 스스로 변수(weight)들을 업데이트 해주는 함수
    # Adam : gradient를 알아서 스마트하게 바꿔줌
    # opt.minimize(손실함수, var_list=[a,b]) : 경사하강 실행
        # var_list : 경사하강법으로 업데이트 할 weight Variable의 목록
        # loss function 손실함수 만들기 : MSE, Binary cross-entropy 등
        
def 손실함수() : 
    예측값 = 키 * a + b
    return tf.square(260 - 예측값)

opt = tf.keras.optimizers.Adam(learning_rate = 0.1) 

opt.minimize(손실함수, var_list = [a,b])


# 한번이 아니라 여러번 반복해야 함
for i in range(300) : 
    opt.minimize(손실함수, var_list = [a,b])
    print(a.numpy(),b.numpy())
    

