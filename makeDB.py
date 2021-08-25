import sqlite3

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

con = sqlite3.connect('_static/trash.db')
cur = con.cursor()

try:
    con.execute('CREATE TABLE trash (tid INTEGER, trash_name TEXT, trash_type TEXT, trash_howto_desc TEXT, trash_howto_id INTEGER)')
except Exception as e:
    print(e) # table already exists

cur.executemany('INSERT INTO trash VALUES (?, ?, ?, ?, ?)', buf)
con.commit()

# test
cur.execute('SELECT * FROM trash WHERE tid < 200')
results = cur.fetchall()
for row in results:
    print(row)

con.close()