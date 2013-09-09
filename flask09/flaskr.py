#! /usr/bin/python
#coding=UTF-8
# -*- coding:utf-8 -*-
# filename: flask.py
# author: chengl6500
# date: 20130404-2100
###
#all the imports
from __future__ import with_statement
from contextlib import closing
import sqlite3
import os
import time
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response
from werkzeug import secure_filename

#configuration
DATABASE = './sqlite3.db'
DB_SCRIPT_INIT = './schema.sql'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'upload')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

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

def init_db(db_name = app.config['DATABASE'], db_script_file = app.config['DB_SCRIPT_INIT']):
    """用脚本文件来建立数据库(数据库名， 脚本名)"""
    with closing(connect_db(db_name)) as db:
        with app.open_resource(db_script_file) as f:
            db.cursor().executescript(f.read())
        db.commit()
        print u"数据记录已成功插入到数据库表中！"

def prepare_db(db_name = app.config['DATABASE'], db_script_file = app.config['DB_SCRIPT_INIT']):
    #如果不存在数据库文件则用数据库脚本创建数据库，否则直接返回
    if not os.path.exists(db_name):
        create_table(db= db_name, table = "entries")
        print u"新建数据库。。。。成功！"

        init_db(db_name, db_script_file)
        return connect_db(db_name)
    else:
        print u"在系统上发现了一个历史数据库:" + app.config['DATABASE']
        return connect_db(db_name)

def prepare_db_data():
    #以手工方式插入数据记录到数据库中
    #create_table(app.config['DATABASE'], "entries")
    conn = prepare_db(app.config['DATABASE'])
    onn.execute("insert into entries values(1, 'first title', 'contents of first title')")
    conn.execute("insert into entries values(2, 'second title', 'contents of second title')")

'''@app.before_request
def before_request():
g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
if hasattr(g,'db'):
g.db.close()
'''

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
"""
print filename.rsplit('.', 1)
print filename.rsplit('.', 1)[1]"""

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    navigation = (
        {"href":"index", "caption":"home"},
        {"href":"login", "caption":"login"},
        {"href":"create", "caption":"create"},
        {"href":"about", "caption":"about"},
        {"href":"upload", "caption":"upload_file"}
        )
    # g.db = connect_db()
    if request.method == 'POST':
        file = request.files['file']
        print "upload is ", allowed_file(file.filename)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("upload succeed!")
            # return redirect('uploaded')
        else:
            flash("upload error!")
    return render_template("upload_file.html", username="guest", navigation=navigation)


@app.route('/uploaded')
def uploaded_file():
    return "<html><head><title>upload succeed!</title></head><body>Your upload file is succeed!!</body></html>"

@app.route('/')
@app.route('/index')
def show_entries():
    navigation = (
        {"href":"index", "caption":"home"},
        {"href":"login", "caption":"login"},
        {"href":"create", "caption":"create"},
        {"href":"about", "caption":"about"},
        {"href":"upload", "caption":"upload_file"}
        )
    login_data = {}
    if "username" in session:
        login_data['username'] = session['username']
        print time.ctime(), session['username']

    g.db = prepare_db()
    db_action = "select id, title, text, create_datetime, modifi_datetime, auth from entries"
    cur = g.db.execute(db_action)
    if cur:
        entries = [dict(
                id = row[0],
                title = row[1],
                text = row[2],
                create_datetime = row[3],
                modifi_datetime = row[4],
                author = row[5]
                ) for row in cur.fetchall()]
    else:
        entries = [{
                'id': 'Empty',
                'title': 'Empty',
                'text': 'Empty',
                'create_datetime': 'Empty',
                'modifi_datetime': 'Empty',
                'auth': 'Empty'
                }]

    if entries:
        return render_template('show_entries.html',\
                                   entries=entries,\
                                   navigation=navigation,\
                                   login_data=login_data)
    else:
        return "sorry ,the database is empty!"

@app.route('/about')
def about():
    navigation = (
        {"href":"index", "caption":"home"},
        {"href":"about", "caption":"about"},
        {"href":"login", "caption":"login"},
        {"href":"create", "caption":"create"}
        )
    return render_template("about.html", navigation=navigation)

@app.route('/create')
def create():
    navigation = (
        {"href":"index", "caption":"home"},
        #{"href":"home", "caption":"index"},
        {"href":"about", "caption":"about"},
        {"href":"login", "caption":"login"},
        {"href":"create", "caption":"create"}
        )
    if 'username' not in session:
        flash("login first")
        return redirect(url_for('login'))

    if request.method == "POST":  #nerver into run
        print "this will not running."
        content = {'title':'login_1'}
        return render_template("create.html", cont = content, navigation=navigation)
    else:
        content = {'title':'creating'}
        return render_template("create.html", cont = content, username = session['username'], navigation = navigation)

@app.route('/created', methods=['POST'])
def created():
    navigation = (
        {"href":"index", "caption":"home"},
        {"href":"about", "caption":"about"},
        )
    if not request.form['title'] or not request.form['content']:
        flash("input is empty")
        return redirect(url_for("show_entries"))

    # insert to table
    g.db = prepare_db()
    db_action = 'insert into entries (title, text, create_datetime, auth) values(?, ?, ?, ?)'
    cur = g.db.execute(db_action, [request.form['title'], request.form['content'], time.ctime(), session['username'] ])
    g.db.commit()
    return redirect(url_for("show_entries"))

@app.route('/myip')
def response_me():
    if request:
        #response = make_response("<html><head><title>make response</title></head><body>Body</body></html>")
        response = make_response(request.remote_addr)
    #response.headers['X-parachtes'] = 'parachutes are cool'
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    navigation = (
        {"href":"index", "caption":"home"},
        {"href":"about", "caption":"about"},
        {"href":"login", "caption":"login"},
        )
    error = None
    if 'username' in session:
        flash("already loggin")
        return redirect(url_for('show_entries'))

    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return login_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password, try again!'

    return render_template('login.html', error=error, navigation=navigation)


def valid_login(username="None", password="None"):
    if username == "admin" and password == "admin":
        session['username'] = 'admin'
        return True
    else:
        return None

def login_the_user_in(username="None"):
    navigation = (
        {"href":"index", "caption":"home"},
        {"href":"about", "caption":"about"},
        {"href":"logout", "caption":"logout"}
        )
    return redirect(url_for("show_entries"))
    #return render_template("index.html", username=username, navigation=navigation)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for("show_entries"))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
