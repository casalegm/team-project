import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '1029730198'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('home-page.html')


@app.route('/members')
def members_page():
    return render_template('members.html')


@app.route('/tvshows')
def shows_page():
    return render_template('shows.html')


@app.route('/networks')
def networks_page():
    return render_template('networks.html')


if __name__ == '__main__':
    app.run(debug=True)
