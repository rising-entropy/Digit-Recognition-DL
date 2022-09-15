import joblib
import tensorflow as tf

model = tf.keras.models.load_model("digit_recognition_model_probability")
joblib.dump(model, 'digit_recognition_model_probability.pkl')