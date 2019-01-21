from flask import Flask
import settings
from db import db
from api.categories import categories


app = Flask (__name__)

def config_app(server):
    server.config['SERVER_NAME'] = settings.FLASK_SERVER
    server.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS


def main():
    config_app(app)

    app.register_blueprint(categories, url_prefix='/api/categories')

    db.init_app(app)
    app.run(debug=settings.FLASK_DEBUG)


if __name__== '__main__':
    main()