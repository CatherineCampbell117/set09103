from flask import Flask, g, request, jsonify
import sqlite3

app = Flask(__name__)
db_location = 'song.db'

def get_db():
    db = gettattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect (db_location)
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db')

@app.route('/')
def hello_world():
    return 'This is my first API call!'

@app.route('/post', method=["POST"])
def testpost():
    input_json = request.get_json(force=True)
    dictToReturn = {'text':input_json['text']}
    return jsonify(dictToReturn)