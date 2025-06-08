# Используем официальный образ Airflow
FROM apache/airflow:2.9.2

# Переключаемся на root для настройки
USER root

# Создаем директории для DAGs и вашего проекта
RUN mkdir -p /opt/airflow/dags /opt/airflow/etl_project

# Возвращаемся к пользователю airflow
USER airflow

# Инициализируем БД, создаем пользователя и запускаем веб-сервер
CMD bash -c "\
  airflow db init && \
  airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com && \
  airflow webserver"