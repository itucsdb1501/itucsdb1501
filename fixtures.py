import psycopg2 as dbapi2

class Fixtures:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_fixturelist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM fixtures"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_fixture(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM fixtures WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

    def add_fixture(self, week):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO fixtures (week) VALUES ('%s')" % (week)
            cursor.execute(query)
            connection.commit()
            return

    def update_fixture(self, id, week):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE fixtures SET week = '%s', WHERE id = '%s'" % (week, id)
            cursor.execute(query)
            connection.commit()
            return