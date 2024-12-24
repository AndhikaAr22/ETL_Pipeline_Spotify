from package.load_data import Mongodb
from package.package_spotify import Spotify
from dotenv import load_dotenv

import os
load_dotenv()


if __name__ == '__main__':
    # # task1
    # url_param = os.getenv('url_param')
    # spotify_instance = Spotify(url_param)
    # token = spotify_instance.get_token_spotify()
    # id_name = spotify_instance.get_id_artist(token)
    # data = spotify_instance.get_all_data(token, id_name)
    # task2
    database = os.getenv('database')
    collection = os.getenv('collection')
    mongodb_instance = Mongodb(database, collection)
    # load_data = mongodb_instance.load_data_to_mongo(data)
    # data_mongodb = mongodb_instance.get_data_mongo()
    data_transform = mongodb_instance.json_parser()