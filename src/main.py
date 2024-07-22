import database as db

# Driver code
if __name__ == "__main__":
    """
    Please enter the necessary information related to the DB at this place. 
    Please change PW and ROOT based on the configuration of your own system. 
    """
    PW = "admin@123"  # IMPORTANT! Put your MySQL Terminal password here.
    ROOT = "root"
    DB = "ecommerce_record"  # This is the name of the database we will create in the next step - call it whatever
    # you like.
    LOCALHOST = "localhost"
    connection = db.create_server_connection(LOCALHOST, ROOT, PW)

    # creating the schema in the DB
    db.create_and_switch_database(connection, DB, DB)

    # Start implementing your task as mentioned in the problem statement
    # Implement all the test cases and test them by running this file

    # Example: Insert data into the 'users' table
    db.create_insert_query(connection, """
        INSERT INTO users (user_id, user_email, user_name, user_password, user_address, is_vendor)
        VALUES 
        ('1', 'john.doe@example.com', 'John Doe', 'password123', '123 Main St', 0),
        ('2', 'jane.smith@example.com', 'Jane Smith', 'securepass', '456 Oak Ave', 1),
        ('3', 'bob.jones@example.com', 'Bob Jones', 'pass123', NULL, 0);
    """)

    # Example: Insert data into the 'products' table
    db.create_insert_query(connection, """
        INSERT INTO products (product_id, product_name, product_description, vendor_id, product_price, emi_available)
        VALUES 
        ('101', 'Laptop', 'High-performance laptop', '2', 999.99, 'Yes'),
        ('102', 'Smartphone', 'Latest smartphone model', '1', 599.99, 'No'),
        ('103', 'Headphones', 'Noise-canceling headphones', '2', 149.99, 'Yes');
    """)

    # Example: Insert data into the 'orders' table
    db.create_insert_query(connection, """
        INSERT INTO orders (order_id, total_value, customer_id, vendor_id, order_quantity, reward_point)
        VALUES 
        (1, 100.0, '1', '2', 3, 10),
        (2, 150.0, '2', '1', 2, 5);
    """)

    # Example: Read data from the 'orders' table
    records = db.select_query(connection, "SELECT * FROM orders")
    print("Data from 'orders' table:")
    for record in records:
        print(record)
