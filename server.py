from statistics import mode
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import base64
import uuid
import os
import numpy as np
import cv2

app = FastAPI()

class ImagePayload(BaseModel):
    image: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/recognize-digit")
async def recognizeDigit(imagePayload: ImagePayload):

    # Load Image
    theImageName = str(uuid.uuid4())+".png"
    imgData = base64.b64decode(imagePayload.image)
    with open(theImageName, "wb") as fh:
        fh.write(imgData)
    image_loaded = tf.keras.preprocessing.image.load_img(theImageName)
    image_array  = tf.keras.preprocessing.image.img_to_array(image_loaded)
    image_array = tf.image.rgb_to_grayscale(image_array)
    image_array = tf.image.resize(
        image_array,
        (28,28),
    )
    image_array /= 255.0
    os.remove(theImageName)

    print(image_array)

    
    # Load the Model
    model = tf.keras.models.load_model("digit_recognition_model")

    # Predict the outcome
    prediction = model.predict(image_array, batch_size=1)
    print(prediction)


    return {"item_name": "image_array"}
