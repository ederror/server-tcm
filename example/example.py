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
    ret = response.json()
    print(ret)

def can(city, ttype):
    uri = url + '/can' + f'?city={city}&trash_type={ttype}'
    response = requests.get(uri)
    ret = response.json()
    for c in ret:
        print(c['detail_addr'])

if __name__ == "__main__":
    #tname = input("input the trash name : ")
    #search(tname)
    #upload()
    can('도봉구', '아이스팩')