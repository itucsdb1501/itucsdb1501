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
from athletes import Athletes
from statistics import Statistics
from users import Users
from admins import Admins
from news import News
from comments import Comments
from fixtures import Fixtures
from competitions import Competitions
from tickets import Tickets


from init import INIT
from _ast import Not

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
    initialize = INIT(app.config['dsn'])
    initialize.All()
    return render_template('home.html', current_time=now.ctime())

@app.route('/Start')
def home_page2():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/Admins', methods=['GET', 'POST'])
def admin_page():
     now = datetime.datetime.now()
     adms = Admins(app.config['dsn'])
     if request.method == 'GET':
        now = datetime.datetime.now()
        return render_template('admins.html', current_time=now.ctime())
     elif 'admin_to_control' in request.form:
        searchList = adms.search_admin(request.form['username'],request.form['password']);
        if searchList == 1:
            return redirect(url_for('admin_page'))
        else:
            return redirect(url_for('home_page2'))

@app.route('/Persons', methods=['GET', 'POST'])
def person_page():
     now = datetime.datetime.now()
     uses = Users(app.config['dsn'])
     if request.method == 'GET':
        now = datetime.datetime.now()
        return render_template('persons.html', current_time=now.ctime())
     elif 'persons_to_control' in request.form:
        searchList = uses.control_user(request.form['username'],request.form['password']);
        if searchList == 1:
            return redirect(url_for('person_page'))
        else:
            return redirect(url_for('home_page2'))


#-------------------------------------------BURAK BALTA  User START---------------------------------

@app.route('/Users', methods=['GET', 'POST'])
def user_page():
    uses = Users(app.config['dsn'])
    if request.method == 'GET' and ('users_to_new' not in request.form):
        now = datetime.datetime.now()
        uselist = uses.get_userlist()
        return render_template('users.html', UserList = uselist, current_time=now.ctime())
    elif 'users_to_delete' in request.form:
        id_users = request.form.getlist('users_to_delete')
        for id_user in id_users:
            uses.delete_user(id_user)
        return redirect(url_for('user_page'))
    elif 'users_to_add' in request.form:
        uses.add_user(request.form['kuladi'],request.form['password'])
        return redirect(url_for('user_page'))
    elif 'users_to_update' in request.form:
        uses.update_user(request.form['id_user'], request.form['kuladi'],request.form['password'])
        return redirect(url_for('user_page'))
    elif 'users_to_search' in request.form:
            searchList = uses.search_user(request.form['name']);
            now = datetime.datetime.now()
            uselist = uses.get_userlist()
            return render_template('users.html', UserList = uselist, SearchList = searchList, current_time=now.ctime())
    elif 'users_to_new' in request.form:
        uses.add_user(request.form['user'],request.form['password'])
        return redirect(url_for('home_page2'))
#--------------------------------------------BURAK BALTA News Start-------------------------------
@app.route('/News', methods=['GET', 'POST'])
def new_page():
    nes = News(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        nelist = nes.get_newlist()
        return render_template('news.html', NewList = nelist, current_time=now.ctime())
    elif 'news_to_delete' in request.form:
        id_news = request.form.getlist('news_to_delete')
        for id_new in id_news:
            nes.delete_new(id_new)
        return redirect(url_for('new_page'))
    elif 'news_to_add' in request.form:
        nes.add_new(request.form['title'],request.form['content'],request.form['country'])
        return redirect(url_for('new_page'))
    elif 'news_to_update' in request.form:
        nes.update_new(request.form['id_new'], request.form['title'],request.form['content'])
        return redirect(url_for('new_page'))
    elif 'news_to_search' in request.form:
            searchList = nes.search_new(request.form['name']);
            now = datetime.datetime.now()
            nelist = nes.get_newlist()
            return render_template('news.html', NewList = nelist, SearchList = searchList, current_time=now.ctime())

@app.route('/Comments', methods=['GET', 'POST'])
def comment_page():
    coms = Comments(app.config['dsn'])
    nes = News(app.config['dsn'])
    if request.method == 'GET':
        now = datetime.datetime.now()
        comlist = coms.get_commentlist()
        nelist = nes.get_newlist()
        return render_template('comments.html', CommentList = comlist, NewList = nelist, current_time=now.ctime())
    elif 'comments_to_delete' in request.form:
        id_comments = request.form.getlist('comments_to_delete')
        for id_comment in id_comments:
            coms.delete_comment(id_comment)
        return redirect(url_for('comment_page'))
    elif 'comments_to_add' in request.form:
        id_comments = request.form.getlist('comments_to_add')
        for id_comment in id_comments:
            coms.add_comment(request.form['name'],request.form['article'],id_comment)
        return redirect(url_for('comment_page'))
    elif 'comments_to_update' in request.form:
        coms.update_comment(request.form['id_comment'], request.form['name'],request.form['article'])
        return redirect(url_for('comment_page'))
    elif 'comments_to_search' in request.form:
            searchList = coms.search_comment(request.form['name']);
            now = datetime.datetime.now()
            comlist = coms.get_commentlist()
            nelist = nes.get_newlist()
            return render_template('comments.html', CommentList = comlist, NewList = nelist, SearchList = searchList, current_time=now.ctime())


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

#------------------------------------------SAMET AYALTI Athletes Start----------

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

#------------------------------------------------Samet Statistics---------------------------

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


#---------------------------ELIF competitions START------------------------------

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


#---------------------------ELIF fixtures START------------------------------

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
    def __init__(self,id,country,continent,language,ant):
        self.id=id
        self.country=country
        self.continent=continent
        self.language=language
        self.ant=ant
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
             return islem.sel_all(language,'SELECT ID,NAME FROM LANGUAGES ORDER BY ID')
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
    def ar_language(name):
         with dbapi2.connect(app.config['dsn']) as connection:
             cursor=connection.cursor()
             komut="SELECT ID,NAME FROM LANGUAGES WHERE NAME LIKE '%s'" % name
             cursor.execute(komut)
             rows=cursor.fetchall()
             table=[language(row[0] ,row[1]) for row in rows]
         return table
    def ar_anthem(name):
         with dbapi2.connect(app.config['dsn']) as connection:
             cursor=connection.cursor()
             komut="SELECT ID,NAME,LANGUAGE FROM ANTHEMS WHERE NAME LIKE '%s'" % name
             cursor.execute(komut)
             rows=cursor.fetchall()
             table=[anthem(row[0] ,row[1],row[2]) for row in rows]
         return table
    def ar_continent(name):
         with dbapi2.connect(app.config['dsn']) as connection:
             cursor=connection.cursor()
             komut="SELECT ID,COUNTRY,CONTINENT,LANGUAGE,ANT FROM CONTINENTS WHERE CONTINENT LIKE '%s'" % name
             cursor.execute(komut)
             rows=cursor.fetchall()
             table=[continent(row[0],row[1],row[2],row[3],row[4]) for row in rows]
         return table
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
             return islem.sel_anthem(anthem,'SELECT ID,NAME,LANGUAGE FROM ANTHEMS ORDER BY ID')
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
             table=[tablo(row[0] ,row[1],row[2],row[3],row[4]) for row in rows]
        return table
    def del_continent(id):
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor=connection.cursor()
            cursor.execute('DELETE FROM CONTINENTS WHERE ID=%s',[id])
            connection.commit()
    def add_continent(id,country,continent,language,ant):
          with dbapi2.connect(app.config['dsn']) as connection:
             cursor=connection.cursor()
             cursor.execute('INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE,ANT) VALUES (%s, %s,%s,%s,%s)',(id, country,continent,language,ant))
             connection.commit()
    def up_continent(id,country,continent,language,ant):
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor=connection.cursor()
            cursor.execute('UPDATE CONTINENTS SET COUNTRY=%s,CONTINENT=%s,LANGUAGE=%s,ANT=%s WHERE ID=%s',(country,continent,language,ant,id))
            connection.commit()
@app.route('/alper')
def alper_tablo():
    return render_template('alper.html')



@app.route('/alper/olustur')
def olustur():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor=connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS CONTINENTS")
        cursor.execute("DROP TABLE IF EXISTS ANTHEMS")
        cursor.execute("DROP TABLE IF EXISTS LANGUAGES")
        cursor.execute("CREATE TABLE LANGUAGES(ID INTEGER UNIQUE PRIMARY KEY,NAME VARCHAR(20) UNIQUE)")
        cursor.execute("CREATE TABLE ANTHEMS(ID INTEGER UNIQUE PRIMARY KEY,NAME VARCHAR(20) UNIQUE,LANGUAGE VARCHAR(20) REFERENCES LANGUAGES(NAME))")
        cursor.execute("CREATE TABLE CONTINENTS(ID INTEGER UNIQUE PRIMARY KEY,COUNTRY VARCHAR(20),CONTINENT VARCHAR(20),LANGUAGE VARCHAR(20) REFERENCES LANGUAGES(NAME),ANT VARCHAR(20) REFERENCES ANTHEMS(NAME))")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (1,'TURKCE')")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (2,'INGILIZCE')")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (3,'ALMANCA')")
        cursor.execute("INSERT INTO LANGUAGES (ID,NAME) VALUES (4,'RUSCA')")
        cursor.execute("INSERT INTO ANTHEMS (ID,NAME,LANGUAGE) VALUES (1,'ISTIKLAL MARSI','TURKCE')")
        cursor.execute("INSERT INTO ANTHEMS (ID,NAME,LANGUAGE) VALUES (2,'GOD SAVE THE QUENN','INGILIZCE')")
        cursor.execute("INSERT INTO ANTHEMS (ID,NAME,LANGUAGE) VALUES (3,'DEUTSCHLANDLIED','ALMANCA')")
        cursor.execute("INSERT INTO ANTHEMS (ID,NAME,LANGUAGE) VALUES (4,'RUSYA ULUSAL MARSI','RUSCA')")
        cursor.execute("INSERT INTO ANTHEMS (ID,NAME,LANGUAGE) VALUES (5,'THE STAR','INGILIZCE')")
        cursor.execute("INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE,ANT) VALUES (1,'TURKIYE','AVRUPA','TURKCE','ISTIKLAL MARSI')")
        cursor.execute("INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE,ANT) VALUES (2,'INGILTERE','AVRUPA','INGILIZCE','GOD SAVE THE QUENN')")
        cursor.execute("INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE,ANT) VALUES (3,'ALMANYA','AVRUPA','ALMANCA','DEUTSCHLANDLIED')")
        cursor.execute("INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE,ANT) VALUES (4,'RUSYA','AVRUPA','RUSCA','RUSYA ULUSAL MARSI')")
        cursor.execute("INSERT INTO CONTINENTS (ID,COUNTRY,CONTINENT,LANGUAGE,ANT) VALUES (5,'AMERIKA','AMERIKA','INGILIZCE','THE STAR')")
        connection.commit()
    return render_template('alper.html')

@app.route('/alper_language')
def alper_language():
    try:
        languages=islem.sel_all(language,'SELECT ID,NAME FROM LANGUAGES ORDER BY ID')
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
        languages=islem.sel_all(language,'SELECT ID,NAME FROM LANGUAGES ORDER BY ID')
        return render_template('alper_language.html',languages=languages)
    else:
        id=request.form['id']
        name=request.form['name']
        try:
            islem.up_language(id, name)
            return redirect(url_for('alper_language'))
        except:
            hata='error in update(invalid id or foreign key error)'
            return render_template('alper_error.html',hata=hata)

@app.route('/alper/ar',methods=['GET','POST'])
def language_ara():
    if request.method=='GET':
        languages=islem.sel_all(language,'SELECT ID,NAME FROM LANGUAGES ORDER BY ID')
        return render_template('alper_language.html',languages=languages)
    else:
        name=request.form['name']
        languages=islem.ar_language(name)
        return render_template('alper_language.html',languages=languages)


@app.route('/don')
def don():
   return render_template('layout.html')
@app.route('/alper/update')
def alper_language_up():
    return render_template('alper_language_up.html')

@app.route('/alper/ara')
def alper_language_ara():
    return render_template('alper_language_ara.html')
@app.route('/alper/anthem/ara')
def alper_anthem_ara():
    return render_template('alper_anthem_ara.html')
@app.route('/alper/continent/ara')
def alper_continent_ara():
    return render_template('alper_continent_ara.html')
@app.route('/alper/continent/ar',methods=['GET','POST'])
def continent_ara():
    if request.method=='GET':
        return redirect(url_for('continent_list'))
    else:
        name=request.form['name']
        continents=islem.ar_continent(name)
        return render_template('alper_continent.html',continents=continents)

@app.route('/alper/anthem/ar',methods=['GET','POST'])
def anthem_ara():
    if request.method=='GET':
        return redirect(url_for('anthem_list'))
    else:
        name=request.form['name']
        anthems=islem.ar_anthem(name)
        return render_template('alper_anthem.html',anthems=anthems)



@app.route('/alper/anthemlist')
def anthem_list():
    try:
        anthems=islem.sel_anthem(anthem,'SELECT ID,NAME,LANGUAGE FROM ANTHEMS ORDER BY ID')
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
        continents=islem.sel_continent(continent,'SELECT ID,COUNTRY,CONTINENT,LANGUAGE,ANT FROM CONTINENTS ORDER BY ID' )
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
        ant=request.form['ant']
        try:
            languages=islem.add_continent(id, country, continent, language,ant)
            return redirect(url_for('continent_list'))
        except:
            hata='invalid language,anthem or id(id is key and language and anthem is foreign key)'
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
        ant=request.form['ant']
        try:
            islem.up_continent(id, country, continent, language,ant)
            return redirect(url_for('continent_list'))
        except:
            hata='invalid language,anthem(language,anthem is foreign key)'
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





