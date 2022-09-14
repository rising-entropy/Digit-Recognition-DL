from email.mime import image
from statistics import mode
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import base64
import uuid
import os
import numpy as np
import cv2
import PIL

def input_prepare(img):
    img = np.asarray(img)             
    img = cv2.resize(img, (28, 28 ))   
    img = cv2.bitwise_not(img)        
    img = img / 255.0
    img = np.array([img])
    return img 

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
    img = cv2.imread(theImageName)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # gray scaling 
    img = input_prepare(img)
    
    os.remove(theImageName)
    
    model = tf.keras.models.load_model("digit_recognition_model_probability")
    pred = model.predict(img)
    thePredList = pred.tolist()[0]
    print(thePredList)
    for i in range(len(thePredList)):
        thePredList[i] = thePredList[i]*100
    return {"prediction": thePredList}
