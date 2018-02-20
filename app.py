from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def todo():
        return "Hello!"


@app.route('/new', methods=['POST'])
def new():
        redirect(url_for('todo'))

if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)        