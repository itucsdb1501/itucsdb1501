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
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM users WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

    def add_user(self, user):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO users (user,password) VALUES ('%s')" % (user,password)
            cursor.execute(query)
            connection.commit()
            return

    def update_user(self, id, user,password):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE users SET user = '%s',password='%s' WHERE id = '%s'" % (user,password, id)
            cursor.execute(query)
            connection.commit()
            return

