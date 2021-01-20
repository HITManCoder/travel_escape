import sqlite3
from pathlib import Path

#db location
db_path = Path(r"C:\Users\Stephen\Python\Travel")
db_file = db_path / "Escape.db"

# Create Database Connections
cnx = sqlite3.connect(db_file)
cur = cnx.cursor()

#cur.execute('DELETE FROM people')
cur.execute('DROP TABLE IF EXISTS people')

cur.execute('''CREATE TABLE IF NOT EXISTS people (
	datetime_txt	TEXT,
	flights	TEXT
	) ''')
#add people in


#cur.execute('''INSERT OR IGNORE INTO people (date, stephen) VALUES (?, ?)''', (yesterday, dealtxt))
#cnx.commit()

#cur.execute('SELECT max, symbol FROM symbols')
