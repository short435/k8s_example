# Created by Zhen-Yi Yu on 2024/03/19

# wsgi and flask libraries
from flask import Flask
from app.config import get_config

def create_app():
    # initialize the Flask app
    app = Flask(__name__)
    # Set up the app config
    app.config.from_object(get_config())

    # Set up blueprint
    from app.route.api import apis
    app.register_blueprint(apis, url_prefix='/')

    return app
