from airflow import DAG
import airflow
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta


def get_default_args():
    return {
        "start_date": airflow.utils.dates.days_ago(1),
        "retries": 10,
        "retry_delay": timedelta(minutes=1),
        "retry_exponential_backoff": True,
        #"provide_context": True,
    }

dag = DAG(
    dag_id="load_crossref_event_into_bigquery",
    default_args=get_default_args(),
    # schedule_interval='0 0 * * *',
    schedule_interval="@once",
    dagrun_timeout=timedelta(minutes=60),
)

def make_this():
    print("tadsdsdsdsddsd")
    return 

run_this = PythonOperator(
    task_id='print_the_context',
    python_callable=make_this,
    dag=dag,
)


run_this
