import sqlite3
conn = sqlite3.connect('Лаб41.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users;")
one_result = cursor.fetchone()
print(one_result)
conn.commit()
conn.close()