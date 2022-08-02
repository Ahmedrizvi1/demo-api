from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return 'Hello!'


@app.route("/wow")
def wow():
    return 'wow!'

if __name__ == '__main__':
    app.run()


