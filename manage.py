from flask_script import Manager
from project import app, db, Network, Show

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    CW = Network(name='The CW', description='CW Television Network')
    ABC = Network(name='ABC', description='American Broadcasting Company Television Network')
    NBC = Network(name='NBC', description='The National Broadcasting Company')
    Greys = Show(title='Greys Anatomy', year=2005, description='The medical drama series focuses on a group of doctors at a hospital in Seattle, including several who began their careers at the facility as interns.', network=ABC)
    Supernatural = Show(title='Supernatural', year=2005, description='This haunting series follows the thrilling yet terrifying journeys of Sam and Dean Winchester, two brothers who face an increasingly sinister landscape as they hunt monsters.', network=CW)
    Friends = Show(title='Friends', year=1994, description='Three young men and three young women - of the BFF kind - live in the same apartment complex and face life and love in New York. ', network=NBC)
    db.session.add(CW)
    db.session.add(ABC)
    db.session.add(NBC)
    db.session.add(Greys)
    db.session.add(Supernatural)
    db.session.add(Friends)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
