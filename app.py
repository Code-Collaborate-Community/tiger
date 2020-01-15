#!/usr/bin/env python3
from flask import Flask, render_template, request
import mysql
import logging

app = Flask(__name__)


def definedlog(fileHandler):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler(fileHandler)
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s : %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def connect_db():
    connection = mysql.connector.connect(
        user='root', password='LoginPass@@11223344',
        host='localhost', database='tiger')
    return connection


def view_messages():
    connection = connect_db()
    message = connection.cursor()
    message.execute("SELECT * FROM tiger.messages")
    view = message.fetchall()
    for row in view:
        print(row)
    return view


@app.route('/')
def Home():
    return render_template('Home.html')


@app.route('/contact_us')
def contact_us():
    return render_template('/contact_us.html')


@app.route('/log_in', methods=['GET', 'POST'])
# TODO write logic to this function
def log_in():
    if request.method == 'POST':
        return render_template('Home.html')
    return render_template('/sign_up.html')


@app.route('/log_out')
# TODO after seesion will be merge write this function
def log_out():
    return render_template('Home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')


def check_username(username):
    connection = connect_db()
    maulers = connection.cursor()
    Fender = "SELECT * FROM users WHERE username  =" + username
    maulers.execute(Fender)
    result = maulers.fetchall()
    if not result:
        # the user doesnt exist
        return False
    else:
        # the user exists
        return True


@app.route('/check')
def check():
    if check_username('sss'):
        item = "working"
    else:
        item = "no"
    return item
