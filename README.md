# server-for-tcm
<img src="https://img.shields.io/badge/-Python-000000?style=flat&logo=Python"> <img src="https://img.shields.io/badge/-SQLite-003B57?style=flat&logo=SQLite"> <img src="https://img.shields.io/badge/-Flask-000000?style=flat&logo=Flask"> <img src="https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat&logo=PyTorch">

Flask Rest API Server for Trash Classification Model

## How to use
### Request

```http
POST /upload
inputimg: Imagefile
Content-Type: multipart/form-data
```
| Name | Description |
| ---- | ----------- |
| `inputimg` | 분석하고 싶은 이미지 |
### Response

```json
{
  "tid": 'trash_id',
  "name": '쓰레기이름',
  "type": '분류',
  "howto": '분리배출법',
  "howtoid": '분류id'
}
```
