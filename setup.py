from setup_package.databaseClass import Database
from setup_package.apiClass import Api

# Create the database. 
db = Database()
db.create() # Column names are hardcoded. May need to enhance this method.
#print("Database successfully created")

# Pull data from data.gov.sg, populate database
api = Api()
data = api.getRecords() # Returns a list of json.
#print("data pulled from data.gov api")
print("Testing db.insert()")
db.insert(data)
#print("Data successfully inserted into database")

# Create predictions
#model = Model()
#model.connect(db)
#model.createTrainedPickle()  # makes 
