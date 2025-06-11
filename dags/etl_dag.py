from airflow.providers.docker.operators.docker import DockerOperator
from airflow import DAG
from airflow.utils.dates import days_ago
from docker.types import Mount

default_args = {
    'owner': 'airflow',
    'depends_on_past': False}

with DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    description="ETL pipeline using Docker",
    start_date=days_ago(1),            
    schedule_interval="* * * * *",  
    catchup=False,
    tags=["etl"],
) as dag:
    
    run_etl = DockerOperator(
        task_id="run_etl_processing",
        image="etl_project:latest",
        api_version="auto",
        auto_remove=True,
        command='poetry run python main.py',
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        working_dir="/app",
        mount_tmp_dir=False,
        mounts=[
            Mount(
                source="/home/imran/etl_project",
                target="/app",
                type="bind"
            )
        ]
    )