#-*- coding: utf-8 -*-
import tensorflow as tf
hello = tf.constant("Hello, tensorflow")
print(hello)
#결과값 : Tensor("Const:0", shape=(), dtype=string)
#이로써 상수나 변수가 아닌 하나의 연산작업.

session = tf.Session()
print(session.run(hello))
#결과 값 : Hello, tensorflow

a = tf.constant(1)
b = tf.constant(2)
print session.run(a+b)
#결과 값 : 3