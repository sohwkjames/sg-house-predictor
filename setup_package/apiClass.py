import requests

class Api():
    def __init__(self, url="", limit=9999):
        # Limit: The number of records to pull from the gov resale housing database.
        # url: URL of the government housing resale database
        #self.url = 'https://data.gov.sg/api/action/datastore_search?resource_id=42ff9cfe-abe5-4b54-beda-c88f9bb438ee'
        self.limit = limit
        self.url = 'https://data.gov.sg/api/action/datastore_search?resource_id=42ff9cfe-abe5-4b54-beda-c88f9bb438ee&limit=' + str(self.limit)
        resp = requests.get(self.url)
        self.json = resp.json()
        
    def getRecords(self):
        # Returns the data as a json.
        return self.json['result']['records']
