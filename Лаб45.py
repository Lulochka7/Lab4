import sqlite3
conn = sqlite3.connect('Лаб41.sqlite')
cursor = conn.cursor()
cursor.execute("UPDATE users SET name=? WHERE rowid = 2",["Tane"])
conn.commit()
conn.close()