from flask import Flask
import os

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DEBUG = True
SECRET_KEY = 'some_key'

# create app
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return 'hello from index'


if __name__ == '__main__':
    app.run()
