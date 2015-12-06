
import datetime
import json
import os
import psycopg2 as dbapi2
import re

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask.helpers import url_for

from teams import Teams
from store import Store
from users import Users
from fixtures import Fixtures
from competitions import Competitions
from tickets import Tickets


from init import INIT

app = Flask(__name__)

#alper
def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

#alper



@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())


#-------------------------------------------BURAK BALTA  User START---------------------------------

@app.route('/Users', methods=['GET', 'POST'])
def user_page():
    uses = Users(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        uselist = uses.get_userlist()
        return render_template('teams.html', UserList = uselist, current_time=now.ctime())
    elif 'users_to_delete' in request.form:
        ids = request.form.getlist('users_to_delete')
        for id in ids:
            uses.delete_user(id)
        return redirect(url_for('user_page'))
    elif 'users_to_add' in request.form:
        uses.add_user(request.form['user'],request.form['password'])
        return redirect(url_for('user_page'))
    elif 'users_to_update' in request.form:
        uses.update_user(request.form['id'], request.form['user'],request.form['password'])
        return redirect(url_for('user_page'))

#--------------------------------------------BURAK BALTA News Start-------------------------------
@app.route('/News', methods=['GET', 'POST'])
def new_page():
    nes = News(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        neslist = nes.get_newlist()
        return render_template('news.html', NewList = neslist, current_time=now.ctime())
    elif 'news_to_delete' in request.form:
        ids = request.form.getlist('news_to_delete')
        for id in ids:
            nes.delete_new(id)
        return redirect(url_for('new_page'))
    elif 'news_to_add' in request.form:
        nes.add_new(request.form['title'],request.form['content'])
        return redirect(url_for('new_page'))
    elif 'news_to_update' in request.form:
        nes.update_new(request.form['id'], request.form['title'],request.form['content'])
        return redirect(url_for('new_page'))



#--------------------------------------------BURAK BALTA FNİSHED--------------------------------------

#--------------------------------------SAMET SECTION START HERE--------------------------------------

@app.route('/Teams', methods=['GET', 'POST'])
def team_page():
    tems = Teams(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        temlist = tems.get_teamlist()
        return render_template('teams.html', TeamList = temlist, current_time=now.ctime())
    elif 'teams_to_delete' in request.form:
        ids = request.form.getlist('teams_to_delete')
        for id in ids:
            tems.delete_team(id)
        return redirect(url_for('team_page'))
    elif 'teams_to_add' in request.form:
        tems.add_team(request.form['country'],request.form['continent'])
        return redirect(url_for('team_page'))
    elif 'teams_to_update' in request.form:
        tems.update_team(request.form['id'], request.form['country'],request.form['continent'])
        return redirect(url_for('team_page'))

#------------------------------------------SAMET AYALTI Athletes Start----------

@app.route('/Athletes', methods=['GET', 'POST'])
def athlet_page():
    aths = Athletes(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        athlist = aths.get_athletlist()
        return render_template('athlets.html', AthletList = athlist, current_time=now.ctime())
    elif 'athlets_to_delete' in request.form:
        ids = request.form.getlist('athlets_to_delete')
        for id in ids:
            aths.delete_athlet(id)
        return redirect(url_for('athlet_page'))
    elif 'athlets_to_add' in request.form:
        aths.add_athlet(request.form['name'],request.form['surname'])
        return redirect(url_for('athlet_page'))
    elif 'athlets_to_update' in request.form:
        aths.update_athlet(request.form['id'], request.form['name'],request.form['surname'])
        return redirect(url_for('athlet_page'))

#------------------------------------------SAMET SECTION FNISHED----------------------------------


#---------------------------ELIF tickets START------------------------------


@app.route('/Tickets', methods=['GET', 'POST'])
def ticket_page():
    ticks = Tickets(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        ticklist = ticks.get_ticketlist()
        return render_template('tickets.html', TicketList = ticklist, current_time=now.ctime())
    elif 'tickets_to_delete' in request.form:
        ids = request.form.getlist('tickets_to_delete')
        for id in ids:
            ticks.delete_ticket(id)
        return redirect(url_for('ticket_page'))
    elif 'tickets_to_add' in request.form:
        ticks.add_ticket(request.form['name'],request.form['surname'])
        return redirect(url_for('ticket_page'))
    elif 'tickets_to_update' in request.form:
        ticks.update_ticket(request.form['id'], request.form['name'],request.form['surname'])
        return redirect(url_for('ticket_page'))


#---------------------------ELIF competitions START------------------------------

@app.route('/Competitions', methods=['GET', 'POST'])
def competition_page():
    coms = Competitions(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        comlist = coms.get_competitionlist()
        return render_template('tickets.html', CompetitionList = comlist, current_time=now.ctime())
    elif 'competitions_to_delete' in request.form:
        ids = request.form.getlist('competitions_to_delete')
        for id in ids:
            coms.delete_competition(id)
        return redirect(url_for('competition_page'))
    elif 'competitions_to_add' in request.form:
        coms.add_competition(request.form['team1'],request.form['team2'])
        return redirect(url_for('competition_page'))
    elif 'competitions_to_update' in request.form:
        coms.update_competition(request.form['id'], request.form['team1'],request.form['team2'])
        return redirect(url_for('competition_page'))


#---------------------------ELIF fixtures START------------------------------

@app.route('/Fixtures', methods=['GET', 'POST'])
def fixture_page():
    fixs = Fixtures(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        fixlist = fixs.get_fixturelist()
        return render_template('fixtures.html', FixtureList = fixlist, current_time=now.ctime())
    elif 'fixtures_to_delete' in request.form:
        ids = request.form.getlist('fixtures_to_delete')
        for id in ids:
            fixs.delete_fixture(id)
        return redirect(url_for('fixture_page'))
    elif 'fixtures_to_add' in request.form:
        fixs.add_fixture(request.form['week'])
        return redirect(url_for('fixture_page'))
    elif 'fixtures_to_update' in request.form:
        fixs.update_fixture(request.form['id'], request.form['week'])
        return redirect(url_for('fixture_page'))

#---------------------------ELIF FINISH------------------------------


#alper
class language:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class islem:
    def sel_all(tablo,komut):
         with dbapi2.connect(app.config['dsn']) as connection:
             cursor=connection.cursor()
             cursor.execute(komut)
             rows=cursor.fetchall()
             table=[tablo(row[0] ,row[1]) for row in rows]
         return table
    def add_language(id,name):
          with dbapi2.connect(app.config['dsn']) as connection:
             cursor=connection.cursor()
             query="INSERT INTO LANGUAGES (ID,NAME) VALUES (?, ?)"
             cursor.execute('INSERT INTO LANGUAGES (ID,NAME) VALUES (%s, %s)',(id, name))
             connection.commit()
             return islem.sel_all(language,'SELECT ID,NAME FROM LANGUAGES')

@app.route('/alper')
def alper_tablo():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor=connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS LANGUAGES")
        cursor.execute("CREATE TABLE LANGUAGES(ID INTEGER,NAME VARCHAR(15))")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (1,'TURKCE')")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (2,'INGILIZCE')")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (3,'ALMANCA')")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (4,'RUSCA')")

        connection.commit()

        '''cursor.execute("SELECT ID,NAME FROM LANGUAGES")
        rows=cursor.fetchall()
        #IDS=[row[0] for row in rows]
        languages=[language(row[0] ,row[1]) for row in rows]'''
        '''languages=islem.sel_all(language,'SELECT ID,NAME FROM LANGUAGES')
    return render_template('alper.html',languages=languages)'''
    return render_template('alper.html')

@app.route('/alper_language')
def alper_language():
        languages=islem.sel_all(language,'SELECT ID,NAME FROM LANGUAGES')
        return render_template('alper_language.html',languages=languages)

@app.route('/alper',methods=['GET','POST'])
def language_page():
    if request.method=='GET':
        languages=islem.sel_all(language,'SELECT ID,NAME FROM LANGUAGES')
        return render_template('alper_language.html',languages=languages)
    else:
        id=request.form['id']
        name=request.form['name']
        languages=islem.add_language(int(id),name)
        return render_template('alper_language.html',languages=languages)

@app.route('/alper/add')
def alper_language_edit():
    return render_template('alper_language_edit.html')


 #alper



@app.route('/initdb')
def init_db():
    initialize = INIT(app.config['dsn'])
    initialize.All()
    return redirect(url_for('home_page'))


if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """user='vagrant' password='vagrant'
                               host='localhost' port=54321 dbname='itucsdb'"""

    app.run(host='0.0.0.0', port=port, debug=debug)





