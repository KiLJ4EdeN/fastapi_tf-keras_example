# fastapi_tf-keras_example
Minimal model serving in 24 lines of code using fastapi.
A model is trained on the mnist dataset and exposed through a service to provide predictions uploaded on images.


# Usage:

```bash
git clone https://github.com/KiLJ4EdeN/fastapi_tf-keras_example
cd fastapi_tf-keras_example
pip install -r requirements.txt
chmod +x run.sh
./run.sh
```

The service should be running on http://127.0.0.1:8000

output:
```
INFO:     Started server process [3966300]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### Now to test new images we can simply use curl

example input:
<img src="https://github.com/KiLJ4EdeN/fastapi_tf-keras_example/blob/main/mnist_sample.jpg" width="250" height="250">


```bash
curl -X POST "http://127.0.0.1:8000/predict" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "image=@mnist_sample.jpg;type=image/jpeg"
```

output:
```
{"label":"5"}
```

### Or the swagger API provided.
To use swagger refer to http://127.0.0.1:8000/docs

Where the endpoint parameters are shown and we are able to upload new images and test the api.

output:
<img src="https://github.com/KiLJ4EdeN/fastapi_tf-keras_example/blob/main/output.png">



The mnist training code can also be viewed [here](https://github.com/KiLJ4EdeN/fastapi_tf-keras_example/blob/main/mnist.ipynb)
