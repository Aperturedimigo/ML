#-*- coding: utf-8 -*-
import tensorflow as tf
a = tf.placeholder(tf.int64)
b = tf.placeholder(tf.int64)
add = tf.add(a,b)
mul = tf.mul(a,b)

with tf.Session() as session:
    print("add {}".format(session.run(add, feed_dict={a:1, b:2})))
    print("mul {}".format(session.run(mul, feed_dict={a:1, b:2})))