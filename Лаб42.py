import sqlite3
conn = sqlite3.connect('Лаб41.sqlite')
cursor = conn.cursor()
cursor.execute("""INSERT INTO users(userid, name, surname, position) 
   VALUES('3', 'Alex', 'Smith', 'working');""")
conn.commit()
conn.close()