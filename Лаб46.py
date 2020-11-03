import sqlite3
conn = sqlite3.connect('Лаб41.sqlite')
cursor = conn.cursor()
cursor.execute("DELETE FROM users WHERE surname='Parker';")
conn.commit()
conn.close()