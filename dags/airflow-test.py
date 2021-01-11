import pandas as pd
import sqlalchemy
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'cimentadaj',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 11, 15, 7),
    'email': ['airflow@example.com'],
    'email_on_failure': True,
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

# Define the main DAG: this is a general
# process that can have many tasks inside
dag = DAG(
    'tutorial',
    default_args=default_args,
    schedule_interval='*/1 * * * *',
)

df = pd.DataFrame({
    'name': 'My name is Pochy'
}, index=[1])

# import pandas as pd
# import sqlalchemy
db_username='test_user'
db_password='123'
db_ip='sql_db'
db_name='test'
db_port=3306
db_connection=sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}?auth_plugin=mysql_native_password'.format(db_username, db_password, db_ip, db_port, db_name))

# Define what task_1 will do
def task_1():
    'Print task 1 complete'
    print('Task 1 complete')

# Define what task_2 will do
def append_data():
    'Append data to test table every minute'
    df.to_sql(
        con=db_connection,
        name="test_table",
        if_exists='append',
        index=False
    )
    print('Task 2 complete')

# Create initial empty task
task0 = DummyOperator(
    task_id='start',
    dag=dag
)

# Create task1
task1 = PythonOperator(
    task_id='task_1',
    python_callable=task_1,
    dag=dag
)

# Create task2
task2 = PythonOperator(
    task_id='append_data',
    python_callable=append_data,
    dag=dag
)

# Create dependencies between tasks.
# task0 is first, then task1 then task2
task0 >> task1 >> task2

