from flask import Blueprint, render_template

controller = Blueprint('html', __name__)


@controller.route('/html', methods=['GET'])
def html():
    return render_template("html.html")


@controller.route('/html', methods=['POST'])
def create_html_job():
    pass
