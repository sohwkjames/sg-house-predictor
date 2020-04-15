import requests

class Api():
    def __init__(self, url=""):
        # When we initialize the api object, request data from data.gov.sg api.
        self.url = 'https://data.gov.sg/api/action/datastore_search?resource_id=42ff9cfe-abe5-4b54-beda-c88f9bb438ee'
        resp = requests.get(self.url)
        self.json = resp.json()
        
    def getRecords(self):
        # Returns the data as a json
        return self.json['result']['records']

