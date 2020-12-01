from lib.parsers.form_parser import FormParser
from flask import Blueprint, render_template, request, redirect, url_for, flash
from db import db
from models.scrape_file import ScrapeFile
from models.scrape_job import ScrapeJob
from models.job_attr import JobType
from lib.parsers.form_parser import FormParser

controller = Blueprint('form', __name__)


@controller.route('/form', methods=['GET'])
def form():
    form_names = FormParser.TEMPLATE_NAMES
    return render_template("form.html", form_names=form_names)


@controller.route('/form', methods=['POST'])
def create_form_job():
    file = request.files['file']
    form_name = request.form['form-type']

    if file.filename:
        if '.pdf' not in file.filename:
            return render_template("form.html", error="JOB FAILED. ERROR INFO: File type is not supported.")
        sf = ScrapeFile(file)

        extra = {
            'file name': file.filename,
            'form name': form_name
        }
        job = ScrapeJob(JobType.FORM, sf.id, extra)

        db.session.add(sf)
        db.session.add(job)
        db.session.commit()

        # Kick off the Job Now
        job.run()

        return redirect(url_for('jobs.detail', job_id=job.id))

    else:
        flash("Job Failed. ERROR INFO: NoFileFoundError. Upload the file and try again.", 'error')
        return redirect('form.form')
