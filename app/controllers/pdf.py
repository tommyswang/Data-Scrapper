from flask import Blueprint, render_template, request, redirect
from db import db
from models.scrape_file import ScrapeFile

controller = Blueprint('pdf', __name__)


@controller.route('/pdf', methods=['GET'])
def pdf():
    return render_template("pdf.html")


@controller.route('/pdf', methods=['POST'])
def create_pdf_job():
    file = request.files['file']

    if file.filename:
        sf = ScrapeFile(file)
        db.session.add(sf)
        db.session.commit()
        return redirect('/pdf')
    else:
        return redirect(request.url)
