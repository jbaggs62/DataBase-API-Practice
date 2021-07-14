import mysql.connector
from mysql.connector import Error



#mycursor.execute("CREATE DATABASE vaccineDB")
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )
    if connection.is_connected():
        db_info=connection.get_server_info()
        print("connected to mysql Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS vaccineDB;")
        record = cursor.fetchone()
        print("You're connect to the databse", record)


except Error as e:
    print("Error while create", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Mysql connection is closed")