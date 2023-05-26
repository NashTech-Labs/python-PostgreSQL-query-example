import psycopg2

def execute_postgresql_query(host, database, user, password, query):
    try:
        # Connect to the database
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        # Execute the query
        cursor = connection.cursor()
        cursor.execute(query)

        # Fetch and print the results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Close the connection
        connection.close()

    except Exception as e:
        print(f"An error occurred while executing the database query: {e}")

# Example usage
db_host = "localhost"
db_database = "mydatabase"
db_user = "myuser"
db_password = "mypassword"
db_query = "SELECT * FROM employees"
execute_postgresql_query(db_host, db_database, db_user, db_password, db_query)

