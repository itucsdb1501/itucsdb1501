Parts Implemented by Elif Aklan
===============================
  Three tables *tickets*, *competitions*, and *fixtures* are implemented by developer part using Oracle/Python, SQL and Vagrant on local.Those objects have in the order tickets.py, competitions.py, fixtures.py python files beside server.py and init.py. Also, there are html file for using text box, check box and button in design part.
  First of all, the implementation logic works running of server.py file. There is part that *"import psycopg2 as dbapi2"* is used as an adaptor to make access for postgreSQL connection. Also, there is an import line for Flask to benefit from its facility which makes the connection between userface and development part of project.


Tickets Operations
++++++++++++++++++
    In order to perform Tickets operations which are add, delete, update and search, there created a table for tickets object. In the following a query is used which represents its table structure:

Table Structure
+++++++++++++++
  .. code-block:: sql

     CREATE TABLE tickets (
                id_ticket SERIAL PRIMARY KEY,
                name VARCHAR(40),
                surname  VARCHAR(40)
            )

    *This SQL table code block takes place as a query in init.py file. But there should be another query before which is for control of table. It is actually used to drop the table and other objects which depend on it. Also, the realization of query happens in the order of connection of cursor, writing the query, and execution of the query. After creating the table, with some queries for insertion to fill the table and connection.commit() are realized. This actually happens for every object.

    Database Operations
   ++++++++++++++++++

  .. code-block:: python
    .. highlight:: python
      :emphasize-lines: 3,5

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

   In the above code, there can be seen Tickets class and its functions. For every defined function, there is different queries to be executed.


Competitions Operations
+++++++++++++++++++++++

    Table structure for Competitions object is like in the following which taes place in *init.py* file:

Table Structure
+++++++++++++++
  .. code-block:: sql

     CREATE TABLE competitions (
                id_competition SERIAL PRIMARY KEY,
                team1 VARCHAR(40),
                team2  VARCHAR(40)
            )

    In the following, there is a part of implementation for Competitions object including initialization for competitions class, for obtaining competitions list, and other important operations such as delete, add, update and search which occurs in *competitions.py* file.

Database Structure
++++++++++++++++++
  .. code-block:: python
    :linenos
      .. highlight:: python

  class Competitions:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_competitionlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM competitions"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_competition(self, id_competition):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM competitions WHERE id_competition = '%s'" % (id_competition)
        cursor.execute(query)
        connection.commit()
        return

    def add_competition(self, team1, team2):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO competitions (team1,team2) VALUES ('%s', '%s')" % (team1,team2)
        cursor.execute(query)
        connection.commit()
        return

    def update_competition(self, id_competition, team1,team2):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE competitions SET team1 = '%s',team2='%s' WHERE id_competition = '%s'" % (team1, team2, id_competition)
        cursor.execute(query)
        connection.commit()
        return

    def search_competition(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM competitions WHERE team1 LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows


Fixtures Operations
+++++++++++++++++++

    Table structure for Fixtures object is like in the following which taes place in *init.py* file:

Table Structure
+++++++++++++++
 .. code-block:: sql

    CREATE TABLE fixtures (
                id_fixture SERIAL PRIMARY KEY,
                week VARCHAR(40)
            )

    In the following, there is a part of implementation for Fixtures object including initialization for fixtures class, to obtain competitions list, and other important operations such as delete, add, update and search which occurs in *fixtures.py* file.

Database Structure
++++++++++++++++++
  .. code-block:: python
    :linenos
      .. highlight:: python

   class Fixtures:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_fixturelist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM fixtures"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_fixture(self, id_fixture):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM fixtures WHERE id_fixture = '%s'" % (id_fixture)
        cursor.execute(query)
        connection.commit()
        return

    def add_fixture(self, week):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO fixtures (week) VALUES ('%s')" % (week)
        cursor.execute(query)
        connection.commit()
        return

    def update_fixture(self, id_fixture, week):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE fixtures SET week = '%s' WHERE id_fixture = '%s'" % (week, id_fixture)
        cursor.execute(query)
        connection.commit()
        return
    def search_fixture(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM fixtures WHERE week LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    * What is more, all these python files actually works on server.py file. After development and compilation part, when the server.py is opened program is run. It can be said that how the all python and html parts work together is explained in details in the following:
    * First of all, there is some part of implementation in server.py which can be called main part.

    * The part for the objects in the order of tickets, competitions and fixtures.

  .. code-block:: python
    :linenos
      .. highlight:: python

@app.route('/Tickets', methods=['GET', 'POST'])
def ticket_page():
    ticks = Tickets(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        ticklist = ticks.get_ticketlist()
        return render_template('tickets.html', TicketList = ticklist, current_time=now.ctime())
    elif 'tickets_to_delete' in request.form:
        id_tickets = request.form.getlist('tickets_to_delete')
        for id_ticket in id_tickets:
            ticks.delete_ticket(id_ticket)
        return redirect(url_for('ticket_page'))
    elif 'tickets_to_add' in request.form:
        ticks.add_ticket(request.form['name'], request.form['surname'])
        return redirect(url_for('ticket_page'))
    elif 'tickets_to_update' in request.form:
        ticks.update_ticket(request.form['id'], request.form['name'],request.form['surname'])
        return redirect(url_for('ticket_page'))
    elif 'tickets_to_search' in request.form:
        searchlist = ticks.search_ticket(request.form['name']);
        now = datetime.datetime.now()
        ticklist = ticks.get_ticketlist()
        return render_template('tickets.html', TicketList = ticklist, SearchList = searchlist, current_time = now.ctime())

    * Secondly, there comes for competitions:

  .. code-block:: python
   :linen

@app.route('/Competitions', methods=['GET', 'POST'])
def competition_page():
    coms = Competitions(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        comlist = coms.get_competitionlist()
        return render_template('competitions.html', CompetitionList = comlist, current_time=now.ctime())
    elif 'competitions_to_delete' in request.form:
        id_competitions = request.form.getlist('competitions_to_delete')
        for id_competition in id_competitions:
            coms.delete_competition(id_competition)
        return redirect(url_for('competition_page'))
    elif 'competitions_to_add' in request.form:
        coms.add_competition(request.form['team1'],request.form['team2'])
        return redirect(url_for('competition_page'))
    elif 'competitions_to_update' in request.form:
        coms.update_competition(request.form['id_competition'], request.form['team1'],request.form['team2'])
        return redirect(url_for('competition_page'))
    elif 'competitions_to_search' in request.form:
        searchlist = coms.search_competition(request.form['name']);
        now = datetime.datetime.now()
        comlist = coms.get_competitionlist()
        return render_template('competitions.html', CompetitionList = comlist, SearchList = searchlist, current_time = now.ctime())

    * Lastly, fixtures part comes in server.py file:

  .. code-block:: python
    :linenos
      .. highlight:: python

@app.route('/Fixtures', methods=['GET', 'POST'])
def fixture_page():
    fixs = Fixtures(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        fixlist = fixs.get_fixturelist()
        return render_template('fixtures.html', FixtureList = fixlist, current_time=now.ctime())
    elif 'fixtures_to_delete' in request.form:
        id_fixtures = request.form.getlist('fixtures_to_delete')
        for id_fixture in id_fixtures:
            fixs.delete_fixture(id_fixture)
        return redirect(url_for('fixture_page'))
    elif 'fixtures_to_add' in request.form:
        fixs.add_fixture(request.form['week'])
        return redirect(url_for('fixture_page'))
    elif 'fixtures_to_update' in request.form:
        fixs.update_fixture(request.form['id_fixture'], request.form['week'])
        return redirect(url_for('fixture_page'))
    elif 'fixtures_to_search' in request.form:
        searchlist = fixs.search_fixture(request.form['name']);
        now = datetime.datetime.now()
        fixlist = fixs.get_fixturelist()
        return render_template('fixtures.html', FixtureList = fixlist, SearchList = searchlist, current_time = now.ctime())

    * All the implementation logic works like when the request comes from html page which flask framework works for this part, the request is considered for any wanted operation. Request form is filled by the coming request.

    *After that, data passed as parameter to the called function from object's python file. This is where the queries work. Finally, the result would be returned which is seen on the user page website.
