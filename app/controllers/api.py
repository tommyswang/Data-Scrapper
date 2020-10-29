from flask import Blueprint, render_template


controller = Blueprint('api', __name__)


@controller.route('/api', methods=['GET'])
def api():
    return render_template("api.html")


@controller.route('/api', methods=['POST'])
def create_api_job():
    pass
