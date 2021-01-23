import time

from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/')
def index():
    return "Hello!"

