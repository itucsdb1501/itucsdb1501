import datetime
import os

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from team import Team

from storeTeam import StoreTeam


app = Flask(__name__)


@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())



@app.route('/teams', methods=['GET', 'POST'])
def teams_page():
    if request.method == 'GET':
        now = datetime.datetime.now()
        teams = app.store.get_teams()
        return render_template('teams.html', teams=teams, current_time=now.ctime())
    elif 'teams_to_delete' in request.form:
        keys = request.form.getlist('teams_to_delete')
        for key in keys:
            app.store.delete_team(int(key))
        return redirect(url_for('teams_page'))
    else:
      country = request.form['country']
      continent = request.form['continent']
      team = Team(country, continent)
      app.store.add_team(team)
      return redirect(url_for('team_page', key=app.store.last_key))


@app.route('/teams/add')
def team_edit_page():
    now = datetime.datetime.now()
    return render_template('team_edit.html', current_time=now.ctime())


@app.route('/team/<int:key>')
def team_page(key):
    now = datetime.datetime.now()
    team = app.store.get_team(key)
    return render_template('team.html', team=team,
                           current_time=now.ctime())


if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    app.store = StoreTeam()
    app.store.add_team(Team('TURKEY',continent=0))
    app.store.add_team(Team('BRAZIL',continent=0))
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5001, True
    app.run(host='0.0.0.0', port=port, debug=debug)






