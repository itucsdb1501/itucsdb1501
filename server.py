
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
class anthem:
    def __init__(self,id,name,language):
        self.id=id
        self.name=name
        self.language=language
class continent:
    def __init__(self,id,country,continent,language):
        self.id=id
        self.country=country
        self.continent=continent
        self.language=language
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
             #query="INSERT INTO LANGUAGES (ID,NAME) VALUES (?, ?)"
             cursor.execute('INSERT INTO LANGUAGES (ID,NAME) VALUES (%s, %s)',(id, name))
             connection.commit()
             return islem.sel_all(language,'SELECT ID,NAME FROM LANGUAGES')
    def del_language(id):
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor=connection.cursor()
            cursor.execute('DELETE FROM LANGUAGES WHERE ID=%s',[id])
            connection.commit()
    def up_language(id,name):
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor=connection.cursor()
            cursor.execute('UPDATE LANGUAGES SET NAME=%s WHERE ID=%s',(name,id))
            connection.commit()
    def sel_anthem(tablo,komut):
        with dbapi2.connect(app.config['dsn']) as connection:
             cursor=connection.cursor()
             cursor.execute(komut)
             rows=cursor.fetchall()
             table=[tablo(row[0] ,row[1],row[2]) for row in rows]
        return table
    def del_anthem(id):
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor=connection.cursor()
            cursor.execute('DELETE FROM ANTHEMS WHERE ID=%s',[id])
            connection.commit()
    def add_anthem(id,name,language):
          with dbapi2.connect(app.config['dsn']) as connection:
             cursor=connection.cursor()
             #query="INSERT INTO LANGUAGES (ID,NAME) VALUES (?, ?)"
             cursor.execute('INSERT INTO ANTHEMS (ID,NAME,LANGUAGE) VALUES (%s, %s,%s)',(id, name,language))
             connection.commit()
             return islem.sel_anthem(anthem,'SELECT ID,NAME,LANGUAGE FROM ANTHEMS')
    def up_anthem(id,name,language):
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor=connection.cursor()
            cursor.execute('UPDATE ANTHEMS SET NAME=%s,LANGUAGE=%s WHERE ID=%s',(name,language,id))
            connection.commit()
    def sel_continent(tablo,komut):
        with dbapi2.connect(app.config['dsn']) as connection:
             cursor=connection.cursor()
             cursor.execute(komut)
             rows=cursor.fetchall()
             table=[tablo(row[0] ,row[1],row[2],row[3]) for row in rows]
        return table
    def del_continent(id):
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor=connection.cursor()
            cursor.execute('DELETE FROM CONTINENTS WHERE ID=%s',[id])
            connection.commit()
    def add_continent(id,country,continent,language):
          with dbapi2.connect(app.config['dsn']) as connection:
             cursor=connection.cursor()
             cursor.execute('INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE) VALUES (%s, %s,%s,%s)',(id, country,continent,language))
             connection.commit()
    def up_continent(id,country,continent,language):
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor=connection.cursor()
            cursor.execute('UPDATE CONTINENTS SET COUNTRY=%s,CONTINENT=%s,LANGUAGE=%s WHERE ID=%s',(country,continent,language,id))
            connection.commit()
@app.route('/alper')
def alper_tablo():
    return render_template('alper.html')



@app.route('/alper/olustur')
def olustur():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor=connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS ANTHEMS")
        cursor.execute("DROP TABLE IF EXISTS CONTINENTS")
        cursor.execute("DROP TABLE IF EXISTS LANGUAGES")
        cursor.execute("CREATE TABLE LANGUAGES(ID INTEGER UNIQUE PRIMARY KEY,NAME VARCHAR(20) UNIQUE)")
        cursor.execute("CREATE TABLE ANTHEMS(ID INTEGER UNIQUE PRIMARY KEY,NAME VARCHAR(20),LANGUAGE VARCHAR(20) REFERENCES LANGUAGES(NAME))")
        cursor.execute("CREATE TABLE CONTINENTS(ID INTEGER UNIQUE PRIMARY KEY,COUNTRY VARCHAR(20),CONTINENT VARCHAR(20),LANGUAGE VARCHAR(20) REFERENCES LANGUAGES(NAME))")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (1,'TURKCE')")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (2,'INGILIZCE')")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (3,'ALMANCA')")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (4,'RUSCA')")
        cursor.execute("INSERT INTO ANTHEMS (ID,NAME,LANGUAGE) VALUES (1,'ISTIKLAL MARSI','TURKCE')")
        cursor.execute("INSERT INTO ANTHEMS (ID,NAME,LANGUAGE) VALUES (2,'GOD SAVE THE QUENN','INGILIZCE')")
        cursor.execute("INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE) VALUES (1,'TURKIYE','AVRUPA','TURKCE')")
        cursor.execute("INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE) VALUES (2,'INGILTERE','AVRUPA','INGILIZCE')")
        cursor.execute("INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE) VALUES (3,'ALMANYA','AVRUPA','ALMANCA')")
        cursor.execute("INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE) VALUES (4,'RUSYA','AVRUPA','RUSCA')")
        cursor.execute("INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE) VALUES (5,'AMERIKA','AMERIKA','INGILIZCE')")
        connection.commit()
    return render_template('alper.html')

@app.route('/alper_language')
def alper_language():
    try:
        languages=islem.sel_all(language,'SELECT ID,NAME FROM LANGUAGES')
        return render_template('alper_language.html',languages=languages)
    except:
        hata='press create database'
        return render_template('alper_error.html',hata=hata)


@app.route('/alper',methods=['GET','POST'])
def language_page():
    if request.method=='GET':
        return redirect(url_for('alper_language'))
    elif 'languages_to_delete' in request.form:
        values=request.form.getlist('languages_to_delete')
        try:
            for value in values:
                islem.del_language(value)
            return redirect(url_for('alper_language'))
        except:
            hata='value is foreign key to other tables'
            return render_template('alper_error.html',hata=hata)
    else:
        id=request.form['id']
        name=request.form['name']
        try:
            languages=islem.add_language(int(id),name)
            return render_template('alper_language.html',languages=languages)
        except:
            hata='error in addition(invalid id)'
            return render_template('alper_error.html',hata=hata)

@app.route('/alper/add')
def alper_language_edit():
    return render_template('alper_language_edit.html')

@app.route('/alper/up',methods=['GET','POST'])
def language_update():
    if request.method=='GET':
        languages=islem.sel_all(language,'SELECT ID,NAME FROM LANGUAGES')
        return render_template('alper_language.html',languages=languages)
    else:
        id=request.form['id']
        name=request.form['name']
        try:
            islem.up_language(id, name)
            return redirect(url_for('alper_language'))
        except:
            hata='error in update(invalid id)'
            return render_template('alper_error.html',hata=hata)

@app.route('/alper/update')
def alper_language_up():
    return render_template('alper_language_up.html')


@app.route('/alper/anthemlist')
def anthem_list():
    try:
        anthems=islem.sel_anthem(anthem,'SELECT ID,NAME,LANGUAGE FROM ANTHEMS')
        return render_template('alper_anthem.html',anthems=anthems)
    except:
        hata='press create database'
        return render_template('alper_error.html',hata=hata)

@app.route('/alper/anthem',methods=['GET','POST'])
def anthem_page():
    if request.method=='GET':
        return redirect(url_for('anthem_list'))
    elif 'anthems_to_delete' in request.form:
        values=request.form.getlist('anthems_to_delete')
        for value in values:
            islem.del_anthem(value)
        return redirect(url_for('anthem_list'))
    else:
        id=request.form['id']
        name=request.form['name']
        language=request.form['language']
        try:
            languages=islem.add_anthem(id, name, language)
            return redirect(url_for('anthem_list'))
        except:
            hata='Invalid language input(language is foreign key to language table) or invalid id'
            return render_template('alper_error.html',hata=hata)

@app.route('/alper/anthem/add')
def alper_anthem_edit():
    return render_template('alper_anthem_edit.html')

@app.route('/alper/anthem/update')
def alper_anthem_up():
    return render_template('alper_anthem_up.html')
@app.route('/alper/anthem/update',methods=['GET','POST'])
def anthem_update():
    if request.method=='GET':
        return redirect(url_for('anthem_list'))
    else:
        id=request.form['id']
        name=request.form['name']
        language=request.form['language']
        try:
            islem.up_anthem(id, name,language)
            return redirect(url_for('anthem_list'))
        except:
            hata='Invalid language input(language is foreign key to language table) or invalid id'
            return render_template('alper_error.html',hata=hata)



@app.route('/alper/continentlist')
def continent_list():
    try:
        continents=islem.sel_continent(continent,'SELECT ID,COUNTRY,CONTINENT,LANGUAGE FROM CONTINENTS' )
        return render_template('alper_continent.html',continents=continents)
    except:
        hata='press create database'
        return render_template('alper_error.html',hata=hata)
@app.route('/alper/continent',methods=['GET','POST'])
def continent_page():
    if request.method=='GET':
        return redirect(url_for('continent_list'))
    elif 'continents_to_delete' in request.form:
        values=request.form.getlist('continents_to_delete')
        for value in values:
            islem.del_continent(value)
        return redirect(url_for('continent_list'))
    else:
        id=request.form['id']
        country=request.form['country']
        continent=request.form['continent']
        language=request.form['language']
        try:
            languages=islem.add_continent(id, country, continent, language)
            return redirect(url_for('continent_list'))
        except:
            hata='invalid language or id(id is key and language is foreign key)'
            return render_template('alper_error.html',hata=hata)
@app.route('/alper/continent/add')
def alper_continent_edit():
    return render_template('alper_continent_edit.html')
@app.route('/alper/continent/update')
def alper_continent_up():
    return render_template('alper_continent_up.html')
@app.route('/alper/continent/update',methods=['GET','POST'])
def continent_update():
    if request.method=='GET':
        return redirect(url_for('continent_list'))
    else:
        id=request.form['id']
        country=request.form['country']
        continent=request.form['continent']
        language=request.form['language']
        try:
            islem.up_continent(id, country, continent, language)
            return redirect(url_for('continent_list'))
        except:
            hata='invalid language(language is foreign key)'
            return render_template('alper_error.html',hata=hata)


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





