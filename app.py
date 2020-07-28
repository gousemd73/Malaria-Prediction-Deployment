
from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import pickle

# Keras
import tensorflow as tf
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.python.keras.backend import set_session
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import pickle
from keras import backend as K



# Flask utils
from flask import Flask, redirect, url_for, request, render_template,jsonify
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer


def model_predict(filepath):
    MODEL_PATH ='model_vgg19.h5'
    model = load_model(MODEL_PATH)
    img = image.load_img(filepath, target_size=(224, 224))
    print(filepath)
    x = image.img_to_array(img)
    x=x/255
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
 
   # with graph.as_default():    
    preds = model.predict(x)
    pred=np.argmax(preds, axis=1)
    print(pred)
    if pred==0:
            return "The Person is Infected With Malaria"
    else:
            return "The Person is not Infected With Malaria"

# Define a flask app
app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = '/uploads'

@app.route('/',methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        f = request.files['inpfile']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        result=model_predict(file_path)
        result = 'Result:'+result
        return render_template('index.html',result=result)
        
        


if __name__ == '__main__':
    app.run()
