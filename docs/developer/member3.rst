Parts Implemented by SAMET AYALTI
=================================
  Three tables *teams*, *athletes*, and *statistics* are implemented by developer part using Python, PostgrSQL and Vagrant on local.Those objects have in the order tickets.py, competitions.py, fixtures.py python files beside server.py and init.py. Also, there are html file for using text box, check box and button in design part.
  First of all, the implementation logic works running of server.py file. There is part that *"import psycopg2 as dbapi2"* is used as an adaptor to make access for postgreSQL connection. Also, there is an import line for Flask to benefit from its facility which makes the connection between userface and development part of project.


Teams Operations
++++++++++++++++
    In order to perform Teams operations which are add, delete, update and search, there created a table for teams object. In the following a query is used which represents its table structure:

Table Structure
+++++++++++++++
  .. code-block:: sql

     CREATE TABLE tickets (
                id_team SERIAL PRIMARY KEY,
                country VARCHAR(40)
            )

    *This SQL table code block takes place as a query in init.py file. But there should be another query before which is for control of table. It is actually used to drop the table and other objects which depend on it. Also, the realization of query happens in the order of connection of cursor, writing the query, and execution of the query. After creating the table, with some queries for insertion to fill the table and connection.commit() are realized. This actually happens for every object.

    Database Operations
   ++++++++++++++++++

  .. code-block:: python
    .. highlight:: python
      :emphasize-lines: 3,5

    class Teams:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_teamlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM teams"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_team(self, id_team):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM teams WHERE id_team = '%s'" % (id_team)
        cursor.execute(query)
        connection.commit()
        return

    def add_team(self, country):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO teams (country) VALUES ('%s')" % (country)
        cursor.execute(query)
        connection.commit()
        return

    def update_team(self,id_team,country):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE teams SET country = '%s' WHERE id_team = '%s'" % (country,id_team)
        cursor.execute(query)
        connection.commit()
        return

    def search_team(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM teams WHERE country LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

   In the above code, there can be seen Teams class and its functions. For every defined function, there is different queries to be executed.


Athletes Operations
+++++++++++++++++++

    Table structure for Competitions object is like in the following which takes place in *init.py* file:

Table Structure
+++++++++++++++
  .. code-block:: sql

     CREATE TABLE athletes (
               id_athlete SERIAL PRIMARY KEY,
               name VARCHAR(40),
               surname VARCHAR(40),
               country VARCHAR(40) REFERENCES teams(country) ON UPDATE CASCADE ON DELETE CASCADE
            )

    In the following, there is a part of implementation for Athletes object including initialization for athletes class, for obtaining competitions list, and other important operations such as delete, add, update and search which occurs in *athletes.py* file.

Database Structure
++++++++++++++++++
  .. code-block:: python
    :linenos
      .. highlight:: python

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



Statistics Operations
+++++++++++++++++++++

    Table structure for Fixtures object is like in the following which taes place in *init.py* file:

Table Structure
+++++++++++++++
 .. code-block:: sql

    CREATE TABLE statistics (
               id_statistic SERIAL PRIMARY KEY,
               distance VARCHAR(40),
               time VARCHAR(40),
               id_athlete INTEGER REFERENCES athletes(id_athlete) ON UPDATE CASCADE ON DELETE CASCADE
            )

    In the following, there is a part of implementation for Fixtures object including initialization for fixtures class, to obtain statistics list, and other important operations such as delete, add, update and search which occurs in *statistics.py* file.

Database Structure
++++++++++++++++++
  .. code-block:: python
    :linenos
      .. highlight:: python

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

    def update_statistic(self,distance,time,id_statistic):
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

    * What is more, all these python files actually works on server.py file. After development and compilation part, when the server.py is opened program is run. It can be said that how the all python and html parts work together is explained in details in the following:
    * First of all, there is some part of implementation in server.py which can be called main part.

    * The part for the objects in the order of teams, athletes and statistics.

  .. code-block:: python
    :linenos
      .. highlight:: python

@app.route('/Teams', methods=['GET', 'POST'])
def team_page():
    tems = Teams(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        temlist = tems.get_teamlist()
        return render_template('teams.html', TeamList = temlist, current_time=now.ctime())
    elif 'teams_to_delete' in request.form:
        id_teams = request.form.getlist('teams_to_delete')
        for id_team in id_teams:
            tems.delete_team(id_team)
        return redirect(url_for('team_page'))
    elif 'teams_to_add' in request.form:
        tems.add_team(request.form['country'])
        return redirect(url_for('team_page'))
    elif 'teams_to_update' in request.form:
        tems.update_team(request.form['id_team'], request.form['country'])
        return redirect(url_for('team_page'))
    elif 'teams_to_search' in request.form:
            searchList = tems.search_team(request.form['name']);
            now = datetime.datetime.now()
            temlist = tems.get_teamlist()
            return render_template('teams.html', TeamList = temlist, SearchList = searchList, current_time=now.ctime())

#----------------------------------------------------

@app.route('/Athletes', methods=['GET', 'POST'])
def athlet_page():
    aths = Athletes(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        athlist = aths.get_athletlist()
        return render_template('athletes.html', AthletList = athlist, current_time=now.ctime())
    elif 'athletes_to_delete' in request.form:
        id_athletes = request.form.getlist('athletes_to_delete')
        for id_athlete in id_athletes:
            aths.delete_athlet(id_athlete)
        return redirect(url_for('athlet_page'))
    elif 'athletes_to_add' in request.form:
        aths.add_athlet(request.form['name'],request.form['surname'],request.form['country'])
        return redirect(url_for('athlet_page'))
    elif 'athletes_to_update' in request.form:
        aths.update_athlet(request.form['id_athlete'], request.form['name'],request.form['surname'])
        return redirect(url_for('athlet_page'))
    elif 'athletes_to_search' in request.form:
            searchList = aths.search_athlet(request.form['name']);
            now = datetime.datetime.now()
            athlist = aths.get_athletlist()
            return render_template('athletes.html', AthletList = athlist, SearchList = searchList, current_time=now.ctime())

#---------------------------------------------------------------------------

@app.route('/Statistics', methods=['GET', 'POST'])
def statistic_page():
    stats = Statistics(app.config['dsn'])
    aths = Athletes(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        statlist = stats.get_statisticlist()
        athlist = aths.get_athletlist()
        return render_template('statistics.html', StatisticList = statlist,AthletList = athlist, current_time=now.ctime())
    elif 'statistics_to_delete' in request.form:
        id_statistics = request.form.getlist('statistics_to_delete')
        for id_statistic in id_statistics:
            stats.delete_statistic(id_statistic)
        return redirect(url_for('statistic_page'))
    elif 'statistics_to_add' in request.form:
        id_athletes = request.form.getlist('statistics_to_add')
        for id_athlete in id_athletes:
            stats.add_statistic(request.form['distance'], request.form['time'],id_athlete)
        return redirect(url_for('statistic_page'))
    elif 'statistics_to_update' in request.form:
        stats.update_statistic(request.form['distance'], request.form['time'],request.form['id_statistic'])
        return redirect(url_for('statistic_page'))
    elif 'statistics_to_search' in request.form:
            searchList = stats.search_statistic(request.form['name']);
            now = datetime.datetime.now()
            statlist = stats.get_statisticlist()
            athlist = aths.get_athletlist()
            return render_template('statistics.html', StatisticList = statlist, SearchList = searchList,AthletList = athlist, current_time=now.ctime())

    * All the implementation logic works like when the request comes from html page which flask framework works for this part, the request is considered for any wanted operation. Request form is filled by the coming request.

    *After that, data passed as parameter to the called function from object's python file. This is where the queries work. Finally, the result would be returned which is seen on the user page website.
