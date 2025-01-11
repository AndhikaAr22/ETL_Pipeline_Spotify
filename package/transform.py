import pandas as pd

class Transformer:
    def __init__(self, album, song, artist):
        self.album = album
        self.song = song
        self.artist = artist

    def get_data_album(self):
        data = self.album
        column_album = ['album_id', 'album_name',  'release_date', 'total_track', 'album_type', 'album_url']

        df_album = pd.DataFrame(data, columns= column_album)
        # transformasi pada kolom release data
        df_album['release_date'] =  df_album['release_date'].apply(
            lambda date: f'{date}-01-01' if len(date) == 4 else date
        )
        # konversi string ke datetime
        df_album['release_date'] =  pd.to_datetime(df_album['release_date'], format='%Y-%m-%d')
        df_album = df_album.drop_duplicates(subset=['album_name'])
        df_album.to_csv('/home/andhika/ETL_pipeline_spotify/data/new_album3.csv', index=False)
        # print('success get data album and ingest data to db')


        return df_album 
    
    def get_data_song(self):
        data = self.song
        column_song = ['song_id', 'song_name',  'popularity', 'duration', 'track_number', 'song_url']

        df_song = pd.DataFrame(data, columns=column_song)
        df_song = df_song.drop_duplicates(subset=['song_name'])
        df_song['duration'] = df_song['duration'] / 60000
        df_song.to_csv('/home/andhika/ETL_pipeline_spotify/data/new_song.csv', index=False)
        print('success get data song and ingest data to db')

        return df_song
    
    def get_data_artist(self):
        data = self.artist
        column_artist = ['artist_id', 'artist_name',  'type',  'artist_url']
        df_artist = pd.DataFrame(data, columns= column_artist)
        df_artist = df_artist.drop_duplicates(subset=['artist_name'])
        df_artist.to_csv('/home/andhika/ETL_pipeline_spotify/data/new_artist.csv', index=False)
        print('success get data artist and ingest data to db')

        return df_artist