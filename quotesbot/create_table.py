import psycopg2

# Connection parameters
db_name = "postgres"  # default database
db_user = "postgres"
db_pass = "asdfqwer"
db_host = "localhost"  # assuming you've published the port or you are running this on the machine where the Docker container is running
db_port = "5432"

# Connect to the PostgreSQL server
conn = psycopg2.connect(database=db_name, user=db_user, password=db_pass, host=db_host, port=db_port)

# Create a new cursor
cur = conn.cursor()

# Execute the CREATE TABLE statement
cur.execute("""
    CREATE TABLE items (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        link TEXT NOT NULL
    )
""")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()