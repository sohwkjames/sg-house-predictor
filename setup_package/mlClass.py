import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib

class Model():

    def __init__(self):
        ## Attributes
        self.df = None    # Holds the entire df in memory.
        self.pipeline = None    # Holds a sklearn pipeline object.
        self.cleaned_columns_X = None
        print("Initialised model object")



    def connect(self, db):
        # Sets df as the database object.
        self.df = db.getPandasDataFrame()

    def saveDfAsPickle(self):
        self.df.to_pickle("./data.pkl")



    def prepData(self):

        def year_to_month(s):
            # Converts input of format "xx years yy months" or "xx years" into a month integer
            splitted = s.split()
            # Data is in format "xx years yy months" or "xx years"
            months = 0
            if len(splitted) >= 4:  # Handle the format "xx years yy months"
                months += int(splitted[0]) * 12 #
                months += int(splitted[2])
            else:
                months += int(splitted[0]) * 12

            return months

        def storey_range(s):
            # converts input of format "xx to xx" to the average of the 2 numbers.
            splitted = s.split()
            val1 = int(splitted[0])
            val2 = int(splitted[2])
            avg_val = (val1 + val2) / 2
            return avg_val

        def flat_type_to_integer(s):
            # Map flat_type to integer to reduce dimensions when get_dummies.
            mapping = {"1 ROOM":1, "2 ROOM":2, "3 ROOM":3,
                       "4 ROOM":4, "5 ROOM": 5, "EXECUTIVE":6, "MULTI-GENERATION":7}
            if s not in mapping:
                return 0
            return mapping[s]

        def getdummy_inplace(local_df):
            local_df = pd.concat([local_df,
                                    pd.get_dummies(local_df.select_dtypes(exclude=['number', 'datetime']))], axis=1)
            cols_to_drop = local_df.select_dtypes(exclude=['number', 'datetime']).columns
            local_df.drop(columns=cols_to_drop, inplace=True)
            return local_df

        # _id: set it as index.
        self.df.set_index("_id", inplace=True)
        # month: change this to a float, representing year of transacation.
        self.df['month'] = pd.to_datetime(self.df['month'])
        self.df['month'] = self.df['month'].dt.year
        self.df.rename(columns={'month':'year_of_sale'}, inplace=True)
        # street_name: Drop if we have town...
        self.df.drop(columns="street_name", inplace=True)
        # storey range: Take middle of the storey range
        self.df['storey_range'] = self.df['storey_range'].apply(storey_range)
        #lease commence date: Can drop if we have remaining lease?
        self.df.drop(columns="lease_commence_date", inplace=True)
        # flat model: drop
        self.df.drop(columns="flat_model", inplace=True)
        # remaining lease: convert to months (integer)
        self.df['remaining_lease'] = self.df['remaining_lease'].apply(year_to_month)
        # block: does it contain any useful information? No.
        self.df.drop(columns="block",inplace=True)
        # flat type: map to integers.
        self.df['flat_type'] = self.df['flat_type'].apply(flat_type_to_integer)
        # get dummy cols.
        self.df = getdummy_inplace(self.df)
        # Bring resale_price to last col
        self.df.insert(len(self.df.columns), 'resale_price_tmp', self.df['resale_price'])
        self.df.drop(columns='resale_price',inplace=True)
        self.df.rename(columns={'resale_price_tmp':'resale_price'})
        return True

    def trainModel(self):
        rfr = RandomForestRegressor()
        X = self.df.iloc[:,:-1]
        y = self.df.iloc[:,-1]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
        pipe = Pipeline([('scalar', StandardScaler()),('rfr',rfr)])
        pipe.fit(X_train, y_train)
        self.pipeline = pipe
        return True

    def saveModelAsPickle(self):
        joblib.dump(self.pipeline, 'sg_housing_pipe.pkl')
        return True

    def saveCleanedDataAsPickle(self):
        '''Call this method after cleaning data to generate a picle of DF.
        Pickled DF can be used for reference for creating inputs for prediction.'''
        joblib.dump(self.df, 'cleaned_data.pkl')
        return True
