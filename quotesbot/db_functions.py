import psycopg2

def connect_to_db():
    params = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'asdfqwer',
        'host': 'localhost',
        'port': '5432'
    }
    conn = psycopg2.connect(**params)
    return conn


def create_items_table():

    # Connect to the PostgreSQL server
    conn = connect_to_db()

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

def create_urls_table():

    # Connect to the PostgreSQL server
    conn = connect_to_db()

    # Create a new cursor
    cur = conn.cursor()

    # Execute the CREATE TABLE statement
    cur.execute("""
        CREATE TABLE urls (
            id SERIAL PRIMARY KEY,
            url TEXT NOT NULL,
            crawled_successfully BOOLEAN NOT NULL
        )
    """)

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

def fill_initial_urls_table():
    conn = connect_to_db()
    cur = conn.cursor()
    
    base_url = 'https://www.sreality.cz/en/search/for-sale/apartments?page={page}#z=4'
    urls = [base_url.format(page=i) for i in range(1, 9)]  # Generate URLs for pages 1 to 8


    for url in urls:
        cur.execute("""
        INSERT INTO urls (url, crawled_successfully) VALUES (%s, %s)
        """, (url, False))

    
    conn.commit()
    cur.close()
    conn.close()

def insert_item(item):
    conn = connect_to_db()
    cur = conn.cursor()
    
    insert_query = """
        INSERT INTO items (name, link)
        VALUES (%s, %s);
    """
    
    cur.execute(insert_query, (item['name'], item['link']))
    
    conn.commit()
    cur.close()
    conn.close()

def main():
    fill_initial_urls_table()

if __name__ == "__main__":
    main()