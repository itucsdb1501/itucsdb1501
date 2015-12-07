import psycopg2 as dbapi2

class Athletes:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_athletlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM athletes"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_athlet(self, id):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM athletes WHERE id = '%s'" % (id)
        cursor.execute(query)
        connection.commit()
        return

    def add_athlet(self, name,surname):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO athletes (name,surname) VALUES ('%s','%s')" % (name,surname)
        cursor.execute(query)
        connection.commit()
        return

    def update_athlet(self, id, name , surname):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE athletes SET name = '%s', surname='%s' WHERE id = '%s'" % (name, surname, id)
        cursor.execute(query)
        connection.commit()
        return

    def search_athlet(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM athletes WHERE name LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
