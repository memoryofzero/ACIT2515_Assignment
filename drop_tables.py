import sqlite3

conn = sqlite3.connect('restaurants.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE restaurants
          ''')

conn.commit()
conn.close()
