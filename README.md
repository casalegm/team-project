# team-project
Team project for Abby Sawyer, Alexis Newton, and Gina Casale.
This is a team project that will create a database for TV shows that will list out the name of the tv show along with the main cast members and the year the show was created, along with the network the show plays on. This database will work with 2 tables: a show table that lists all the shows and a network table that lists out networks that shows play on. The relationship will be one network has many shows.
A show can only have one network, but a network can contain many shows.

## running the application

* if you don't have virtual environment, set it up
  * $ virtualenv venv

* activate the virtual environment
  * $ source venv/bin/activate

* install packages
  * $ pip install -r requirements.txt

* initialize the database
  * $ python manage.py deploy

* run the development server with the debugger on
  * $ python manage.py runserver -d
