from flask import Blueprint, render_template, request, redirect

controller = Blueprint('home', __name__)


@controller.route('/')
def index():
    return render_template("index.html")


@controller.route('/hello')
def hello_world():
    team_name = DemoParser.our_team_name()
    return render_template('hello.html', team_name=team_name)
