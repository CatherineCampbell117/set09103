from flask import Flask, g, request, jsonify, render_template
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
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        db.commit()

def init_db():
    with app.app_context():
        db = get_db()
        db.commit()

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/post', methods=["POST"])
def testpost():
    input_json = request.get_json(force=True)
    dictToReturn = {'text':input_json['text']}
    return jsonify(dictToReturn)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)