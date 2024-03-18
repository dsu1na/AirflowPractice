airflow db init
airflow users create --username admin --firstname Toni --lastname Kutta --role Admin --email tonikutta@gmail.com
aiflow webserver -p 8080 --daemon
airflow scheduler --daemon