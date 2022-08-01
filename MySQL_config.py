from ast import expr_context
import mysql.connector
from mysql.connector import Error
import pandas as pd

class MySQL():

    def __init__(self, host_name, user_name, user_password, db_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name

    def create_server_connection(self):
        connection = None   #encerra as conexões de DB existentes, se existir
        try:
            connection = mysql.connector.connect(
                host = self.host_name,
                user = self.user_name,
                passwd = self.user_password,
                database = self.db_name
            )
            print("Banco de dados MySQL conectado com sucesso!")
        except Error as err:  # erro retornado pelo MySQL
            print(f"Error: {err}")   

        return connection
    
    def execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Sucesso na consulta!")
        except Error as err:
            print(f"Error: {err}")


'''
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Banco de dados criado com sucesso!")
    except Error as err:
        print(f"Error: {err}")
'''





