import sqlite3

conn = sqlite3.connect('restaurants.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE restaurants
          (id INTEGER PRIMARY KEY ASC,
           name VARCHAR(100) NOT NULL,
           num_employees INTEGER NOT NULL,
           location VARCHAR(100) NOT NULL,
           year_opened INTEGER NOT NULL,
           restaurant_type VARCHAR(15) NOT NULL,
           num_locations INTEGER,
           has_drivethrough INTEGER,
           num_michelin_stars INTEGER,
           chef_name VARCHAR(100))
          ''')

conn.commit()
conn.close()
