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

    def add_statistic(self, distance,time):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO statistics (distance,time) VALUES ('%s','%s')" % (distance,time)
        cursor.execute(query)
        connection.commit()
        return

    def update_statistic(self,id,distance,time):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE statistics SET distance = '%s', time = '%s' WHERE id = '%s'" % (distance,time,id)
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