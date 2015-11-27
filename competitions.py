import psycopg2 as dbapi2

class Competitions:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_competitionlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM competitions"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_competition(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM competition WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

    def add_competition(self, team1, team2):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO competition (team1,team2) VALUES ('%s')" % (team1,team2)
            cursor.execute(query)
            connection.commit()
            return

    def update_competition(self, id, team1,team2):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE competition SET team1 = '%s', team2='%s' WHERE id = '%s'" % (team1, team2, id)
            cursor.execute(query)
            connection.commit()
            return