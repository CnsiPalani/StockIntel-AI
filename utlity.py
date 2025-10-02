import mysql.connector

def get_connection():
    """
    Establishes and returns a connection to the MySQL database.

    Attempts to connect to a MySQL database using the specified host, user, password, and database name.
    If the connection is successful, returns the connection object.
    If an error occurs during connection, prints the error and returns None.

    Returns:
        mysql.connector.connection.MySQLConnection or None: The database connection object if successful, otherwise None.
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@99",
            database="stockintel_ai"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_connection(conn):
    """
    Closes the given MySQL database connection.

    Args:
        conn (mysql.connector.connection.MySQLConnection): The database connection object to be closed.
    """
    if conn:
        conn.close()
        print("Database connection closed.")
    else:
        print("No connection to close.")

import mysql.connector

def execute_query(query, params=None):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            if query.strip().lower().startswith("select"):
                result = cursor.fetchall()  # Fetch all results
            else:
                conn.commit()
                result = None
        except Exception as e:
            print(f"Error executing query: {e}")
            result = None
        finally:
            cursor.close()  # Always close the cursor
            close_connection(conn)
        return result
    return None


# Insert bulk data
def insert_bulk_data(table, data_list):
    """
    Inserts multiple rows of data into a specified table in the MySQL database.

    Constructs an INSERT SQL query based on the provided table name and a list of data dictionaries,
    then executes the query using the execute_query function.

    Args:
        table (str): The name of the table where data will be inserted.
        data_list (list): A list of dictionaries, each containing column-value pairs to be inserted into the table.
    """
    if not data_list:
        print("No data provided for bulk insert.")
        return

    placeholders = ', '.join(['%s'] * len(data_list[0]))
    columns = ', '.join(data_list[0].keys())
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        try:
            values = [tuple(data.values()) for data in data_list]
            cursor.executemany(sql, values)
            conn.commit()
            print(f"{cursor.rowcount} rows inserted successfully.")
        except Exception as e:
            print("Error executing bulk insert:", e)
        finally:
            cursor.close()
            close_connection(conn)  

 