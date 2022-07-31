from flask import Flask
app = Flask(__name__)


@app.route('/<name>''<age>')
def home(name,age):
    int()
    return 'Hello ' + name + ' Your age is !'+age


if __name__ == '__main__':
    app.run()


