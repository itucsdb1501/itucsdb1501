import psycopg2 as dbapi2

class INIT:

    def __init__(self, cp):
        self.cp = cp
        return

    def teams(self):
       with dbapi2.connect(self.cp) as connection:
           cursor = connection.cursor()
           query = "DROP TABLE IF EXISTS teams CASCADE"
           cursor.execute(query)

           query = """CREATE TABLE teams (
                   id SERIAL PRIMARY KEY,
                   country VARCHAR(40) UNIQUE NOT NULL
                   continent  VARCHAR(40) UNIQUE NOT NULL
               )"""
           cursor.execute(query)

           cursor.execute("INSERT INTO teams (country,continent) VALUES ('Spain','Europa')")
           cursor.execute("INSERT INTO teams (country,continent) VALUES ('TUrkey','Europa')")
           cursor.execute("INSERT INTO teams (country,continent) VALUES ('China','Asia')")
           connection.commit()

    def athletes(self):
       with dbapi2.connect(self.cp) as connection:
           cursor = connection.cursor()
           query = "DROP TABLE IF EXISTS athletes CASCADE"
           cursor.execute(query)

           query = """CREATE TABLE athletes (
                   id SERIAL PRIMARY KEY,
                   name VARCHAR(40) UNIQUE NOT NULL
                   surname  VARCHAR(40) UNIQUE NOT NULL
               )"""
           cursor.execute(query)

           cursor.execute("INSERT INTO athletes (name,surname) VALUES ('samet','dur')")
           cursor.execute("INSERT INTO athletes (name,surname) VALUES ('xyz','abc')")
           cursor.execute("INSERT INTO athletes (name,surname) VALUES ('ch','xy')")
           connection.commit()

    def users(self):
       with dbapi2.connect(self.cp) as connection:
           cursor = connection.cursor()
           query = "DROP TABLE IF EXISTS users CASCADE"
           cursor.execute(query)

           query = """CREATE TABLE users (
                   id SERIAL PRIMARY KEY,
                   user VARCHAR(40) UNIQUE NOT NULL
                   password  VARCHAR(40) UNIQUE NOT NULL
               )"""
           cursor.execute(query)

           cursor.execute("INSERT INTO users (user,password) VALUES ('Samet','Ayaltı')")
           cursor.execute("INSERT INTO users (user,password) VALUES ('BUrak','Balta')")
           cursor.execute("INSERT INTO users (user,password) VALUES ('Deneme','BirKi')")
           connection.commit()

    def All(self):

        self.teams()
        self.users()

