from setup_package.databaseClass import Database
from setup_package.apiClass import Api
from setup_package.mlClass import Model

pullData = False # Modify these values according to setup requirements
createDB = False

# Create the sqlite3 database.
db = Database()
if createDB == True:
    db.create() # Column names are hardcoded. May need to enhance this method.

# Pull data from data.gov.sg, populate database
if pullData == True:
    api = Api(limit=70000)
    data = api.getRecords() # Returns a list of json.
    db.insert(data)

# Train model
model = Model()
model.connect(db)
model.saveDfAsPickle() # For ipynb troubleshooting
if (model.prepData() == True):
    print("Data cleaning and preperation complete")
if (model.trainModel() == True):
    print("Model fitted to pipeline.")
model.getPickle()
