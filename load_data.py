from pymongo import MongoClient, InsertOne
import json
import pandas as pd
from package_spotify import Spotify
from dotenv import load_dotenv

import os
load_dotenv()


mongodb = os.getenv('mongodb')
client = MongoClient(mongodb)
database = client['spotify']
collection = database['spotify_data']

def load_data_mongo(data):
    try:
        result = collection.insert_many(data)
        print(f"Inserted document IDs: {result.inserted_ids}")
    except Exception as e:
        print(f"Error inserting data: {e}")

    client.close()
    