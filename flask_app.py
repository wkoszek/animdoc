import os
import signal

from flask import Flask

app = Flask(__name__)
from flask import render_template

@app.route('/')
def main():
    return render_template('main.tpl')

@app.route('/healthcheck')
def healthcheck():
    return 'OK'


def signal_handler(signalnum, frame):
    print('Received SIGINT, shutting down.')
    os._exit(0)


signal.signal(signal.SIGINT, signal_handler)