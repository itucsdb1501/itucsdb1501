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

    def delete_statistic(self, id):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM statistics WHERE id = '%s'" % (id)
        cursor.execute(query)
        connection.commit()
        return

    def add_statistic(self,name,surname,distance,time,id_athlete):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO statistics (name,surname,distance,time,id_athlete) VALUES ('%s','%s','%s','%s','%s')" % (name,surname,distance,time,id_athlete)
        cursor.execute(query)
        connection.commit()
        return

    def update_statistic(self,id,name,surname,distance,time,id_athlete):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE statistics SET id_athlete='%s', name='%s', surname='%s', distance = '%s', time = '%s' WHERE id = '%s'" % (id_athlete,name,surname,distance,time,id)
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