"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        def initials(self):
            return "{}. {}.".format(self.firstname[0], self.lastname[0])





@app.route('/')
@app.route('/index')


def index():
    return render_template('index.html', title ="Cybernality",
                           user=User("Huerta", "Christopher"))

@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)
