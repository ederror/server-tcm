#-*- encoding: utf-8 -*-

from flask import jsonify, request, render_template, url_for, redirect
from models import Trash, app, db
import json
import os

import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn
import torch.nn.functional as F

from PIL import Image
from pathlib import Path

app.config['UPLOAD_FOLDER'] = 'C:/Users/Shim/Desktop/Git/server-for-tfm/uploads'

transformations = transforms.Compose([transforms.Resize(256),
                                    transforms.CenterCrop(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
def get_default_device():
    """Pick GPU if available, else CPU"""
    if torch.cuda.is_available():
        return torch.device('cuda')
    else:
        return torch.device('cpu')

def to_device(data, device):
    """Move tensor(s) to chosen device"""
    if isinstance(data, (list,tuple)):
        return [to_device(x, device) for x in data]
    return data.to(device, non_blocking=True)

def predict_image(img):
    # Convert to a batch of 1
    xb = to_device(img.unsqueeze(0), device)
    # Get predictions from model
    yb = model(xb)
    # Pick index with highest probability
    prob, preds  = torch.max(yb, dim=1)
    print(prob,preds)
    # Retrieve the class label
    return classes_dict[str(preds[0].item())]

class OurModel(nn.Module):
    def forward(self, xb):
        return torch.softmax(self.backbone(xb), dim=1)


model = torch.load('_static/resnet50.pt')
model.eval()
classes_dict = json.load(open('_static/trash_class_index.json'))
device = get_default_device()
print(f'current device = {device}')
to_device(model, device)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST']) # POST method만 허용
def predict():
    if request.method == 'POST':
        img_beforeTrans = Image.open(Path('_static/test.jpg'))
        img = transformations(img_beforeTrans)
        class_id, class_name = predict_image(img)

        return jsonify({'class_id': class_id, 'class_name': class_name})

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else: # POST
        print(f'func [search] called.')
        #if request.form["trash_name"]:
        found_trash = Trash.query.filter_by(trash_name=request.form['trash_name']).first()

        return f'tid = {found_trash.tid}, 이름 = {found_trash.trash_name}, 종류 = {found_trash.trash_type}'

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else: # POST
        print(f'func [upload] called.')
        if request.files:
            try:
                os.stat(app.config['UPLOAD_FOLDER'])
            except:
                os.mkdir(app.config['UPLOAD_FOLDER'])
            img = request.files['inputimg']
            print(img, img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'] , img.filename))

            img = transformations(Image.open(os.path.join(app.config['UPLOAD_FOLDER'] , img.filename)))
            class_id, class_name = predict_image(img)
            print(class_id, class_name)
            found_trash = Trash.query.filter_by(trash_name=class_name).first()
            return f'tid = {found_trash.tid}, 이름 = {found_trash.trash_name}, 종류 = {found_trash.trash_type}'
        return redirect(url_for('upload', filename=img.filename))

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port= 3654)
