from flask import Flask,render_template

app = Flask(__name__)

odp = 'Odopwiedź'

@app.route("/")
def hello_world():
    return '<p>Hej</p>'


def cos():
    return render_template('strona.html')
