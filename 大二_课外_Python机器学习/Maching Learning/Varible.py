import tensorflow as tf

start = tf.Variable(0, name='counter')

one = tf.constant(1)

new_value = tf.add(start, one)
update = tf.assign(start, new_value)

init = tf.initialize_all_variables() # Initialize the variables 1

with tf.Session() as sess:
    sess.run(init) # Initialize the variables 2
    for i in range(3):
        sess.run(update) # Run the train process
        print(sess.run(start)) # Everytime print or output a value in tensorflow, you must run it in the session before