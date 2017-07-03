from flask import Flask, render_template
from app.api.v1 import tasks, auth
from app.utils.bootstrap import Bootstrap
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
# celeryApp = Celery('tasks', broker='amqp://guest@rabbit1')
#
# @celeryApp.task
# def add(x, y):
#     return x + y

app = Flask(__name__)

api_bootstrap = Bootstrap('/api/v1')
api_bootstrap.register_blueprints(app, [tasks, auth])

@app.route('/')
def index():
    """
    Home Page
    """
    return render_template('index.html')

@app.route('/login')
def login():
    """
    Login Page
    """
    return 'login'

@app.route('/signup')
def signup():
    """
    Signup Page
    """
    return 'signup'

if __name__ == "__main__":
    app.run()
