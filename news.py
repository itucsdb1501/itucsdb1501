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

    def delete_new(self, id_new):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM news WHERE id_new = '%s'" % (id_new)
        cursor.execute(query)
        connection.commit()
        return

    def add_new(self,title,content,country):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT country FROM teams WHERE country= '%s'" % (country)
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            query = "INSERT INTO news (title,content,country) VALUES ('%s','%s','%s')" % (title,content,country)
            cursor.execute(query)
        else:
            query = "INSERT INTO teams (country) VALUES ('%s')" % (country)
            cursor.execute(query)
            query = "INSERT INTO news (title,content,country) VALUES ('%s','%s','%s')" % (title,content,country)
            cursor.execute(query)

        connection.commit()
        return

    def update_new(self, id_new, title,content):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE news SET title = '%s', content='%s' WHERE id_new = '%s'" % (title, content, id_new)
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


