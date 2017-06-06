from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from app.api.v1 import tasks
import os
import socket


#connecting to Redis

celeryApp = Celery('tasks', broker='amqp://guest@rabbit1')

@celeryApp.task
def add(x, y):
    return x + y

app = Flask(__name__)

app.register_blueprint(tasks, url_prefix='/api/v1')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
