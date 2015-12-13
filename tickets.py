import psycopg2 as dbapi2

class Tickets:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_ticketlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM tickets"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_ticket(self, id):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM tickets WHERE id_ticket = '%s'" % (id)
        cursor.execute(query)
        connection.commit()
        return

    def add_ticket(self, name, surname):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO tickets (name,surname) VALUES ('%s', '%s')" % (name,surname)
        cursor.execute(query)
        connection.commit()
        return

    def update_ticket(self, id, name, surname):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE tickets SET name = '%s', surname='%s' WHERE id_ticket = '%s'" % (name, surname, id)
        cursor.execute(query)
        connection.commit()
        return

    def search_ticket(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM tickets WHERE name LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows