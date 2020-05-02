import numpy as np
import tensorflow as tf

# 利用tfModel的形式重写线性回归
# data
'''
X = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
y = tf.constant([[10.0], [20.0]])


class linear(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.dense = tf.keras.layers.Dense(
            # 只有一个单元就是说只有一个输出
            units=1,
            # 激活函数无 为线性关系
            activation=None,
            # 参数初始化
            kernel_initializer=tf.zeros_initializer(),
            bias_initializer=tf.zeros_initializer()
        )

    def call(self, input):
        output = self.dense(input)
        return output


model = linear()
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
for i in range(100):
    with tf.GradientTape() as tape:
        y_pre = model(X)
        loss = tf.reduce_sum(tf.square(y_pre - y))
    # 对参数纪进行求导数
    grads = tape.gradient(loss, model.variables)
    optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))
print(model.variables)
'''
