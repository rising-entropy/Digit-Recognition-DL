import tensorflow as tf
mnist = tf.keras.datasets.mnist
import numpy as np

(x_train,y_train), (x_test,y_test) = mnist.load_data()

x_train, x_test = x_train/255.0, x_test/255.0

model = tf.keras.models.load_model("digit_recognition_model_probability")
print(model.predict(np.array([x_test[0]])))