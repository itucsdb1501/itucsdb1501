import psycopg2 as dbapi2

class Comments:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_commentlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM comments"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_comment(self, id_comment):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM comments WHERE id_comment = '%s'" % (id_comment)
        cursor.execute(query)
        connection.commit()
        return

    def add_comment(self, name,article,id_new):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO comments (name,article,id_new) VALUES ('%s','%s','%s')" % (name,article,id_new)
        cursor.execute(query)
        connection.commit()
        return

    def update_comment(self, id_comment, name , article):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE comments SET name = '%s', article='%s' WHERE id_comment = '%s'" % (name, article, id_comment)
        cursor.execute(query)
        connection.commit()
        return

    def search_comment(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM comments WHERE name LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
