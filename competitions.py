import psycopg2 as dbapi2

class Competitions:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_competitionlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM competitions"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_competition(self, id_competition):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM competitions WHERE id_competition = '%s'" % (id_competition)
        cursor.execute(query)
        connection.commit()
        return

    def add_competition(self, team1, team2):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO competitions (team1,team2) VALUES ('%s', '%s')" % (team1,team2)
        cursor.execute(query)
        connection.commit()
        return

    def update_competition(self, id_competition, team1,team2):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE competitions SET team1 = '%s',team2='%s' WHERE id_competition = '%s'" % (team1, team2, id_competition)
        cursor.execute(query)
        connection.commit()
        return

    def search_competition(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM competitions WHERE team1 LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows