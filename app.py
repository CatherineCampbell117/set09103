from flask import Flask, g, request, jsonify, render_template,
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

@app.route('/')
def getsongs(search):
    conn = sqlite3.connect(song.db)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM `songs` WHERE `title` LIKE ? OR `lyrics` LIKE ?",
        ("%"+search+"%", "%"+search+"%",)
    )
    results = cursor.fetchall()
    conn.close()
    return results 

@app.route('/post', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = dict(request.form)
        songs = getsongs(data["search"])
    else:
        songs = []
    return render_template("results.html", sgs=songs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)