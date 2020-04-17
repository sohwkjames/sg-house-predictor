from setup_package.databaseClass import Database
from setup_package.apiClass import Api

# Create the sqlite3 database. 
db = Database()
db.create() # Column names are hardcoded. May need to enhance this method.

# Pull data from data.gov.sg, populate database
api = Api(limit=70000)
data = api.getRecords() # Returns a list of json.

db.insert(data)


# Create predictions
#model = Model()
#model.connect(db)
#model.createTrainedPickle()  # makes 
