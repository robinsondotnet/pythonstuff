from flask import Flask
from redis import Redis, RedisError
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from celery import Celery
import os
import socket


#connecting to Redis

celeryApp = Celery('tasks', broker='amqp://guest@rabbit1')

@celeryApp.task
def add(x, y):
    return x + y



app = Flask(__name__)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()

@app.route("/")
def Hello():
    try:
        myuser = User('kento\'s User')
        db.session.add(myuser)
        db.session.commit()

        users = User.query.all()

        visits = ''

        for user in users:
            visits  += "id:{0} username:{1}".format(user.id, user.username)

    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3> Hello {name}! </h3>"\
           "<b> Hostname:</b> {hostname}<br />" \
           "<b> Visits: </b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname= socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
