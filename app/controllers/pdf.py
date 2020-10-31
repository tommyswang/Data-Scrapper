from flask import Blueprint, render_template

controller = Blueprint('pdf', __name__)


@controller.route('/pdf', methods=['GET'])
def pdf():
    return render_template("pdf.html")


@controller.route('/pdf', methods=['POST'])
def create_pdf_job():
    pass

