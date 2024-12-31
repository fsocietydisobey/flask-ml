from flask_sqlalchemy import SQLAlchemy
import os



db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))

def config_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()


    # app.config['SQLALCHEMY_DATABASE_URI'] = \
    # '{DBMS}://{user}:{password}@{server}/{database}'.format(
    #     DBMS='mariadb+mariadbconnector',
    #     user='root',
    #     password='123456',
    #     server='localhost',
    #     database='cars'
    # )




