from airflow.operators.python import PythonOperator

from orquestracao.dag_debug_variables import _print_context


def test_python_operator():

    task = PythonOperator(
        task_id="print_context",
        python_callable=_print_context
    )

    result = task.execute(context={})

    print(result)