
#!/usr/bin/env python3

from flask import Flask, jsonify, render_template

from flask_cors import CORS
from controllers.api import controller as api_controller
from controllers.pdf import controller as pdf_controller
from controllers.html import controller as html_controller
from controllers.form import controller as form_controller
from controllers.home import controller as home_controller

from db import db
import os
from os import path
import pathlib

import logging

env_name = os.environ.get('ENV', 'dev_local')  # default ENV is dev_local


def create_app(testing=False):
    app = Flask(__name__, template_folder='templates',
                static_folder='static', static_url_path='')
    app.config.from_object(__name__)
    app.logger.setLevel(logging.INFO)

    # config environment
    current_abs_path = pathlib.Path(__file__).resolve().parents[0]
    config_file_path = f"{current_abs_path}/configs/{env_name}.py"
    if not path.exists(config_file_path):
        app.logger.error(
            f"Config file for ENV {env_name} at path {config_file_path} does not exist. Exit.")
        exit(1)
    else:
        app.logger.info(f"Loads config from {config_file_path}")
    app.config.from_pyfile(config_file_path)

    CORS(app, resources={r'/*': {'origins': '*'}})

    # register controllers
    app.register_blueprint(home_controller)
    app.register_blueprint(api_controller)
    app.register_blueprint(pdf_controller)
    app.register_blueprint(html_controller)
    app.register_blueprint(form_controller)

    return app


if __name__ == "__main__":
    env_name = os.environ.get('ENV', 'dev_local')  # default ENV is dev_local

    app = create_app()
    app.logger.info(f"Environment: {env_name}")
    app.app_context().push()

    from models.scrape_file import ScrapeFile
    from models.scrape_job import ScrapeJob
    db.init_app(app)

    # migrate database
    db.create_all()
    db.session.commit()

    app.run(host='0.0.0.0', port=5000, debug=True)
