import os
import datetime
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from user import User
from storeUser import StoreUser

app = Flask(__name__)


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
        keys = request.form.getlist('users_to_delete')
        for key in keys:
            app.store.delete_user(int(key))
        return redirect(url_for('users_page'))
    else:
      name = request.form['name']
      surname = request.form['surname']
      user = User(name, surname)
      app.store.add_user(user)
      return redirect(url_for('user_page', key=app.store.last_key))


@app.route('/users/add')
def user_edit_page():
    now = datetime.datetime.now()
    return render_template('user_edit.html', current_time=now.ctime())



@app.route('/user/<int:key>')
def user_page(key):
    now = datetime.datetime.now()
    user = app.store.get_user(key)
    return render_template('user.html', user=user,
                           current_time=now.ctime())



if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    app.store = StoreUser()
    app.store.add_user(User('burak', surname=1980))
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    app.run(host='0.0.0.0', port=port, debug=debug)
