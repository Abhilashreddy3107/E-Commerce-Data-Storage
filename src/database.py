import mysql.connector
# Global methods to interact with the Database

# This method establishes the connection with the MySQL
def create_server_connection(host_name, user_name, user_password):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("Server connection established successfully.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# This method will create the database and make it an active database
def create_and_switch_database(connection, db_name, switch_db=True):
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        if switch_db:
            cursor.execute(f"USE {db_name}")
        print(f"Database '{db_name}' created and switched successfully.")

        # Add this part to create 'orders' table with 'order_quantity' column
        create_table(connection, """
            CREATE TABLE IF NOT EXISTS orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                total_value FLOAT,
                customer_id VARCHAR(255),
                vendor_id VARCHAR(255),
                order_quantity INT,
                reward_point INT
            );
        """)

        # Explicitly check and add 'order_quantity' column
        check_and_add_order_quantity_column(connection)
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# This method will establish the connection with the newly created DB
def create_db_connection(host_name, user_name, user_password, db_name):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print(f"Connection to database '{db_name}' established successfully.")

        # Explicitly check and add 'order_quantity' column
        check_and_add_order_quantity_column(connection)

        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# Use this function to create the tables in a database
def create_table(connection, table_creation_statement):
    try:
        cursor = connection.cursor()
        cursor.execute(table_creation_statement)
        print("Table created successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Perform all single insert statments in the specific table through a single function call
def create_insert_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Insert statement executed successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# retrieving the data from the table based on the given query
def select_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# Execute multiple insert statements in a table
def insert_many_records(connection, sql, val):
    try:
        cursor = connection.cursor()
        cursor.executemany(sql, val)
        connection.commit()
        print("Multiple insert statements executed successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Explicitly check and add 'order_quantity' column
def check_and_add_order_quantity_column(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("DESCRIBE orders")
        columns = [column[0] for column in cursor.fetchall()]

        if 'order_quantity' not in columns:
            cursor.execute("ALTER TABLE orders ADD COLUMN order_quantity INT")
            print("Added 'order_quantity' column to 'orders' table.")

        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
