from flask import FLASK, render_template
app = FLASK(__name__)

@app.route('/hello/<name>')
def hello(name=None):
    user = {'name': name}
    return render_template('hello.html', user=user)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)