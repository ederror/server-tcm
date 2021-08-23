import json
classes = ['나무젓가락', 'cd', '헤어드라이어', '칫솔', '은박보냉백', '영수증', '알약', '아이스팩', '스파우트파우치', '마스크', '고무장갑', '건전지', '유리', '캔', '계란판', '종이', '플라스틱통', 'PET', '드라이버', '플라스틱', '요구르트병', '종이팩', '스프링노트', '상자', 'unknown']
class_dict = {}
classID = 0

for cl in classes:
    class_dict[str(classID)] = [f'T{classID:06}', cl]
    classID += 1
    
f = open("trash_class_index.json", "w")
f.write(json.dumps(class_dict, ensure_ascii = False))
f.close()