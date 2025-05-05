import sqlite3
conn = sqlite3.connect("db/test_data.sqlite")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE)")
conn.commit()
conn.close()

