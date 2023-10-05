import airflow.utils.dates
from airflow import DAG
from airflow.operators.python import PythonOperator

import logging

def _print_context(**kwargs):
    logging.info(f"kwargs = {kwargs}")
    return kwargs


with DAG(
        dag_id="debug_variables",
        start_date=airflow.utils.dates.days_ago(3),
        schedule_interval="@daily",
) as dag:
    PythonOperator(
        task_id="print_context",
        python_callable=_print_context
    )

