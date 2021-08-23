#-*- encoding: utf-8 -*-

from flask import Flask, jsonify, request
import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn
import torch.nn.functional as F

from PIL import Image
from pathlib import Path


app = Flask(__name__)

@app.route('/predict', methods=['POST']) # POST method만 허용
def predict():
    if request.method == 'POST':
        img_beforeTrans = Image.open(Path('_static/test.jpg'))
        img = transformations(img_beforeTrans)
        class_id, class_name = predict_image(img)

        return jsonify({'class_id': class_id, 'class_name': class_name})

if __name__ == "__main__":
    app.run()
