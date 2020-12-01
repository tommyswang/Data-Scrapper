from flask import Blueprint, render_template, request, redirect, url_for
from db import db
from models.scrape_file import ScrapeFile
from models.scrape_job import ScrapeJob
from models.job_attr import JobType

controller = Blueprint('form', __name__)


@controller.route('/form', methods=['GET'])
def form():
    return render_template("form.html")


@controller.route('/form', methods=['POST'])
def create_form_job():
    file = request.files['file']

    if file.filename:
        if '.pdf' not in file.filename:
            return render_template("form.html", error="JOB FAILED. ERROR INFO: File type is not supported.")
        sf = ScrapeFile(file)

        extra = {
            'file name': file.filename
        }
        job = ScrapeJob(JobType.FORM, sf.id, extra)

        db.session.add(sf)
        db.session.add(job)
        db.session.commit()

        # Kick off the Job Now
        job.run()

        return redirect(url_for('jobs.detail', job_id=job.id))

    else:
        return render_template("form.html", error="Job Failed. ERROR INFO: NoFileFoundError. Upload the file and try again.")
