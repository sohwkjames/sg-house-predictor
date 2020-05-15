import sqlite3
import pandas as pd

class Database():

    def __init__(self):
        self.columns = ['_id', 'month', 'town', 'flat_type', 'block', 'street_name',
                        'storey_range', 'floor_area_sqm', 'flat_model', 'lease_commence_date',
                        'remaining_lease', 'resale_price']
        self.dbName = 'house_resale_data.db'
        self.connection = sqlite3.connect(self.dbName)

    def create(self):
        # Creates the mysql .db file in the root folder
        self.connection = sqlite3.connect(self.dbName)
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
        # data is a list of jsons.
        #{'town': 'ANG MO KIO', 'flat_type': '2 ROOM', 'flat_model': 'Improved', 'floor_area_sqm': '44', 'street_name': 'ANG MO KIO AVE 10', 'resale_price': '232000', 'month': '2017-01', 'remaining_lease': '61 years 04 months', 'lease_commence_date': '1979', 'storey_range': '10 TO 12', '_id': 1, 'block': '406'}
        # Create a list of tuples. The order of elements in each tuple should be the same as the columns.
        tupleList = []
        order = self.columns
        for record in data:
            eachTuple = tuple(record[i] for i in order)
            tupleList.append(eachTuple)
        print("Adding {} records to database".format(len(tupleList)))
        insertStatement = 'INSERT or IGNORE INTO house_prices VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
        c = self.connection.cursor()
        c.executemany(insertStatement, tupleList)
        self.connection.commit()

    def getPandasDataFrame(self):
        # Returns a pandas dataframe of all the data in the table.
        query = "SELECT * FROM house_prices"
        df = pd.read_sql(query, self.connection)
        return df
