import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

load_dotenv()

USER_DATABASE = os.getenv('USER_DATABASE')
PASSWORD_DATABASE = os.getenv('PASSWORD_DATABASE')
PORT_DATABASE = os.getenv('PORT_DATABASE')
DATABASE_NAME = os.getenv('DATABASE_NAME')
HOST_DATABASE = os.getenv('HOST_DATABASE')

class DbConnectionTest:
    def __init__(self) -> None:
        self.connection = None
        self.test_connection()

    def test_connection(self):
        # Parâmetros de conexão
        db_params = {
            'dbname': DATABASE_NAME,
            'user': USER_DATABASE,
            'password': PASSWORD_DATABASE,
            'host': HOST_DATABASE,
            'port': PORT_DATABASE
        }

        try:
            # Estabelecendo a conexão
            self.connection = psycopg2.connect(**db_params)
            cursor = self.connection.cursor()

            # Capturando o valor de uma linha da tabela test
            cursor.execute("SELECT name FROM test;")
            db_value_name = cursor.fetchone()
            print("Conexão bem-sucedida! Versão do PostgreSQL:", db_value_name[0])

        except OperationalError as e:
            print("Erro ao conectar ao PostgreSQL:", e)

        finally:
            # Fechando a conexão
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão fechada.")

if __name__ == "__main__":
    DbConnectionTest()
