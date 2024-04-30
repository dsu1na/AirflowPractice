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
    dag_id = "my_xcom_sample_dag",
    default_args = default_args,
    schedule = None
)

def task1(**context):
    print("Executing task 1 : Hello World")
    context['ti'].xcom_push(key="task1_push", value="task_2 push from task_1")

def task2(**context):
    print("Executing task 2 ...")
    task2_str = context['ti'].xcom_pull(key="task1_push", task_ids = "task_1")
    print(task2_str)
    print(f"Printing the xcom push : {task2_str}")

task_1 = PythonOperator(
    dag = dag,
    python_callable = task1,
    task_id = "task_1",
    provide_context=True
)

task_2 = PythonOperator(
    dag = dag,
    python_callable = task2,
    task_id = "task_2",
    provide_context = True
)

task_2.set_upstream(task_1)
