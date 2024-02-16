import mysql.connector
import os

# Getting my mysql password
mysql_password = os.getenv('MYSQL_PASSWORD')

mysql_connection = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = mysql_password,
  database = 'cripto_infos'
)

cursor = mysql_connection.cursor()

# Creating assets table
assets_table_query = '''
CREATE TABLE assets (
    asset_id varchar(255) PRIMARY KEY,
    asset_symbol varchar(255),
    asset_name varchar(255),
    asset_info_link varchar(255)
);
'''

cursor.execute(assets_table_query)

# Creating infos table
infos_table_query = '''
CREATE TABLE infos (
    asset_id varchar(255) PRIMARY KEY,
    rank_of_day int,
    supply float,
    volume_trading_usd float,
    price float,
    per_price_change float,
    date_d date
);
'''

cursor.execute(infos_table_query)

cursor.close()
mysql_connection.close()
