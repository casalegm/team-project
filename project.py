import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '1029730198'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class Network(db.Model):
    __tablename__ = 'networks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.Text)
    shows = db.relationship('Show', backref='network')


class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    network_id = db.Column(db.Integer, db.ForeignKey('networks.id'))


@app.route('/')
def index():
    return render_template('home-page.html')


@app.route('/members')
def members_page():
    return render_template('members.html')


@app.route('/shows')
def shows_page():
    shows = Show.query.all()
    return render_template('tvshow-all.html', shows=shows)


@app.route('/networks')
def networks_page():
    networks = Network.query.all()
    return render_template('network-all.html', networks=networks)


if __name__ == '__main__':
    app.run(debug=True)
