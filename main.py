from dags.package.package_mongo import Mongodb
from dags.package.package_spotify import Spotify
from dags.package.transform import Transformer
from dotenv import load_dotenv

import os
load_dotenv()


if __name__ == '__main__':
    database = os.getenv('database')
    collection = os.getenv('collection')
    # task1
    url_param = os.getenv('url_param')
    spotify_instance = Spotify(url_param)
    token = spotify_instance.get_token_spotify()
    id_name = spotify_instance.get_id_artist(token)
    data = spotify_instance.get_all_data(token, id_name)
    mongodb_instance = Mongodb(database, collection)
    load_data = mongodb_instance.load_data_to_mongo(data)
    # task2
    data_mongodb = mongodb_instance.get_data_mongo()
    list_album, list_song, list_artist = mongodb_instance.json_parser()
    transform = Transformer(list_album, list_song, list_artist)
    data_album = transform.get_data_album()
    data_lagu = transform.get_data_song()
    data_artis = transform.get_data_artist()
    # task3
    # load data to bigquery 