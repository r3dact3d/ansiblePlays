import pyodbc
import json

server = '{{ sql_server_host }}'
database = '{{ sql_server_database }}'
username = '{{ sql_server_user }}'
password = '{{ sql_server_password }}'

connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

cursor.execute("SELECT hostname, ip_address FROM your_inventory_table")
rows = cursor.fetchall()

inventory = {"all": {"hosts": {}}}
for row in rows:
    inventory["all"]["hosts"][row.hostname] = {"ansible_host": row.ip_address}

print(json.dumps(inventory))
