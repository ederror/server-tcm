import sqlite3

con = sqlite3.connect('_static/trash.db')
cur = con.cursor()

try:
    con.execute('CREATE TABLE trash (tid INTEGER, trash_name TEXT, trash_type TEXT, trash_howto_desc TEXT, trash_howto_id INTEGER)')
except Exception as e:
    print(e) # table already exists

buf = []
with open("_static/trash_data.csv", "r", encoding="UTF8") as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.strip()
        token = line.split(",")
        try:
            buf.append((token[1], token[0], token[2], token[3], token[4]))
        except:
            continue

cur.executemany('INSERT INTO trash VALUES (?, ?, ?, ?, ?)', buf)
con.commit()

# Garbage Can
try:
    con.execute('CREATE TABLE can (cid INTEGER, city TEXT, trash_type TEXT, addr TEXT, detail_addr TEXT, latitude FLOAT, longitude FLOAT)')
except Exception as e:
    print(e) # table already exists

cid = 1
def parse(filename):
    global cid
    buf = []
    with open(filename, "r", encoding="UTF8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            token = line.split(",")
            try:
                buf.append([cid, token[1], token[2], token[3], token[4], float(token[5]), float(token[6]) ])
                cid += 1
            except:
                continue
    cur.executemany('INSERT INTO can VALUES (?, ?, ?, ?, ?, ?, ?)', buf)
    con.commit()

parse("_static/가로쓰레기통.csv")
parse("_static/아이스팩.csv")
parse("_static/폐형관등_건전지.csv")

# test
cur.execute('SELECT * FROM trash WHERE tid < 200')
results = cur.fetchall()
for row in results:
    print(row)

con.close()