import psycopg2 as dbapi2

class Statistics:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_statisticlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM statistics"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_statistic(self, id_statistic):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM statistics WHERE id_statistic = '%s'" % (id_statistic)
        cursor.execute(query)
        connection.commit()
        return

    def add_statistic(self,distance,time,id_athlete):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO statistics (distance,time,id_athlete) VALUES ('%s','%s','%s')" % (distance,time,id_athlete)
        cursor.execute(query)
        connection.commit()
        return

    def update_statistic(self,id_statistic,name,surname,distance,time):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE statistics SET distance = '%s', time = '%s' WHERE id_statistic = '%s'" % (distance,time,id_statistic)
        cursor.execute(query)
        connection.commit()
        return

    def search_statistic(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM statistics WHERE distance LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows