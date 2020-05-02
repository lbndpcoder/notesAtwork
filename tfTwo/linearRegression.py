import numpy as np
import tensorflow as tf

print(tf.__version__)
'''
# 声明固定的参数
a = tf.constant([[1, 2]])
b = tf.constant([[1, 2]])
# 加法运算
c = tf.add(a, b)
print(c)
'''
# 针对性的自动求导数
'''
x = tf.Variable(3.)
with tf.GradientTape() as tape:
    y = tf.square(x)
y_grad = tape.gradient(y, x)
print(y_grad)
'''

# linear regression
# data
X_raw = np.array([2013, 2014, 2015, 2016, 2017], dtype=np.float32)
y_raw = np.array([12000, 14000, 15000, 16500, 17500], dtype=np.float32)
# normalization
X = (X_raw - X_raw.min()) / (X_raw.max() - X_raw.min())
y = (y_raw - y_raw.min()) / (y_raw.max() - y_raw.min())

X = tf.constant(X)
y = tf.constant(y)

a = tf.Variable(0.)
b = tf.Variable(0.)
variables = [a, b]
epoh = 100
# 定义优化函数
optimizers = tf.keras.optimizers.SGD(learning_rate=5e-4)
for e in range(epoh):
    # 定义求导的范围 / 损失函数
    with tf.GradientTape() as tape:
        y_pre = a * X + b
        loss = tf.reduce_sum(tf.square(y_pre - y))
    # 进行求导
    grads = tape.gradient(loss, variables)
    # 优化函数需要导数以及对应的变量
    optimizers.apply_gradients(grads_and_vars=zip(grads, variables))

print(a, b)



