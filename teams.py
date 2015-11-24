import psycopg2 as dbapi2

class Teams:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_teamlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM teams"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_team(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM teams WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

    def add_team(self, country,continent):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO teams (country,continent) VALUES ('%s')" % (country,continent)
            cursor.execute(query)
            connection.commit()
            return

    def update_team(self, id, country):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE teams SET country = '%s', continent='%s' WHERE id = '%s'" % (country, continent, id)
            cursor.execute(query)
            connection.commit()
            return