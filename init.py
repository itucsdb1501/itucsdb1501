import psycopg2 as dbapi2

class INIT:

    def __init__(self, cp):
        self.cp = cp
        return

    def teams(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DROP TABLE IF EXISTS teams CASCADE"
        cursor.execute(query)
        query = """CREATE TABLE teams (
                id_team SERIAL PRIMARY KEY,
                country VARCHAR(40) UNIQUE NOT NULL
            )"""
        cursor.execute(query)

        cursor.execute("""INSERT INTO teams (country) VALUES ('Turkey')""")
        connection.commit()

    def athletes(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DROP TABLE IF EXISTS athletes CASCADE"
        cursor.execute(query)
        query = """CREATE TABLE athletes (
               id_athlete SERIAL PRIMARY KEY,
               name VARCHAR(40),
               surname VARCHAR(40),
               country VARCHAR(40) REFERENCES teams(country) ON UPDATE CASCADE ON DELETE CASCADE
            )"""
        cursor.execute(query)

        cursor.execute("""INSERT INTO athletes (name,surname,country) VALUES ('Samet','Ayaltı','Turkey')""")
        connection.commit()

    def statistics(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DROP TABLE IF EXISTS statistics CASCADE"
        cursor.execute(query)
        query = """CREATE TABLE statistics (
               id_statistic SERIAL PRIMARY KEY,
               distance VARCHAR(40),
               time VARCHAR(40),
               name VARCHAR(40),
               surname VARCHAR(40),
               id_athlete INTEGER REFERENCES athletes(id_athlete) ON UPDATE CASCADE ON DELETE CASCADE
            )"""
        cursor.execute(query)

        cursor.execute("""INSERT INTO statistics (name,surname,distance,time,id_athlete) VALUES ('Ahmet','Alaq','100m','25sn','1')""")
        connection.commit()

    def users(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DROP TABLE IF EXISTS users CASCADE"
        cursor.execute(query)
        query = """CREATE TABLE users (
               id SERIAL PRIMARY KEY,
               kuladi VARCHAR(40),
               password VARCHAR(40)
            )"""
        cursor.execute(query)

        cursor.execute("""INSERT INTO users (kuladi,password) VALUES ('Samet','Ayaltı')""")
        connection.commit()

    def news(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DROP TABLE IF EXISTS news CASCADE"
        cursor.execute(query)
        query = """CREATE TABLE news (
               id SERIAL PRIMARY KEY,
               title VARCHAR(40),
               content VARCHAR(40)
            )"""
        cursor.execute(query)

        cursor.execute("""INSERT INTO news (title,content) VALUES ('Haber','Ayrıntılar Geliyor')""")
        connection.commit()

    def comments(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DROP TABLE IF EXISTS comments CASCADE"
        cursor.execute(query)
        query = """CREATE TABLE comments (
               id SERIAL PRIMARY KEY,
               name VARCHAR(40),
               article VARCHAR(140)
            )"""
        cursor.execute(query)

        cursor.execute("""INSERT INTO comments (name,article) VALUES ('Samet','Yorumum...')""")
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
        self.teams()
        self.users()

        self.comments()
        self.athletes()
        self.statistics()
#         self.fixtures()
#         self.competitions()
#         self.tickets()



