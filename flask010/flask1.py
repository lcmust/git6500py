# -*- coding: utf-8 -*-
from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import redirect
from flask import escape
from flask import g
from flask import flash
from contextlib import closing
import time
import sqlite3

FLASK_SETTINGS = './flask.config'

app = Flask(__name__)
app.config.from_pyfile(FLASK_SETTINGS, silent=False)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select id, title, text from entries order by id desc')
    entries = [dict(id=row[0], title=row[1], text=row[2],) for row in cur.fetchall()]
    """
    print time.ctime() + ", and session is bellow:"
    for tmp in request.cookies:
        print tmp, request.cookies[tmp]
    """
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    if not request.form['title'] or not request.form['text']:
        flash("your input is empty, input again!")
        return redirect(url_for('show_entries'))
    g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

if __name__ == '__main__':
    app.debug=True
    print "It's time is:" + time.ctime() + ", and server is beginning..."
    app.run(host="0.0.0.0")
