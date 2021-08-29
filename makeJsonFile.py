import json
classes = [
    '나무젓가락',
    'PET',
    'cd',
    'unknown',
    '건전지',
    '계란판',
    '고무장갑',
    '드라이버',
    '마스크',
    '상자',
    '스파우트파우치',
    '스프링노트',
    '아이스팩',
    '알약',
    '영수증',
    '요구르트병',
    '유리',
    '은박보냉백',
    '종이',
    '종이팩',
    '칫솔',
    '캔',
    '플라스틱',
    '플라스틱통',
    '헤어드라이어']
class_dict = {}
classID = 0

for cl in classes:
    class_dict[str(classID)] = [f'T{classID:06}', cl]
    classID += 1
f = open("_static/trash_class_index.json", "w")
f.write(json.dumps(class_dict, ensure_ascii=False))
f.close()