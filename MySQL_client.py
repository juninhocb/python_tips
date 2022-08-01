from MySQL_config import MySQL as sql
from MySQL_tables import *
from MySQL_data import *

host = "localhost"
username = "root"
password = "p@lmeiras2"
data_base = "pessoa"


sql_manager = sql(host, username, password, data_base)
connection = sql_manager.create_server_connection()
sql_manager.execute_query(connection, create_pessoa_table) 
sql_manager.execute_query(connection, create_client_table)
sql_manager.execute_query(connection, create_participant_table)
sql_manager.execute_query(connection, create_course_table)
sql_manager.execute_query(connection, alter_participant)
sql_manager.execute_query(connection, alter_course)
sql_manager.execute_query(connection, alter_course_again)
sql_manager.execute_query(connection, create_takescourse_table)
sql_manager.execute_query(connection, pop_pessoa)
sql_manager.execute_query(connection, pop_participant)
sql_manager.execute_query(connection, pop_course)
sql_manager.execute_query(connection, pop_takescourse)


