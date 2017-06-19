from flask import Blueprint
# from pyspark import SparkContext
# from pyspark.streaming import StreamingContext

tasks = Blueprint('tasks', __name__)


@tasks.route('/tasks/')
def get():
    return 'hola desde resource module (blueprint)'
