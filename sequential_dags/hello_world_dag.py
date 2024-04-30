from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# define default arguments
default_args = {
    "owner": "admin",
    "start_date": datetime(2024, 4, 28),
    "retries": 1,
}

# instantiate dag

dag = DAG(
    dag_id = "my_hello_world_dag",
    default_args = default_args,
    schedule = None
)

def task1():
    print("Executinf task 1 : Hello World")

def task2():
    print("Executing task 2 : World Hello")

task_1 = PythonOperator(
    dag = dag,
    python_callable = task1,
    task_id = "task_1"
)

task_2 = PythonOperator(
    dag = dag,
    python_callable = task2,
    task_id = "task_2"
)

task_2.set_upstream(task_1)
