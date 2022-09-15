from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
# import tensorflow as tf
import base64
import uuid
import os
import numpy as np
import cv2
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware


def input_prepare(img):
    img = np.asarray(img)             
    img = cv2.resize(img, (28, 28 ))   
    img = cv2.bitwise_not(img)        
    img = img / 255.0
    img = np.array([img])
    return img 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    image = Image.open(theImageName)
    new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
    new_image.paste(image, (0, 0), image)              # Paste the image on the background. Go to the links given below for details.
    theImageName = theImageName.replace(".png", ".jpeg")
    new_image.convert('RGB').save(theImageName, "JPEG")  # Save as JPEG
    img = cv2.imread(theImageName)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # gray scaling 
    img = input_prepare(img)
    
    os.remove(theImageName)
    os.remove(theImageName.replace(".jpeg", ".png"))
    
    # model = tf.keras.models.load_model("digit_recognition_model_probability")
    model = pickle.load(open('C:/Users/marcus/Desktop/Deep Learning/Digit-Recognition-DL/digit_recognition_model_probability.pkl', 'rb'))
    pred = model.predict(img)
    thePredList = pred.tolist()[0]
    for i in range(len(thePredList)):
        thePredList[i] = thePredList[i]*100
    return {"prediction": thePredList}


if __name__ == '__main__':
    uvicorn.run(app, port=5000)