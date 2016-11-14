import tensorflow as tf
#creation
#weights = tf.Variable(tf.random_normal([4,5],stddev=0.35),name="weights")
biases = tf.Variable(tf.zeros([5]),name="biases")
saved_weights = tf.Variable(tf.random_normal([4,5],stddev=0.35),name="saved_weights")
#initialzation from another Varibale
#w2 = tf.Variable(weights.initialized_value(),name="w2")
#w_twice = tf.Variable(weights.initialized_value()*2,name="w_twice")

#custom initialization
cus_init = tf.initialize_variables([biases])

#initialzation
init_op = tf.initialize_all_variables()

#saving and restoring {"saved_weights":weights}
saver = tf.train.Saver({"saved_weights":saved_weights})

#save path "/home/yuzongfu/TFwithPY3.4/saving_wei_and_bias.ckpt

with tf.Session() as sess:
	#sess.run(init_op)
	
#restore
	
	saver.restore(sess,"/home/yuzongfu/TFwithPY3.4/saving_weights.ckpt")
	sess.run(cus_init)

	print(sess.run(saved_weights))
	print(sess.run(biases))
#save
	#save_path = saver.save(sess,"/home/yuzongfu/TFwithPY3.4/saving_wei_and_bias.ckpt")
	#print("saved in file:%s" %(save_path))
	#save_weights_path = saver.save(sess,"/home/yuzongfu/TFwithPY3.4/saving_weights.ckpt")
	#print(sess.run(w2))
	#print(sess.run(w_twice))
