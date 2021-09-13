import requests
import os

url = 'http://localhost:3654'

def search(trash_name):
    uri = url + '/search'
    response = requests.post(uri, data= {'trash_name': trash_name})
    print(response.text)

def upload():
    uri = url + '/upload'
    img = open('test.jpg', 'rb')
    response = requests.post(uri, files= {'inputimg': ('uploadimg.jpg', img, 'multipart/form-data')})
    print(response.text)

if __name__ == "__main__":
    tname = input("input the trash name : ")
    search(tname)
    upload()