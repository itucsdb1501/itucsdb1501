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

    def news(self):
       with dbapi2.connect(self.cp) as connection:
           cursor = connection.cursor()
           query = "DROP TABLE IF EXISTS news CASCADE"
           cursor.execute(query)

           query = """CREATE TABLE news (
                   id SERIAL PRIMARY KEY,
                   title VARCHAR(40) UNIQUE NOT NULL
                   content  VARCHAR(40) UNIQUE NOT NULL
               )"""
           cursor.execute(query)

           cursor.execute("INSERT INTO news (title,content) VALUES ('Spain','Europa')")
           cursor.execute("INSERT INTO news (title,content) VALUES ('TUrkey','Europa')")
           cursor.execute("INSERT INTO news (title,content) VALUES ('China','Asia')")
           connection.commit()

    def tickets(self):
       with dbapi2.connect(self.cp) as connection:
           cursor = connection.cursor()
           query = "DROP TABLE IF EXISTS tickets CASCADE"
           cursor.execute(query)

           query = """CREATE TABLE tickets (
                   id SERIAL PRIMARY KEY,
                   name VARCHAR(40) UNIQUE NOT NULL
                   surname  VARCHAR(40) UNIQUE NOT NULL
               )"""
           cursor.execute(query)

           cursor.execute("INSERT INTO tickets (name,surname) VALUES ('elif','aklan')")
           cursor.execute("INSERT INTO tickets (name,surname) VALUES ('xyz','abc')")
           cursor.execute("INSERT INTO tickets (name,surname) VALUES ('ch','xy')")
           connection.commit()

    def competitions(self):
       with dbapi2.connect(self.cp) as connection:
           cursor = connection.cursor()
           query = "DROP TABLE IF EXISTS competitions CASCADE"
           cursor.execute(query)

           query = """CREATE TABLE competitions (
                   id SERIAL PRIMARY KEY,
                   team1 VARCHAR(40) UNIQUE NOT NULL
                   team2  VARCHAR(40) UNIQUE NOT NULL
               )"""
           cursor.execute(query)

           cursor.execute("INSERT INTO competitions (team1,team2) VALUES ('elif','aklan')")
           cursor.execute("INSERT INTO competitions (team1,team2) VALUES ('xyz','abc')")
           cursor.execute("INSERT INTO competitions (team1,team2) VALUES ('ch','xy')")
           connection.commit()


    def fixtures(self):
       with dbapi2.connect(self.cp) as connection:
           cursor = connection.cursor()
           query = "DROP TABLE IF EXISTS fixtures CASCADE"
           cursor.execute(query)

           query = """CREATE TABLE fixtures (
                   id SERIAL PRIMARY KEY,
                   week VARCHAR(40) UNIQUE NOT NULL

               )"""
           cursor.execute(query)

           cursor.execute("INSERT INTO fixtures (week) VALUES ('elif')")
           cursor.execute("INSERT INTO fixtures (week) VALUES ('elif')")
           cursor.execute("INSERT INTO fixtures (week)VALUES ('aklan')")
           connection.commit()

    def All(self):
        self.news()
        self.athletes()
        self.teams()
        self.users()
        self.fixtures()
        self.competitions()
        self.tickets()



