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

@app.route('/tvshow/add', methods=['GET', 'POST'])
def add_shows():
    if request.method == 'GET':
        networks = Network.query.all()
        return render_template('tvshow-add.html', networks=networks)
    if request.method == 'POST':
        # get data from the form
        title = request.form['title']
        year = request.form['year']
        description = request.form['description']
        network_name = request.form['network']
        network = Network.query.filter_by(name=network_name).first()
        show = Show(title=title, year=year, description=description, network=network)

        # insert the data into the database
        db.session.add(show)
        db.session.commit()
        return redirect(url_for('shows_page'))


@app.route('/networks')
def networks_page():
    networks = Network.query.all()
    return render_template('network-all.html', networks=networks)

@app.route('/network/add', methods=['GET', 'POST'])
def add_networks():
    if request.method == 'GET':
        return render_template('network-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        description = request.form['description']

        # insert the data into the database
        network = Network(name=name, description=description)
        db.session.add(network)
        db.session.commit()
        return redirect(url_for('networks_page'))


if __name__ == '__main__':
    app.run(debug=True)
