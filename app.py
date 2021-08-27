#-*- encoding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Trash, app, db
import json

import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn
import torch.nn.functional as F

from PIL import Image
from pathlib import Path

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


model = torch.load('_static/resnext50.pt')
model.eval()
classes_dict = json.load(open('_static/trash_class_index.json'))
device = get_default_device()
print(device)
to_device(model, device)

'''
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:/Users/Shim/Desktop/Git/server-for-tfm/_static/trash.db'
db = SQLAlchemy(app)
'''


@app.route('/')
def index():
    return '<HTML><BODY><H1>TRASH IMAGE CLASSIFICATION REST API</H1></BODY></HTML>'

@app.route('/predict', methods=['POST']) # POST method만 허용
def predict():
    if request.method == 'POST':
        img_beforeTrans = Image.open(Path('_static/test.jpg'))
        img = transformations(img_beforeTrans)
        class_id, class_name = predict_image(img)

        return jsonify({'class_id': class_id, 'class_name': class_name})

if __name__ == "__main__":
    db.create_all()
    db.session.add(Trash(tid=1, trash_name='페트병', trash_type='PET', trash_howto_desc='버리는 법', trash_howto_id = 1))
    db.session.commit()
    sometrash = Trash.query.filter_by(tid=1).first()
    print(sometrash)
    app.run()
