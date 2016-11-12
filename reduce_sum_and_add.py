import tensorflow as tf
matrix1 = tf.constant([[1.,2.,3.]])
matrix2 = tf.constant([[2.,3.,4.]])
x = tf.constant([[1.,2.,3.],[3.,2.,1.]])
matrix3 = tf.constant([[[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]],[[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]]])
with tf.Session() as sess:
# test'+'
#	print(sess.run(matrix1+matrix2))
# test reduce_sum() parameter
	print(sess.run(tf.reduce_sum(matrix3,[0,1,2])))
	print(sess.run(matrix3))
