import tensorflow as tf

텐서 = tf.constant([3,4,5])
print(텐서)

# 각각을 곱하고 더하고 하는 과정이 번거로움 -> 행렬(숫자 여러개를 한꺼번에 계산하기 편리)
# 행렬이랑 비슷하게 쓸 수 있는 파이썬 코드 : 텐서
# 텐서가 필요한 이유
    # 숫자 한번에 연산하기 스킬 가능
    # 행렬로 input/w 값 저장 가능
    # 그럼 node 값 계산식이 쉬워진다.
    
텐서 = tf.constant([3,4,5])
텐서2 = tf.constant([6,7,8])
print(텐서 + 텐서2)

# 텐서로 행렬 표현하기
    # tf.add()
    # tf.substract()
    # tf.divide()
    # tf.multiply() : element끼리 곱
    # tf.matmul() : 행렬의 곱(일명, dot product)
텐서3 = tf.constant([[1,2],
                    [3,4]])
텐서4 = tf.constant([[1,2],[3,2],[5,2]])
텐서4

print(tf.matmul(텐서4, 텐서3))
print(tf.multiply(텐서, 텐서2))

# 데이터들을 많이 담고 싶은 데, 뭐를 담을 지 모를 때
    # tf.zeros("모양지정")
텐서5 = tf.zeros([2,2,3]) # 3개의 데이터를 담은 리스트를 하나 생성 -> 그걸 2개 -> 그걸 2개
텐서5

# shape
print(텐서.shape) # 자료가 3개 들어있다.
print(텐서3.shape)

# 텐서의 datatype
    # int : 정수
    # float : 실수(많이 사용)
텐서6 = tf.constant([3.0, 4.0, 5.0])
텐서7 = tf.constant([3,4,5], tf.float32)
print(텐서6, 텐서7)

# 특별한 텐서
    # Variable : weight를 저장하고 싶을 때
    # Variable은 변경이 쉽게 된다. but constant는 고정된 값으로 변경 불가
    # Variable.numpy() : 안에 있는 실제 값을 출력하고 싶을 때
    # Variable.assign() : 변수를 변경하고 싶을 때
    # 물론, 변수에 행렬도 넣을 수 있다.
w = tf.Variable(1.0)
print(w)
print(w.numpy())

w.assign(2.0)
print(w.numpy())
