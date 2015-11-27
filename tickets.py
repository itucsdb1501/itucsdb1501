import psycopg2 as dbapi2

class Tickets:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_ticketlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM tickets"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_ticket(self, id):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM tickets WHERE id = '%s'" % (id)
            cursor.execute(query)
            connection.commit()
            return

    def add_ticket(self, name, surname):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO tickets (name,surname) VALUES ('%s')" % (name,surname)
            cursor.execute(query)
            connection.commit()
            return

    def update_ticket(self, id, name, surname):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "UPDATE tickets SET name = '%s', surname='%s' WHERE id = '%s'" % (name, surname, id)
            cursor.execute(query)
            connection.commit()
            return