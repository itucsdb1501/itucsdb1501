import psycopg2 as dbapi2

class News:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_athletlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM news"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_athlet(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM news WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

    def add_athlet(self, title,content):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO news (country,continent) VALUES ('%s')" % (title,content)
            cursor.execute(query)
            connection.commit()
            return

    def update_athlet(self, id, country):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE news SET title = '%s', content='%s' WHERE id = '%s'" % (title, content, id)
            cursor.execute(query)
            connection.commit()
            return