from pymongo import MongoClient
from dotenv import load_dotenv
import json
import os
load_dotenv()
    
class Mongodb:
    def __init__(self, database, collection):
        self.mongodb_url = os.getenv('mongodb')
        self.client = MongoClient(self.mongodb_url)
        self.database = self.client[database]
        self.collection = self.database[collection]

    def load_data_to_mongo(self, data):
        try:
            result = self.collection.insert_many(data)
            print(f"Inserted document IDs: {result.inserted_ids}")
        except Exception as e:
            print(f"Error inserting data: {e}")

        self.client.close()
    
    def get_data_mongo(self):
        file_path = '/home/andhika/ETL_pipeline_spotify/data/mongodb_data.json'
        data_mongo = list(self.collection.find())

        for item in data_mongo:
            item['_id'] = str(item['_id'])

        with open(file_path, 'w') as f:
            json.dump(data_mongo, f)
        print(f'berhasil mengambil data mongo dan disimpah di {file_path}')
        