import sqlite3

conn = sqlite3.connect('my_sql.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
conn.commit()
lst = [12, 4, 5, 'py', 'world', 7, 'key', 'spring', 32, 'holiday']
for el in lst:
    if type(el) is str:
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (el,))
        conn.commit()
        d = len(el)
        cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (d,))
        conn.commit()
    elif type(el) is int:
        if el % 2 == 0:
            cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (el,))
            conn.commit()
        else:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', ('нечетное',))
            conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
let = cursor.fetchall()
cursor.execute('''SELECT * FROM tab_2''')
num = cursor.fetchall()
if len(num) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
else:
    cursor.execute('''UPDATE tab_1 SET col_1 = "hello" FROM id = 1''')

cursor.execute('''SELECT*FROM tab_2''')
num = cursor.fetchall()
print(let)
print(num)
