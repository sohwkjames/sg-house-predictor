
## This script should test all the endpoints by sending requests/json payloads.
# This successfully sends a json payload.
import requests
import joblib

# What json does the endpoint expect?
def generate_json(include_y=False):
    sample_json = {'year_of_sale': 2018, 'flat_type': 3, 'storey_range': 2.0,
                'floor_area_sqm': 120.0, 'remaining_lease': 809,
                'town_ANG MO KIO': 0, 'town_BEDOK': 1, 'town_BISHAN': 0,
                'town_BUKIT BATOK': 1, 'town_BUKIT MERAH': 0, 'town_BUKIT PANJANG': 0,
                'town_BUKIT TIMAH': 0, 'town_CENTRAL AREA': 0, 'town_CHOA CHU KANG': 0,
                'town_CLEMENTI': 0, 'town_GEYLANG': 0, 'town_HOUGANG': 0, 'town_JURONG EAST': 0,
                'town_JURONG WEST': 0, 'town_KALLANG/WHAMPOA': 0, 'town_MARINE PARADE': 0,
                'town_PASIR RIS': 0, 'town_PUNGGOL': 0, 'town_QUEENSTOWN': 0, 'town_SEMBAWANG': 0,
                'town_SENGKANG': 0, 'town_SERANGOON': 0, 'town_TAMPINES': 0,
                'town_TOA PAYOH': 0, 'town_WOODLANDS': 0, 'town_YISHUN': 0}
    if include_y:
        sample_json['resale_price_tmp'] = 320000.0
    return sample_json

sample_json = generate_json()

url = "http://127.0.0.1:5000/game"
r = requests.post(url, json=sample_json)
#print(r.status_code)




# Test opening the pickled file
#path = "../sg_housing_pipe.pkl"
# Open the pickle
#rfr = joblib.load(path)

#cleaned_data = joblib.load("../cleaned_data.pkl")
#print(cleaned_data.columns)
#print(rfr.predict())
