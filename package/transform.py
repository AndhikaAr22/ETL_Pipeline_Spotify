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
        # engine = self.postgres_conn.connect()
        # df_album.to_sql('album_table', con=engine, if_exists='replace', index=False)
        df_album.to_csv('/home/andhika/ETL_pipeline_spotify/data/new_album1.csv', index=False)
        # print('success get data album and ingest data to db')


        return df_album 