from flask import Flask, jsonify, request, render_template
import json
import sqlite3
import datetime
import urllib.request
import pickle
import numpy as np
import joblib

app = Flask(__name__)

DB_NAME = 'households.db'

@app.route('/')
def displayWelcome():
    # Display a random sample from the database.
    return render_template("guessing_game.html")

@app.route('/game', methods=['POST'])
def welcome():
    # Receive json of house pricing features
    content = request.json

    # Open the RFR model
    path = "../sg_housing_pipe.pkl"
    # Open the pickle
    rfr = joblib.load(path)
    # Transform json into format consumable by sklearn model
    def transform_single_json_for_model(single_json):
        return np.array(list(single_json.values())).reshape(1,-1)
    prediction = float(rfr.predict(transform_single_json_for_model(content)))
    print(prediction)
    return jsonify({"prediction":prediction})


app.run(port=5000, debug=True)
