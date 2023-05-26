# Execute a database query using the PostgreSQL database in Python

This script demonstrates how to execute a database query using the PostgreSQL database and the psycopg2 library.

The execute_postgresql_query function takes five parameters: host (the database server hostname or IP address), database (the name of the database to connect to), user (the username for the database connection), password (the password for the database connection), and query (the SQL query to execute).
Inside the function, we connect to the PostgreSQL database using psycopg2.connect(), passing the host, database, user, and password parameters.
We create a cursor object using connection.cursor() to execute SQL commands and fetch results.
The query is executed using cursor.execute(query), where query is the SQL query provided as a parameter to the function.
We fetch the results using cursor.fetchall(), which returns all the rows returned by the query.
Finally, we iterate over the rows and print them.
The connection is closed using connection.close() to release the resources.
