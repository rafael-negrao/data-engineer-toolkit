from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import is_venv_installed

with DAG(
        dag_id="virtualenv",
        start_date=airflow.utils.dates.days_ago(3),
        schedule_interval="@daily",
) as dag:

    if not is_venv_installed():
        log.warning("A tarefa de exemplo virtalenv_python requer virtualenv, instale-o.")
    else:
        @task.virtualenv(
            task_id="virtualenv_python", requirements=["colorama==0.4.0"], system_site_packages=False
        )
        def callable_virtualenv():
            """
            Exemplo de função que será executada em ambiente virtual.

            Não é garantido que a importaçao do módulo ocorrerá antes da biblioteca ser instalada.
            """
            from time import sleep

            from colorama import Back, Fore, Style

            print(Fore.RED + "some red text")
            print(Back.GREEN + "and with a green background")
            print(Style.DIM + "and in dim text")
            print(Style.RESET_ALL)
            for _ in range(4):
                print(Style.DIM + "Please wait...", flush=True)
                sleep(1)
            print("Finished")

        virtualenv_task = callable_virtualenv()
