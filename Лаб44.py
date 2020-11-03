import sqlite3
conn = sqlite3.connect('Лаб41.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users;")
three_results = cursor.fetchmany(3)
print(three_results)
conn.commit()
conn.close()