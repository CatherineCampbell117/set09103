from flask import Flask, g
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