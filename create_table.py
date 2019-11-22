import sqlite3

conn = sqlite3.connect('trainers.sqlite')

c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS trainer(
    trainer_id INTEGER PRIMARY KEY ASC,
    name VARCHAR(60) NOT NULL,
    pokemon_team VARCHAR(180) NOT NULL,
    trainer_class VARCHAR(60) NOT NULL,
    type VARCHAR(20) NOT NULL,
    pokecoins INTEGER NOT NULL,
    location VARCHAR(60) NOT NULL,
    movement_type VARCHAR(10),
    phone_num INTEGER,
    have_partner INTEGER,
    badge VARCHAR(20),
    element VARCHAR(20),
    prize VARCHAR(20)
    );
''')

conn.commit()
conn.close()
