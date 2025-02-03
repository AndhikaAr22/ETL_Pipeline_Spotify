import requests
import base64
import json
from dotenv import load_dotenv

import os
load_dotenv()

# class spotify
class Spotify:
    client_id_spotify = os.getenv('client_id')
    client_secret_spotify = os.getenv('client_secret')
    url_token = os.getenv('url_token')
    def __init__(self,url_param):
        self.url_param = url_param


    def get_token_spotify(self):
        token_url = self.url_token
        credentials = f'{self.client_id_spotify}:{self.client_secret_spotify}'
        base64_credentials = base64.b64encode(credentials.encode()).decode()
        payload = {
            'grant_type':'client_credentials'
        }
        headers = {
            'Authorization': f'Basic {base64_credentials}'
        }

        response = requests.post(token_url, data=payload, headers=headers)

        if response.status_code == 200:
            token_data = response.json()
            token = token_data['access_token']
            # print(f"Token Spotify: ----> {token}")
            return token
        else:
            print(f"Gagal mendapatkan token Spotify. Status Code: {response.status_code}, Response: {response.text}")
            return None

    def get_id_artist(self, token):
        print(f'token untuk ambil id {token}')
        id_artist = []
        name_artist = []
        url = self.url_param
        params = {
            'q': 'genre:"indonesian"',
            'type': 'artist',
            'limit': 50,
            'market': 'ID'
        }
        headers = {
            'Authorization': f'Bearer {token}'  
        }
        response = requests.get(url, params=params, headers=headers)
        search_data = response.json()

        for artist in search_data['artists']['items']:
            artis_name = artist['name']
            artis_id = artist['id']
            name_artist.append(artis_name)
            id_artist.append(artis_id)

        # print("Nama-nama artis dari market Indonesia: ---> sudah ada")
        # print(name_artist)
        # print(f"ID artis dari market Indonesia:---> {id_artist}")
        # print(id_artist)
        return id_artist
    
    def get_all_data(sefl, token, id):
        print(f'token untuk ambil semua data {token}')
        all_source_data = []
        headers = {
            'Authorization': f'Bearer {token}'
        }
        for artist_id in id:
            url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'
            top_track_response = requests.get(url, headers=headers)
            source_data = top_track_response.json()
            all_source_data.append(source_data)
        return all_source_data

# url_param = os.getenv('url_param')
# spotify_intance = Spotify(url_param)
# # token = spotify_intance.get_token_spotify()
# id_name = spotify_intance.get_id_artist()
# data = spotify_intance.get_all_data()