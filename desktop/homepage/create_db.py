import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(base_dir, 'db', 'contents.db')

conn = sqlite3.connect(base_dir)
curs = conn.cursor()

# curs.execute('CREATE TABLE high_math(id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(15))')
# curs.execute('INSERT INTO high_math(name) values("数と式")')
# curs.execute('INSERT INTO high_math(name) values("図形と計量")')
# curs.execute('INSERT INTO high_math(name) values("二次関数")')
# curs.execute('INSERT INTO high_math(name) values("データ分析")')
# conn.commit()

curs.execute('SELECT name FROM high_math')
a = curs.fetchall()
print(a[0][0])
for i in a:
    print(i[0])

conn.close()
