import os
from dotenv import load_dotenv
from urllib import parse

import psycopg2
import psycopg2.extras
import click

from flask.cli import with_appcontext
from flask import g

from app import current_app as app

def get_db():
    "store connection to database in a current-request-context variable"

    basedir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(basedir, '.env'))

    parse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ.get("DATABASE_URL"))

    if 'db' not in g:
        g.db = psycopg2.connect(
            database = url.path[1:], 
            user = url.username, 
            password = url.password, 
            host = url.hostname, 
            port = url.port
        )
        # puedo devolver solo db (habiendo antes creado el atributo de g)
        return g.db

# teardown_appcontext() registers a function to be called when the application context ends. 
@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    "Creates the table for the database."
    db = get_db()

    with app.open_resource('schema.sql') as schema:
        cursor = db.cursor()
        cursor.execute(schema.read().decode('utf8'))
        db.commit()

# click.command() defines a command line command called init-db that calls the init_db
@click.command('init-db')
@with_appcontext
def init_db_command():
    "Creates the database with postgresql."
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    "close_db and init_db_command functions need to be registered with the application instance"
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


class Query():

    def __init__(self,):
        self.connect = get_db()
        self.cursor = self.connect.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def select_by_name(self, name):
        self.cursor.execute("""select * from users WHERE username = '{}';""".format(name))
        self.connect.commit()
        user = self.cursor.fetchone()
        return user

    def select_by_id(self, user_id):
        self.cursor.execute("""select * from users WHERE id = '{}';""".format(user_id))
        self.connect.commit()
        user = self.cursor.fetchone()
        return user

    def insert_user(self, name, email, passw):
        self.cursor.execute("""insert into users 
            (username, email, password) 
            values ('{}', '{}', crypt('{}', gen_salt('bf')));""".format(name, email, passw))
        self.connect.commit()

    def check_email(self, email):
        self.cursor.execute("""select * from users where email = '{}';""".format(email))
        self.connect.commit()
        row = self.cursor.fetchone()
        return row

    def check_password(self, passw):
        self.cursor.execute("""select * from users where password = crypt('{}', password);""".format(passw))
        self.connect.commit()
        row = self.cursor.fetchone()
        return row