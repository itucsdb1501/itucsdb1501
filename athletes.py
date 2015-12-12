import psycopg2 as dbapi2

class Athletes:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_athletlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM athletes"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_athlet(self, id_athlete):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM athletes WHERE id_athlete = '%s'" % (id_athlete)
        cursor.execute(query)
        connection.commit()
        return

    def add_athlet(self, name,surname,country):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT country FROM teams WHERE country= '%s'" % (country)
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            query = "INSERT INTO athletes (name,surname,country) VALUES ('%s','%s','%s')" % (name,surname,country)
            cursor.execute(query)
        else:
            query = "INSERT INTO teams (country) VALUES ('%s')" % (country)
            cursor.execute(query)
            query = "INSERT INTO athletes (name,surname,country) VALUES ('%s','%s','%s')" % (name,surname,country)
            cursor.execute(query)

        connection.commit()
        return

    def update_athlet(self, id_athlete, name , surname):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE athletes SET name = '%s', surname='%s' WHERE id_athlete = '%s'" % (name, surname, id_athlete)
        cursor.execute(query)
        connection.commit()
        return

    def search_athlet(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM athletes WHERE name LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
