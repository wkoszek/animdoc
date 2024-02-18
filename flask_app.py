import sqlite3
conn = sqlite3.connect('database.db')
import os
import signal

from flask import Flask

app = Flask(__name__)
from flask import render_template

def fetch_comments():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comments')
    return cursor.fetchall()


@app.route('/')
def main():
    return render_template('main.tpl')

@app.route('/healthcheck')
def healthcheck():
    return 'OK'

@app.route('/comments')
def comments():
    comments = fetch_comments()
    return render_template('comments.tpl', comments=comments)

def signal_handler(signalnum, frame):
    print('Received SIGINT, shutting down.')
    os._exit(0)


signal.signal(signal.SIGINT, signal_handler)