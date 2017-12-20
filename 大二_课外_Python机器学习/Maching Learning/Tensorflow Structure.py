import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.3 + 0.1

# create tensorflow structure start #

# Will be trained to be closer to 0.3, firstly set to be in range (-1.0, 1.0)
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

# Will be trained to be closer to 0.1, firstly set to be 0
biases = tf.Variable(tf.zeros([1]))

# The expression that we get after machine training
y = x_data * Weights + biases

# Steps that try to minimize the loss in the process
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

# create tensorflow structure end #

# Run the tensorflow

with tf.Session() as sess:
    sess.run(init)
    for step in range(201):
        sess.run(train)
        if step % 10 == 0:
            print(step, sess.run(Weights), sess.run(biases))