from google.cloud import bigquery

class LoadData:
    client = bigquery.Client.from_service_account_json('', project='project-bq-satu')
    
    def __init__(self, df_album, df_song, df_artist):
        self.df_album = df_album
        self.df_song = df_song
        self.df_artist = df_artist    

        def load_data_album(self):
            transform_album = self.df_album
            table_id = "project-bq-satu.spotify_data.album_data"
            # save schema into variable in airflow 
            schema = [
                bigquery.SchemaField("album_id", "STRING", "NULLABLE"),
                bigquery.SchemaField("album_name", "STRING", "NULLABLE"),
                bigquery.SchemaField("release_date", "DATE", "NULLABLE"),
                bigquery.SchemaField("total_track", "INTEGER", "NULLABLE"),
                bigquery.SchemaField("album_type", "STRING", "NULLABLE"),
                bigquery.SchemaField("album_url", "STRING", "NULLABLE")
            ]
            try:
                job_config = bigquery.LoadJobConfig(
                    schema=schema, 
                    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE)
                job = self.client.load_table_from_dataframe(transform_album, table_id, job_config=job_config)
                # Menunggu hingga job selesai
                job.result()

                print("sukses load data album ke BigQuery.")
            except Exception as e:
                print("Terjadi kesalahan saat memuat data ke BigQuery:", str(e))
        
    
    # load data album to bigquery
    def load_data_artist(self):
        transform_artist = self.df_artist
        table_id = "project-bq-satu.spotify_data.artist_data"
        # save schema into variable in airflow 
        schema = [
            bigquery.SchemaField("artist_id", "STRING", "NULLABLE"),
            bigquery.SchemaField("artist_name", "STRING", "NULLABLE"),
            bigquery.SchemaField("type", "STRING", "NULLABLE"),
            bigquery.SchemaField("artist_url", "STRING", "NULLABLE")
        ]
        try:
            job_config = bigquery.LoadJobConfig(
                schema=schema, 
                write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE)
            job = self.client.load_table_from_dataframe(transform_artist, table_id, job_config=job_config)
            # Menunggu hingga job selesai
            job.result()

            print("sukses load data artis ke BigQuery.")
        except Exception as e:
            print("Terjadi kesalahan saat memuat data ke BigQuery:", str(e))
        
    
    # load data album to bigquery
    def load_data_song(self):
        transform_song = self.df_song
        table_id = "project-bq-satu.spotify_data.song_data"
        # save schema into variable in airflow 

        schema = [
            bigquery.SchemaField("song_id", "STRING", "NULLABLE"),
            bigquery.SchemaField("song_name", "STRING", "NULLABLE"),
            bigquery.SchemaField("popularity", "INTEGER", "NULLABLE"),
            bigquery.SchemaField("duration", "FLOAT", "NULLABLE"),
            bigquery.SchemaField("track_number", "INTEGER", "NULLABLE"),
            bigquery.SchemaField("song_url", "STRING", "NULLABLE")
        ]
        try:
            job_config = bigquery.LoadJobConfig(
                schema=schema, 
                write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE)
            job = self.client.load_table_from_dataframe(transform_song, table_id, job_config=job_config)
            # Menunggu hingga job selesai
            job.result()

            print("sukses load data lagu ke BigQuery.")
        except Exception as e:
            print("Terjadi kesalahan saat memuat data ke BigQuery:", str(e))
