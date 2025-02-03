from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_hello():
    print("Hello, Airflow!")

def print_goodbye():
    print("Goodbye, Airflow!")

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

task_hello = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

task_goodbye = PythonOperator(
    task_id='print_goodbye',
    python_callable=print_goodbye,
    dag=dag,
)

task_hello >> task_goodbye
