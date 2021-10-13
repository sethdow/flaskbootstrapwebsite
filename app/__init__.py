from flask_mongoengine import MongoEngine
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, url_for
from config import config

db = MongoEngine()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    bootstrap.init_app(app)
    # needs configs to init database
    app.config.from_object(config['default'])
    config['default'].init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


