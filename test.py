import sqlite3
db_file = 'paperhearts.db'
cnn = sqlite3.connect(db_file)
cur = cnn.cursor()
tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(tables.fetchall())