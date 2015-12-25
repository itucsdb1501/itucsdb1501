Parts Implemented by Burak Balta
================================
  Three tables *users*, *news*, and *comments* are implemented by developer part using Python, PostgreSql and Vagrant on local. Those objects have in the order users.py, news.py, comments.py python files beside server.py and init.py. Also, there are html file for using text box, check box and button in design part.
  First of all, the implementation logic works running of server.py file. There is part that *"import psycopg2 as dbapi2"* is used as an adaptor to make access for PostgreSql connection. Also, there is an import line for Flask to benefit from its facility which makes the connection between userface and development part of project.


Users Operations
++++++++++++++++
    In order to perform Users operations which are add, delete, update and search, there created a table for users object. In the following a query is used which represents its table structure:

Table Structure
+++++++++++++++
  .. code-block:: sql

     CREATE TABLE users (
               id_user SERIAL PRIMARY KEY,
               kuladi VARCHAR(40),
               password VARCHAR(40)
               )

    *This SQL table code block takes place as a query in init.py file. But there should be another query before which is for control of table. It is actually used to drop the table and other objects which depend on it. Also, the realization of query happens in the order of connection of cursor, writing the query, and execution of the query. After creating the table, with some queries for insertion to fill the table and connection.commit() are realized. This actually happens for every object.

    Database Operations
   ++++++++++++++++++

  .. code-block:: python
    .. highlight:: python
      :emphasize-lines: 3,5

    class Users:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_userlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_user(self, id_user):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE id_user = '%s'" % (id_user)
        cursor.execute(query)
        connection.commit()

    def add_user(self, kuladi,password):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO users (kuladi,password) VALUES ('%s','%s')" % (kuladi,password)
        cursor.execute(query)
        connection.commit()
        return

    def update_user(self, id_user, kuladi,password):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE users SET kuladi = '%s',password='%s' WHERE id_user = '%s'" % (kuladi,password, id_user)
        cursor.execute(query)
        connection.commit()
        return

    def search_user(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE kuladi LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def control_user(self,kuladi,password):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE kuladi LIKE '%s' AND password LIKE '%s'" % (kuladi,password)
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            return 1
        else:
            return 0

   In the above code, there can be seen Users class and its functions. For every defined function, there is different queries to be executed.


News Operations
+++++++++++++++

    Table structure for News object is like in the following which takes place in *init.py* file:

Table Structure
+++++++++++++++
  .. code-block:: sql

     CREATE TABLE news (
               id_new SERIAL PRIMARY KEY,
               title VARCHAR(40),
               content VARCHAR(40),
               country VARCHAR(40) REFERENCES teams(country) ON UPDATE CASCADE ON DELETE CASCADE
            )

    In the following, there is a part of implementation for News object including initialization for competitions class, for obtaining news list, and other important operations such as delete, add, update and search which occurs in *news.py* file.

Database Structure
++++++++++++++++++
  .. code-block:: python
    :linenos
      .. highlight:: python

  class News:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_newlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM news"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_new(self, id_new):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM news WHERE id_new = '%s'" % (id_new)
        cursor.execute(query)
        connection.commit()
        return

    def add_new(self,title,content,country):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT country FROM teams WHERE country= '%s'" % (country)
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            query = "INSERT INTO news (title,content,country) VALUES ('%s','%s','%s')" % (title,content,country)
            cursor.execute(query)
        else:
            query = "INSERT INTO teams (country) VALUES ('%s')" % (country)
            cursor.execute(query)
            query = "INSERT INTO news (title,content,country) VALUES ('%s','%s','%s')" % (title,content,country)
            cursor.execute(query)

        connection.commit()
        return

    def update_new(self, id_new, title,content):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE news SET title = '%s', content='%s' WHERE id_new = '%s'" % (title, content, id_new)
        cursor.execute(query)
        connection.commit()
        return

    def search_new(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM news WHERE title LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows


Comments Operations
+++++++++++++++++++

    Table structure for Comments object is like in the following which takes place in *init.py* file:

Table Structure
+++++++++++++++
 .. code-block:: sql

    CREATE TABLE fixtures (
                id_fixture SERIAL PRIMARY KEY,
                week VARCHAR(40)
            )

    In the following, there is a part of implementation for comments object including initialization for fixtures class, to obtain competitions list, and other important operations such as delete, add, update and search which occurs in *comments.py* file.

Database Structure
++++++++++++++++++
  .. code-block:: python
    :linenos
      .. highlight:: python

   class Comments:

    def __init__(self, cp):
        self.cp = cp
        return

    def get_commentlist(self):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM comments"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def delete_comment(self, id_comment):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "DELETE FROM comments WHERE id_comment = '%s'" % (id_comment)
        cursor.execute(query)
        connection.commit()
        return

    def add_comment(self, name,article,id_new):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "INSERT INTO comments (name,article,id_new) VALUES ('%s','%s','%s')" % (name,article,id_new)
        cursor.execute(query)
        connection.commit()
        return

    def update_comment(self, id_comment, name , article):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "UPDATE comments SET name = '%s', article='%s' WHERE id_comment = '%s'" % (name, article, id_comment)
        cursor.execute(query)
        connection.commit()
        return

    def search_comment(self,name):
        connection = dbapi2.connect(self.cp)
        cursor = connection.cursor()
        query = "SELECT * FROM comments WHERE name LIKE '%s'" % (name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    * What is more, all these python files actually works on server.py file. After development and compilation part, when the server.py is opened program is run. It can be said that how the all python and html parts work together is explained in details in the following:
    * First of all, there is some part of implementation in server.py which can be called main part.

    * The part for the objects in the order of users, news and comments.

  .. code-block:: python
    :linenos
      .. highlight:: python

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

    * Secondly, there comes for news:

  .. code-block:: python
   :linen

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

    * Lastly, comments part comes in server.py file:

  .. code-block:: python
    :linenos
      .. highlight:: python

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


    * All the implementation logic works like when the request comes from html page which flask framework works for this part, the request is considered for any wanted operation. Request form is filled by the coming request.

    *After that, data passed as parameter to the called function from object's python file. This is where the queries work. Finally, the result would be returned which is seen on the user page website.
