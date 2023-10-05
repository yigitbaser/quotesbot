import psycopg2

class PostgreSQLPipeline(object):
    
    def open_spider(self, spider):
        print("\n\n\n\n\n\n\nENTERED THE PIPELINE\n\n\n\n\n\n\n\n")
        self.connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='asdfqwer',
            dbname='postgres'
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute(
            "INSERT INTO items(name, link) VALUES(%s, %s);",
            (item['name'], item['link'])
        )
        self.connection.commit()
        return item
