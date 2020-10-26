#!/usr/bin/env python3

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

# format here is:
# from <relative module file name> import <class name>
from flask_cors import CORS
from lib.parsers.demo_parser import DemoParser

app = Flask(__name__, template_folder = 'templates', static_folder = 'static', static_url_path = '')
app.config.from_object(__name__)

''' 
    SQLAlchemy Setup 
    TODO: use OS variables or config file - hard code for now
    This is our MySQL DB hosted on cloud, for now lets keep it like this 
    so project will build and we can keep working
'''
DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='abc123456', server='155.138.217.198', database='data_scrper')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABSE_URI
db = SQLAlchemy(app)

from lib.entity.ScrapeFile import ScrapeFile
from lib.entity.ScrapeJob import ScrapeJob

@app.route('/')
def index():
    return render_template("index.html")


CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/api', methods=['GET'])
def api():
    return render_template("api.html")


@app.route('/api', methods=['POST'])
def create_api_job():
    pass


@app.route('/form', methods=['GET'])
def form():
    return render_template("form.html")


@app.route('/form', methods=['POST'])
def create_form_job():
    pass


@app.route('/html', methods=['GET'])
def html():
    return render_template("html.html")


@app.route('/html', methods=['POST'])
def create_html_job():
    pass


@app.route('/pdf', methods=['GET'])
def pdf():
    return render_template("pdf.html")


@app.route('/pdf', methods=['POST'])
def create_pdf_job():
    pass

# sanity check route

@app.route('/hello')
def hello_world():
    team_name = DemoParser.our_team_name()
    return render_template('hello.html', team_name=team_name)


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
    app.run(host='0.0.0.0', port=5000, debug=True)
