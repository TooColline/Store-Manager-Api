from flask import Flask

from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__)

    return app