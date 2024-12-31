from flask import Flask
# from resources.car_resource import CrudRoute
from database.config import config_database
from routes.config import config_routes


def app_start():

    app = Flask(__name__)

    config_database(app)
    config_routes(app)

    return app


APP = app_start()

if __name__ == '__main__':
    APP.run(debug=True)

