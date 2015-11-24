import psycopg2 as dbapi2

class Athletes:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_athletlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM athletes"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_athlet(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM athletes WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

    def add_athlet(self, name,surname):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO athletes (name,surname) VALUES ('%s')" % (name,surname)
            cursor.execute(query)
            connection.commit()
            return

    def update_athlet(self, id, name):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE athletes SET name = '%s', title='%s' WHERE id = '%s'" % (name, surname, id)
            cursor.execute(query)
            connection.commit()
            return

