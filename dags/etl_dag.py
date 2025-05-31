from datetime import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
    dag_id="etl_dag",
    start_date=datetime(2025, 5, 30),
    schedule_interval="2 * * * *",
    catchup=False,
) as dag:
    
    run_etl = DockerOperator(
        task_id="run_etl_container",
        image="etl_project:latest",
        command="poetry run python main.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mounts=[
            {
                "Source": "/home/imran/etl_project",
                "Target": "/app",
                "Type": "bind"
            }
        ],
        working_dir="/app",
    )