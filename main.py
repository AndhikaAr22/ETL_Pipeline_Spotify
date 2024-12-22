from load_data import load_data_mongo
from package_spotify import Spotify
from dotenv import load_dotenv

import os
load_dotenv()


if __name__ == '__main__':
    # task1
    url_param = os.getenv('url_param')
    spotify_intance = Spotify(url_param)
    # token = spotify_intance.get_token_spotify()
    id_name = spotify_intance.get_id_artist()
    data = spotify_intance.get_all_data()
    # task2
    load_data = load_data_mongo(data)