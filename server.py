from os import path
from sqlite3 import dbapi2 as sqlite3
from flask import (Flask, request, session, g, redirect, url_for, abort,
                   render_template, flash)

app = Flask(__name__)

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect(path.join(app.root_path, 'blog.db'))
    return g.sqlite_db


@app.route('/')
def show_home():
    db = get_db()
    cur = db.execute('select date, time, title, text, icon from entries order by id desc')
    raw = cur.fetchall()
    entries = []
    for entry in raw:
	entries.append({'date':entry[0], 'time':entry[1], 'title':entry[2],
            'text':entry[3], 'icon':entry[4]})
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
