import psycopg2 as dbapi2

class Fixtures:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_fixturelist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM fixtures"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_fixture(self, id_fixture):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM fixtures WHERE id_fixture = '%s'" % (id_fixture)
        cursor.execute(query)
        connection.commit()
        return

    def add_fixture(self, week):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO fixtures (week) VALUES ('%s')" % (week)
        cursor.execute(query)
        connection.commit()
        return

    def update_fixture(self, id_fixture, week):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE fixtures SET week = '%s' WHERE id_fixture = '%s'" % (week, id_fixture)
        cursor.execute(query)
        connection.commit()
        return
    def search_fixture(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM fixtures WHERE week LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows