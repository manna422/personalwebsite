import os
from flask import (Flask, request, session, g, redirect, url_for, abort,
                   render_template, flash)

app = Flask(__name__)

@app.route('/')
def show_home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
