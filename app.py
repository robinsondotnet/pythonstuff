from flask import Flask, render_template
from celery import Celery
from app.api.v1 import tasks, auth


celeryApp = Celery('tasks', broker='amqp://guest@rabbit1')

@celeryApp.task
def add(x, y):
    return x + y

app = Flask(__name__)

# TODO: Register as group for /api/v1/
app.register_blueprint(tasks, url_prefix='/api/v1')
app.register_blueprint(auth, url_prefix='/api/v1')

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
    app.run(host='0.0.0.0', port=80)
