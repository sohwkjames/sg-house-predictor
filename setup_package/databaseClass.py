import sqlite3

class Database():

    def __init__(self):
        self.connection = None

    def create(self):
        # Creates the mysql .db file in the root folder
        self.connection = sqlite3.connect('house_resale_data.db')
        c = self.connection.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS house_prices
             (_id integer PRIMARY KEY,
              month varchar,
              town varchar,
              flat_type varchar,
              block varchar,
              street_name varchar,
              storey_range varchar,
              floor_area_sqm integer,
              flat_model varchar,
              lease_commence_date dt,
              remaining_lease varchar,
              resale_price integer)''')
              
    def insert(self, data):
        # Takes a json, inserts it into the database
        # data is a list of jsons   

        c = self.connection.cursor()



