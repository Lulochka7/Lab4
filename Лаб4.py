import sqlite3
conn = sqlite3.connect('Лаб41.sqlite')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   name TEXT,
   surname TEXT,
   position TEXT);
""")
cursor.execute("""INSERT INTO users(userid, name, surname, position) 
   VALUES('3', 'Alex', 'Smith', 'working');""")
   
more_users = [('1', 'Peter', 'Parker', 'director'), ('2', 'Bruce', 'Wayne', 'accountant')]
cursor.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)

conn.commit()

conn.close()