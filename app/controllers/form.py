from flask import Blueprint, render_template

controller = Blueprint('form', __name__)
app.config['APPLICATION_ROOT'] = '/data-scrapper-app'

@controller.route('/form', methods=['GET'])
def form():
    return render_template("form.html")


@controller.route('/form', methods=['POST'])
def create_form_job():
    pass
