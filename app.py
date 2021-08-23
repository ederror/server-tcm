#-*- encoding: utf-8 -*-

from flask import Flask, jsonify, request
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
#classes = ['나무젓가락', 'cd', '헤어드라이어', '칫솔', '은박보냉백', '영수증', '알약', '아이스팩', '스파우트파우치', '마스크', '고무장갑', '건전지', '유리', '캔', '계란판', '종이', '플라스틱통', 'PET', '드라이버', '플라스틱', '요구르트병', '종이팩', '스프링노트', '상자', 'unknown']
classes_dict = json.load(open('_static/trash_class_index.json'))
device = get_default_device()
print(device)
to_device(model, device)

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
