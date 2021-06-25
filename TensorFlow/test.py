import tensorflow as tf
import numpy as np

# tensor_a = tf.constant("Hello world")
# print(tensor_a)
# print(tensor_a.numpy())
#
# node1 = tf.constant(3.0, tf.float32)
# node2 = tf.constant(4.0) # also tf.float32 implicitly
# node3 = tf.add(node1, node2)
#
# print("node1:", node1, "node2:", node2)
# print("node3: ", node3)

# @tf.function
# def adder(a, b):
#     return a + b
#
# A = tf.constant(1)
# B = tf.constant(2)
# print(tf.add(A, B))
#
# C = tf.constant([1, 2])
# D = tf.constant([3, 4])
# print(adder(C, D))
#
# E = tf.constant([[1, 2, 3], [4, 5, 6]])
# F = tf.constant([[2, 3, 4], [5, 6, 7]])
# print(adder(E, F))

a = tf.constant("Hello world!")
print(a)
print(type(a))
print(a.numpy())
print(type(a.numpy()))