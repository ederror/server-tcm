# server-for-tcm
<img src="https://img.shields.io/badge/-Python-000000?style=flat&logo=Python"> <img src="https://img.shields.io/badge/-SQLite-003B57?style=flat&logo=SQLite"> <img src="https://img.shields.io/badge/-Flask-000000?style=flat&logo=Flask"> <img src="https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat&logo=PyTorch">

Flask Rest API Server for Trash Classification Model

# How to use
## Predict API
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

## Can API
### Request

```http
GET /upload
trash_type: 쓰레기분류(일반쓰레기/폐건전지/폐형광등/아이스팩)
```
| Name | Description |
| ---- | ----------- |
| `trash_type` | 쓰레기분류(일반쓰레기/폐건전지/폐형광등/아이스팩) |
### Response
[Json]
| Name | Description |
| ---- | ----------- |
| `cid` | id |
| `city` | 구 |
| `trash_type` | 쓰레기 분류 |
| `addr` | 주소(도로명주소) |
| `detail_addr` | 상세주소 |
| `latitude` | 위도 |
| `longitude` | 경도 |
