
#!/usr/bin/env python3

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS
from controllers.api import controller as api_controller
from controllers.pdf import controller as pdf_controller
from controllers.html import controller as html_controller
from controllers.form import controller as form_controller


def create_app():
    app = Flask(__name__, template_folder='templates',
                static_folder='static', static_url_path='')
    app.config.from_object(__name__)

    # from lib.entity.ScrapeFile import ScrapeFile
    # from lib.entity.ScrapeJob import ScrapeJob

    @app.route('/')
    def index():
        return render_template("index.html")

    CORS(app, resources={r'/*': {'origins': '*'}})

    app.register_blueprint(api_controller)
    app.register_blueprint(pdf_controller)
    app.register_blueprint(html_controller)
    app.register_blueprint(form_controller)

    @app.route('/job/<hash>')
    def get_job(hash):
        return "Building. You are trying to access job " + str(hash)

    # sanity check route

    @app.route('/hello')
    def hello_world():
        team_name = DemoParser.our_team_name()
        return render_template('hello.html', team_name=team_name)

    return app


app = create_app()

'''
    SQLAlchemy Setup
    TODO: use OS variables or config file - hard code for now
    This is our MySQL DB hosted on cloud, for now lets keep it like this
    so project will build and we can keep working
'''
DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='root', password='abc123456', server='155.138.217.198', database='data_scrper')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABSE_URI
db = SQLAlchemy(app)

db.create_all()
db.session.commit()
app.run(host='0.0.0.0', port=5000, debug=True)
