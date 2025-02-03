from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from package.package_mongo import Mongodb
from package.package_spotify import Spotify
from datetime import datetime, timedelta
import json

# mongodb config
mongodb_config = Variable.get("mongodb_config", deserialize_json=True)
mongodb_url = mongodb_config['mongodb_uri']
database_name = mongodb_config['database_name']
collection_name = mongodb_config['collection_name']

# spotify 


# task1
def task1():
    spotify_instance = Spotify()
    token = spotify_instance.get_token_spotify()
    id_name = spotify_instance.get_id_artist(token)
    all_data = spotify_instance.get_all_data(token, id_name)
    mongodb_instance = Mongodb(database_name, collection_name)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 3),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'simple_dag',
    default_args=default_args,
    description='DAG sederhana dengan tugas cetak log',
    schedule_interval=timedelta(days=1),
)

start_task = DummyOperator(
    task_id='start_task',
    dag=dag,
)

end_task = DummyOperator(
    task_id='end_task',
    dag=dag,
)

start_task >> end_task
