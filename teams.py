import psycopg2 as dbapi2

class Teams:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_teamlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM teams"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_team(self, id_team):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM teams WHERE id_team = '%s'" % (id_team)
        cursor.execute(query)
        connection.commit()
        return

    def add_team(self, country):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO teams (country) VALUES ('%s')" % (country)
        cursor.execute(query)
        connection.commit()
        return

    def update_team(self,id_team,country):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE teams SET country = '%s' WHERE id_team = '%s'" % (country,id_team)
        cursor.execute(query)
        connection.commit()
        return

    def search_team(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM teams WHERE country LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows