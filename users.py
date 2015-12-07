import psycopg2 as dbapi2

class Users:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_userlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_user(self, id):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE id = '%s'" % (id)
        cursor.execute(query)
        connection.commit()

    def add_user(self, user,password):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO users (kuladi,password) VALUES ('%s','%s')" % (user,password)
        cursor.execute(query)
        connection.commit()
        return

    def update_user(self, id, user,password):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE users SET kuladi = '%s',password='%s' WHERE id = '%s'" % (user,password, id)
        cursor.execute(query)
        connection.commit()
        return

    def search_user(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE kuladi LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

