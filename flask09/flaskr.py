# -*- coding:utf-8 -*-
#all the imports
from __future__ import with_statement
from contextlib import closing
import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for,\
	abort, render_template, flash

#configuration
DATABASE = './sqlite3.db'
DB_SCRIPT = './schema.sql'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FALSKR_SETTINGS', silent=True)

def connect_db(db_name = app.config['DATABASE']):
    return sqlite3.connect(db_name)

def create_table(db, table):
    """手动建立数据库(数据库名， 表名)"""
    conn = connect_db(db)
    conn.execute("create table if not exists " + table + "(id integer primary key autoincrement, title string not null, text string not null, create_datetime date default datetime, modifi_datetime date, auth string)")
    conn.commit()

def init_db(db_name = app.config['DATABASE'], db_script_file = app.config['DB_SCRIPT']):
    """用脚本文件来建立数据库(数据库名， 脚本名)"""
    with closing(connect_db(db_name)) as db:
        with app.open_resource(db_script_file) as f:
            db.cursor().executescript(f.read())
        db.commit()

def prepare_db(db_name = app.config['DATABASE'], db_script_file = app.config['DB_SCRIPT']):
    #如果不存在数据库文件则用数据库脚本创建数据库，否则直接返回
    if not os.path.exists(db_name):
        create_table(db= db_name, table = "entries")
        init_db(db_name, db_script_file)
        print u"新建数据库。。。。成功！"
        return connect_db(db_name)
    else:
        print u"在系统上发现了一个历史数据库:" + app.config['DATABASE']
        return connect_db(db_name)
    #以手工方式创建数据库
    #create_table(app.config['DATABASE'], "entries")
    #conn = connect_db(app.config['DATABASE'])
    #conn.execute("insert into entries values(1, 'first title', 'contents of first title')")
    #conn.execute("insert into entries values(2, 'second title', 'contents of second title')")

'''@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g,'db'):
        g.db.close()
'''

def valid_login(username="None", password="None"):
    if username == "admin" and password == "admin":
        #return "Welcome %s" % username
        session['username'] = 'admin'
        return True
    else:
        return None

def login_the_user_in(username="None"):
    navigation = (
        {"href":"home", "caption":"home"},
        {"href":"about", "caption":"about"},
        {"href":"logout", "caption":"logout"}
        )
    return render_template("index.html", username=username, navigation=navigation)

@app.route('/')
@app.route('/home')
def show_entries():
    navigation = (
        {"href":"home", "caption":"home"},
        {"href":"about", "caption":"about"},
        {"href":"login", "caption":"login"},
        {"href":"create", "caption":"create"}
        )
    # g.db = connect_db()
    g.db = prepare_db()
    cur = g.db.execute('select title,text,create_datetime,modifi_datetime,auth from entries ')
    if cur:
        entries = [dict(
            title=row[0],
            text=row[1],
            create_datetime=row[2],
            modifi_datetime=row[3],
            author=row[4]
            ) for row in cur.fetchall()]
    else:
        entries = [{
            'title':'Empty',
            'text':'Empty',
            'create_datetime':'Empty',
            'modifi_datetime':'Empty',
            'auth':'Empty'
            }]

    if entries:
        return render_template('show_entries.html',\
            entries=entries, navigation=navigation)
    else:
        return "sorry ,the database is empty!"

@app.route('/about')
def about():
    navigation = (
        {"href":"home", "caption":"home"},
        {"href":"about", "caption":"about"},
        {"href":"login", "caption":"login"},
        {"href":"create", "caption":"create"}
    )
    return render_template("about.html", navigation=navigation)

@app.route('/create')
def create():
    navigation = (
        {"href":"home", "caption":"home"},
        {"href":"about", "caption":"about"},
        {"href":"login", "caption":"login"},
        {"href":"create", "caption":"create"}
    )
    if 'username' not in session:
        flash("login first")
        return redirect('login')

    if request.method == "POST":
        content = {'title':'login_1'}
        return render_template("create.html", cont = content, navigation=navigation)
    else:
        content = {'title':'login_2'}
        return render_template("create.html", cont = content, username = session['username'], navigation = navigation)

@app.route('/created', methods=['POST'])
def created():
    navigation = (
         {"href":"home", "caption":"home"},
         {"href":"about", "caption":"about"},
         {"href":"login", "caption":"login"}
    )
    content = {'title':'created'}
    content["input_title"] = request.form['title']
    content["input_content"] = request.form['content']
    return render_template("created.html", navigation = navigation, cont = content)

@app.route('/login', methods=['GET', 'POST'])
def login():
    navigation = (
        {"href":"home", "caption":"home"},
        {"href":"about", "caption":"about"},
        {"href":"login", "caption":"login"},
        {"href":"create", "caption":"create"}
    )
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return login_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password, try again!'

    return render_template('login.html', error=error, navigation=navigation)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect("home")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
