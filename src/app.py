from flask import Flask, request, jsonify
from typing import Optional
from .database import init_db, session_db


# init db
init_db()


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'message': 'Server is running'}), 200






@app.teardown_appcontext
def shutdown_session(exception=None):
    session_db.remove()

