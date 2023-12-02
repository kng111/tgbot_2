import sqlite3


db = sqlite3.connect('DR_Koll.db')
cur = db.cursor()

cur.execute('''CREATE TABLE table1 (
id INTEGER PRIMARY KEY,
imy TEXT NOT NULL,
fam TEXT NOT NULL,
otch TEXT NOT NULL,
doljn TEXT NOT NULL,
dr TEXT NOT NULL
)''')