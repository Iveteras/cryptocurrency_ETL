import mysql.connector
import os

# Getting my mysql password
mysql_password = os.getenv('MYSQL_PASSWORD')

mysql_connection = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = mysql_password
)

cursor = mysql_connection.cursor()

# Creating the database
db_name = "cripto_infos"
cursor.execute(f"CREATE DATABASE {db_name}")

cursor.close()
mysql_connection.close()