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
        return data_mongo
        
    def json_parser(self):
        data = self.get_data_mongo()
        if not data:  # Check if data is empty or None
            print("No data retrieved from MongoDB.")
            return [], [], []

        list_album = []
        list_lagu = []
        list_artis = []

        for item in data:  # Iterating over the list of dictionaries
            if 'tracks' in item:
                for track in item['tracks']:  # Loop through tracks in each item
                    # album
                    album_info = track.get('album', {})
                    id_album = album_info.get('id', '')
                    name_album = album_info.get('name', '')
                    release_date = album_info.get('release_date', '')
                    total_track = album_info.get('total_tracks', 0)
                    album_type = album_info.get('album_type', '')
                    url_album = album_info.get('external_urls', {}).get('spotify', '')

                    album = [id_album, name_album, release_date, total_track, album_type, url_album]
                    list_album.append(album)

                    # song
                    id_song = track.get('id', '')
                    name_song = track.get('name', '')
                    popularity = track.get('popularity', 0)
                    duration = track.get('duration_ms', 0)
                    track_number = track.get('track_number', 0)
                    url_song = track.get('external_urls', {}).get('spotify', '')

                    song = [id_song, name_song, popularity, duration, track_number, url_song]
                    list_lagu.append(song)

                    # artist
                    artist_info = track.get('artists', [])[0] if track.get('artists') else {}
                    id_artist = artist_info.get('id', '')
                    name_artist = artist_info.get('name', '')
                    type_artist = artist_info.get('type', '')
                    url_artist = artist_info.get('external_urls', {}).get('spotify', '')

                    artist = [id_artist, name_artist, type_artist, url_artist]
                    list_artis.append(artist)

        print(f"Albums: {list_album}")
        # print(f"Songs: {list_lagu}")
        # print(f"Artists: {list_artis}")
        return list_album, list_lagu, list_artis
