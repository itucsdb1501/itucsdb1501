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

    def delete_user(self, id_user):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE id_user = '%s'" % (id_user)
        cursor.execute(query)
        connection.commit()

    def add_user(self, kuladi,password):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO users (kuladi,password) VALUES ('%s','%s')" % (kuladi,password)
        cursor.execute(query)
        connection.commit()
        return

    def update_user(self, id_user, kuladi,password):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE users SET kuladi = '%s',password='%s' WHERE id_user = '%s'" % (kuladi,password, id_user)
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

    def control_user(self,kuladi,password):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE kuladi LIKE '%s' AND password LIKE '%s'" % (kuladi,password)
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            return 1
        else:
            return 0

