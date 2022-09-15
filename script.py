import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train,y_train), (x_test,y_test) = mnist.load_data()

x_train, x_test = x_train/255.0, x_test/255.0

model = tf.keras.models.Sequential(layers=[
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(512, activation=tf.keras.activations.relu),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(256, activation=tf.keras.activations.sigmoid),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(128, activation=tf.keras.activations.relu),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(64, activation=tf.keras.activations.sigmoid),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Activation(activation=tf.keras.activations.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)

# print(model.evaluate(x_test,y_test))

probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])

model.save('C:/Users/marcus/Desktop/Deep Learning/Digit-Recognition-DL/digit_recognition_model')
probability_model.save('C:/Users/marcus/Desktop/Deep Learning/Digit-Recognition-DL/digit_recognition_model_probability')
