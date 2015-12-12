import psycopg2 as dbapi2

class Admins:

    def __init__(self, cp):
        self.cp = cp
        return

    def search_admin(self,username,password):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM admins WHERE kuladi LIKE '%s' AND password LIKE '%s'" % (username,password)
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            return 1
        else:
            return 0

