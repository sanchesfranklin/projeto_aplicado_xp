import os
from airflow.utils.db import provide_session
from airflow.utils.db import provide_session
from airflow.models import Connection
from dotenv import load_dotenv

load_dotenv()

USER_DATABASE = os.getenv('USER_DATABASE')
PASSWORD_DATABASE = os.getenv('PASSWORD_DATABASE')
PORT_DATABASE = os.getenv('PORT_DATABASE')
DATABASE_NAME = os.getenv('DATABASE_NAME')
HOST_DATABASE = os.getenv('HOST_DATABASE')
DATABASE_CONN_ID_AIRFLOW = os.getenv('DATABASE_CONN_ID_AIRFLOW')

class DBConnectionHandler:
    """Cria uma conexão do Banco de dados Postgresql, para as tasks
    que utilizam alguma interação com o banco precise utilizar.
    """

    def __init__(self) -> None:
        self.create_postgres_connection()


    # criar a conexão com o PostgreSQL
    @provide_session
    def create_postgres_connection(session=None):
        conn = Connection(
            conn_id=DATABASE_CONN_ID_AIRFLOW,
            conn_type='postgres',
            host=HOST_DATABASE,
            schema=DATABASE_NAME,
            login=USER_DATABASE,
            password=PASSWORD_DATABASE,
            port=PORT_DATABASE
        )

        # Verificar se a conexão já existe e evitar duplicação
        existing_conn = session.query(Connection).filter(Connection.conn_id == 'my_postgres_conn').first()
        if not existing_conn:
            session.add(conn)
            session.commit()
