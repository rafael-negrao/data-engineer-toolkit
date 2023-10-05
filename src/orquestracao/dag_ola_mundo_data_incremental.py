from datetime import datetime
from pathlib import Path

import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator

#
def _calculate_stats(input_path, output_path):
    """Calculates event statistics."""

    events = pd.read_json(input_path)
    stats = events.groupby(["date", "user"]).size().reset_index()

    Path(output_path).parent.mkdir(exist_ok=True)
    stats.to_csv(output_path, index=False)


# Uma DAG representa um workflow, um conjunto de task
with DAG(
        dag_id="ola_mundo_data_incremental",  # nome da DAG
        start_date=datetime(2023, 10, 1),  # A data em que o DAG deve começar a funcionar pela primeira vez
        end_date=datetime(2023, 10, 5),  # A data em que o DAG deve encerrar o funcionamento
        schedule_interval="@daily"  # timedelta oferece a capacidade de usar programações baseadas em frequência.
) as dag:

    calculate_stats = PythonOperator(
        task_id="calculate_stats",
        python_callable=_calculate_stats,
        op_kwargs={
            "input_path": "/opt/airflow/data/events/{{ ds }}/events.json",
            "output_path": "/opt/airflow/data/stats/{{ ds }}/stats.csv"}
    )

    
