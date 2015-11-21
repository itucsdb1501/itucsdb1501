import os
import datetime
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from team import Team
from store import Store
from user import User
from fixture import Fixture
from anthem import Anthem

app = Flask(__name__)

def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn


@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/users', methods=['GET', 'POST'])
def users_page():
    if request.method == 'GET':
        now = datetime.datetime.now()
        users = app.store.get_users()
        return render_template('users.html', users=users, current_time=now.ctime())
    elif 'users_to_delete' in request.form:
        key_users = request.form.getlist('users_to_delete')
        for key_user in key_users:
            app.store.delete_user(int(key_user))
        return redirect(url_for('users_page'))
    else:
      name = request.form['name']
      surname = request.form['surname']
      user = User(name, surname)
      app.store.add_user(user)
      return redirect(url_for('user_page', key_user=app.store.last_key_user))


@app.route('/users/add')
def user_edit_page():
    now = datetime.datetime.now()
    return render_template('user_edit.html', current_time=now.ctime())



@app.route('/user/<int:key_user>')
def user_page(key_user):
    now = datetime.datetime.now()
    user = app.store.get_user(key_user)
    return render_template('user.html', user=user,
                           current_time=now.ctime())

@app.route('/teams', methods=['GET', 'POST'])
def teams_page():
    if request.method == 'GET':
        now = datetime.datetime.now()
        teams = app.store.get_teams()
        return render_template('teams.html', teams=teams, current_time=now.ctime())
    elif 'teams_to_delete' in request.form:
        key_teams = request.form.getlist('teams_to_delete')
        for key_team in key_teams:
            app.store.delete_team(int(key_team))
        return redirect(url_for('teams_page'))
    else:
      country = request.form['country']
      continent = request.form['continent']
      team = Team(country, continent)
      app.store.add_team(team)
      return redirect(url_for('team_page', key_team=app.store.last_key_team))


@app.route('/teams/add')
def team_edit_page():
    now = datetime.datetime.now()
    return render_template('team_edit.html', current_time=now.ctime())


@app.route('/team/<int:key_team>')
def team_page(key_team):
    now = datetime.datetime.now()
    team = app.store.get_team(key_team)
    return render_template('team.html', team=team,
                           current_time=now.ctime())

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


if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    app.store = Store()
    app.store.add_user(User('burak', 'balta'))
    app.store.add_team(Team('TURKEY',"Europe"))
    app.store.add_team(Team('BRAZIL',"America"))
    app.store.add_fixture(Fixture('Usa',"Uk"))
    app.store.add_anthem(Anthem('Turkey',"Istiklal Marsi"))

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






