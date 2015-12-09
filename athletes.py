import psycopg2 as dbapi2
from jinja2.lexer import integer_re
from orca.messages import EMPTY

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

    def delete_athlet(self, id):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM athletes WHERE id = '%s'" % (id)
        cursor.execute(query)
        connection.commit()
        return

    def add_athlet(self, name,surname,country):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
#        query = "SELECT id FROM teams WHERE country= '%s'" % (country)
#        cursor.execute(query)
#        rows = cursor.fetchall()

#        if rows
#        query = "INSERT INTO teams (country) VALUES ('%s')" % (country)
#        cursor.execute(query)
#        query = "INSERT INTO athletes (name,surname) VALUES ('%s','%s')" % (name,surname)
#        cursor.execute(query)
#       else:
 
        query = "INSERT INTO athletes (name,surname,country) VALUES ('%s','%s','%s')" % (name,surname,country)
        cursor.execute(query)

        connection.commit()
        return

    def update_athlet(self, id, name , surname, country):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE athletes SET name = '%s', surname='%s', country='%s' WHERE id = '%s'" % (name, surname,country, id)
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
