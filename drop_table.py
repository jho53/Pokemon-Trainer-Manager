import sqlite3

conn = sqlite3.connect('trainers.sqlite')

c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS trainer''')

conn.commit()
conn.close()
