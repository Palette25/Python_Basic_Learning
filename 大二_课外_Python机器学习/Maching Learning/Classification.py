import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# layer adder
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
    biase = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
    Wx_plus_b = tf.matmul(inputs, Weights) + biase
    if activation_function == None:
        result = Wx_plus_b
    else:
        result = activation_function(Wx_plus_b)
    return result

# define accuracy function
def compute_accuracy(x, y):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: x})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs:x, ys:y})
    return result

# define placeholder for input
xs = tf.placeholder(tf.float32, [None, 784]) # 28*28
ys = tf.placeholder(tf.float32, [None, 10])

# add output layer
prediction = add_layer(xs, 784, 10, activation_function=tf.nn.softmax)

# The error distance between prediction and real data
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
                                              reduction_indices=[1])) # loss
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Now we get to run the network
init = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    for step in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={xs: batch_xs, ys:batch_ys})
        if step % 10 == 0:
            print(compute_accuracy(mnist.test.images,
                                   mnist.test.labels))