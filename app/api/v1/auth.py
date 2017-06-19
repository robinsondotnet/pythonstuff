import os

from flask import Blueprint, jsonify

from app.services.graph import GraphService

auth = Blueprint('auth', __name__)


@auth.route('/auth/login')
def login():
    graph = GraphService()
    me = graph.get_me()
    try:
        id = me["id"]
    except Exception as e:
        raise
    return jsonify({'result': id})

@auth.route('/auth/signup')
def signup():
    return 'signed up'


