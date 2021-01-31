from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import load_model
import cv2
import numpy as np
# to test the service using curl:
# curl -X POST "http://127.0.0.1:8000/predict" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "image=@mnist_sample.jpg;type=image/jpeg"

# create a fastapi app instance.
app = FastAPI()

# load the keras model.
model = load_model('mnist_model.h5')


@app.post("/predict")
# define a form with a multipart input, which will be the image in this case.
async def predict(image: UploadFile = File(...)):
    contents = await image.read()
    with open(f'{image.filename}', 'wb') as f:
        f.write(contents)
    loaded_image = cv2.imread(image.filename, cv2.IMREAD_GRAYSCALE)
    loaded_image = np.expand_dims(loaded_image, axis=0)
    prediction = np.argmax(model.predict(loaded_image))
    return {"label": str(prediction)}
