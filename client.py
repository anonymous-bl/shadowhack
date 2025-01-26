import socket
import pymysql

def check_mysql_connection(host, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5)  # Timeout of 5 seconds
        client_socket.connect((host, port))
        client_socket.close()
        return True
    except (socket.timeout, socket.error) as e:
        print(f"Error connecting to MySQL server: {e}")
        return False

def execute_sql_query(query, database):
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database=database  # Specify the database name
        )
        
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)

    except pymysql.MySQLError as e:
        print(f"Error executing query: {e}")

    finally:
        if connection:
            connection.close()

def main():
    host = 'localhost'
    port = 3306  # Default MySQL port

    if check_mysql_connection(host, port):
        print("Connection to MySQL server is open. Executing query...")
        
        # Define your SQL query here
        query = "SELECT * FROM users"
        database = 'dvwa'  # Specify your database name
        execute_sql_query(query, database)
    else:
        print("Unable to connect to MySQL server.")

if __name__ == '__main__':
    main()
