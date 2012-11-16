#!/usr/bin/python
#coding=utf8
# all the imports
from __future__ import with_statement
from contextlib import closing
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import sys, os

# configuration
DATABASE = './flaskr.db'
DB_SCRIPT = './schema.sql'
DEBUG = True
SECRET_KEY = 'development key'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_pyfile('settings.py')


def connect_db(db_name):  #返回对数据库的连接句柄
    #return sqlite3.connect(app.config['DATABASE'])
    return sqlite3.connect(db_name)
	
def create_table(db_name, table_name):  #手动建立数据库(数据库名， 表名)
    conn = sqlite3.connect(db_name)
    conn.execute("create table if not exists " + table_name + "(id integer primary key autoincrement, title string not null, text string not null)")
    conn.commit()
	
def init_db(db_name, db_script):   #用脚本文件来建立数据库(数据库名， 脚本名)
    with closing(connect_db(db_name)) as db:
        with app.open_resource(db_script) as f:
            db.cursor().executescript(f.read())
        db.commit()
	
def prepare_db():
    #如果不存在数据库文件则用数据库脚本创建数据库，否则直接返回
    if not os.path.exists(app.config['DATABASE']):
        init_db(app.config['DATABASE'], app.config['DB_SCRIPT'])
        print u"新建数据库。。。。成功！"
        return
    else:
        print u"在系统上发现了一个历史数据库:" + app.config['DATABASE']
        return
    #以手工方式创建数据库
    #create_table(app.config['DATABASE'], "entries")
    #conn = connect_db(app.config['DATABASE'])
    #conn.execute("insert into entries values(1, 'first title', 'contents of first title')")
    #conn.execute("insert into entries values(2, 'second title', 'contents of second title')")

@app.before_request
def before_request():
    g.db = connect_db(app.config['DATABASE'])

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']\
               or request.form['password'] != app.config['PASSWORD'] :
            error = "Invalid username OR password"
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/loggout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run()
