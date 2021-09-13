# server_for_tcm
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
  "tid": 'trash id',
  "trash_name": '쓰레기이름',
  "trash_type": '분류'
}
```
