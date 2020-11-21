from flask import Blueprint, render_template, request, redirect, url_for
from db import db
from models.scrape_file import ScrapeFile
from models.scrape_job import ScrapeJob
from models.job_attr import JobType

controller = Blueprint('pdf', __name__)


@controller.route('/pdf', methods=['GET'])
def pdf():
    return render_template("pdf.html")


@controller.route('/pdf', methods=['POST'])
def create_pdf_job():
    file = request.files['file']

    if file.filename:
        sf = ScrapeFile(file)
        job = ScrapeJob(JobType.PDF, sf.id)

        db.session.add(sf)
        db.session.add(job)
        db.session.commit()

        # Kick off the Job Now
        job.run()

        return redirect(url_for('jobs.detail', job_id=job.id))
    else:
        return render_template("pdf.pdf", error="Parsing job was not created.")
