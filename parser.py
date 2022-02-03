import sqlite3

bd = sqlite3.connect("db/gym-bd.db")
cur = bd.cursor()
for i in open("temp.csv").read().split("\n")[1:-1]:
    a, b, c, d = i.split("#")
    res = cur.execute(f"""INSERT INTO 'Программы-Упражнения' VALUES ({a},{b},{c},'{d}')""")
bd.commit()
bd.close()