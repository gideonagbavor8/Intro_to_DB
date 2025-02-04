import mysql.connector
from mysql.connector import errorcode

# Database connection details
config = {
    'user': 'root',
    'password': '05545Komla@47692@',
    'host': '127.0.0.1'
}

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

# Connect to MySQL server
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    print("Successfully connected to MySQL server.")

    # Create the database
    create_database(cursor)

    # Close cursor and connection
    cursor.close()
    cnx.close()
    print("Closed connection to MySQL server.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
