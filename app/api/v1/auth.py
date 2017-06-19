from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)


@auth.route('/auth/login')
def login():
    return jsonify({"success": True})

@auth.route('/auth/signup')
def signup():
    return 'signed up'


