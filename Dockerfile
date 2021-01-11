FROM apache/airflow
USER root
RUN apt-get update && apt-get install -y libmysqlclient-dev gcc
COPY scripts/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
USER airflow



