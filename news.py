import psycopg2 as dbapi2

class News:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_newlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM news"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_new(self, id):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM news WHERE id = '%s'" % (id)
        cursor.execute(query)
        connection.commit()
        return

    def add_new(self,title,content):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO news (title,content) VALUES ('%s','%s')" % (title,content)
        cursor.execute(query)
        connection.commit()
        return

    def update_new(self, id, title,content):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE news SET title = '%s', content='%s' WHERE id = '%s'" % (title, content, id)
        cursor.execute(query)
        connection.commit()
        return

    def search_new(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM news WHERE title LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows


