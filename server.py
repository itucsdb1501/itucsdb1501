
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
from fixture import Fixture
from anthem import Anthem

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

@app.route('/fixtures', methods=['GET', 'POST'])
def fixtures_page():
    if request.method == 'GET':
        now = datetime.datetime.now()
        fixtures = app.store.get_fixtures()
        return render_template('fixtures.html', fixtures=fixtures, current_time=now.ctime())
    elif 'fixtures_to_delete' in request.form:
        key_fixtures = request.form.getlist('fixtures_to_delete')
        for key_fixture in key_fixtures:
            app.store.delete_fixture(int(key_fixture))
        return redirect(url_for('fixtures_page'))
    else:
      team1 = request.form['team1']
      team2 = request.form['team2']
      fixture = Fixture(team1, team2)
      app.store.add_fixture(fixture)
      return redirect(url_for('fixture_page', key_fixture=app.store.last_key_fixture))


@app.route('/fixtures/add')
def fixture_edit_page():
    now = datetime.datetime.now()
    return render_template('fixture_edit.html', current_time=now.ctime())



@app.route('/fixture/<int:key_fixture>')
def fixture_page(key_fixture):
    now = datetime.datetime.now()
    fixture = app.store.get_fixture(key_fixture)
    return render_template('fixture.html', fixture=fixture,
                           current_time=now.ctime())







#alper

@app.route('/anthems', methods=['GET', 'POST'])
def anthems_page():
    if request.method == 'GET':
        now = datetime.datetime.now()
        anthems = app.store.get_anthems()
        return render_template('anthems.html', anthems=anthems, current_time=now.ctime())
    elif 'anthems_to_delete' in request.form:
        key_anthems = request.form.getlist('anthems_to_delete')
        for key_anthem in key_anthems:
            app.store.delete_anthem(int(key_anthem))
        return redirect(url_for('anthems_page'))
    else:
      country = request.form['country']
      name = request.form['name']
      anthem = Anthem(country, name)
      app.store.add_anthem(anthem)
      return redirect(url_for('anthem_page', key_anthem=app.store.last_key_anthem))


@app.route('/anthems/add')
def anthem_edit_page():
    now = datetime.datetime.now()
    return render_template('anthem_edit.html', current_time=now.ctime())


@app.route('/anthem/<int:key_anthem>')
def anthem_page(key_anthem):
    now = datetime.datetime.now()
    anthem = app.store.get_anthem(key_anthem)
    return render_template('anthem.html', anthem=anthem,
                           current_time=now.ctime())


@app.route('/initdb')
def initialize_database():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor=connection.cursor()


        #query="""DROP TABLE IF EXIST ANTHEM"""
        #cursor.execute(query)

        #
        query="""CREATE TABLE ANTHEM (id INTEGER,name VARCHAR(15))"""
        cursor.execute(query)
        #
        query="""CREATE TABLE LANGUAGES(id INTEGER,name VARCHAR(15))"""
        cursor.execute(query)
        query="""INSERT INTO ANTHEM (id,name) VALUES (0,'Istiklal Marsi')"""
        cursor.execute(query)
        query="""INSERT INTO ANTHEM (id,name) VALUES (1,'Deneme')"""
        cursor.execute(query)

        query="""UPDATE ANTHEM SET id=2 WHERE id=0"""
        cursor.execute(query)

        query="""DELETE FROM ANTHEM WHERE id=1"""
        cursor.execute(query)

        connection.commit()
    return redirect(url_for('home_page'))

@app.route('/deneme')
def counter_page():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor=connection.cursor()



        query="SELECT name FROM ANTHEM"
        cursor.execute(query)


        isim=cursor.fetchone()[0]
        return "%s" %isim


 #alper


'''
projeyinin calismasini engelledigi icin comment out ettik
@app.route('/deneme')
def counter_page():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor=connection.cursor()

        query="SELECT name FROM ANTHEM"
        cursor.execute(query)

        isim=cursor.fetchone()[0]
        return "%s" %isim
'''

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





