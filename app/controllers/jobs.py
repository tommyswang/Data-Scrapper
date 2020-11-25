from flask import Blueprint, render_template, current_app, request, redirect, url_for, flash

from models.scrape_job import ScrapeJob
from models.job_attr import JobStatus
import hashlib

controller = Blueprint('jobs', __name__)


def short_hash(value, digits):
    value = str(value)

    return hashlib.md5(value.encode('utf-8')).hexdigest()[:digits]


@controller.route('/jobs', methods=['GET'])
def index():
    jobs = ScrapeJob.query.order_by(ScrapeJob.sys_created_on.desc()).all()
    return render_template(
        "jobs/index.html", 
        jobs=jobs, 
        hash=short_hash, 
        JobStatus=JobStatus)


@controller.route('/job/<job_id>', methods=['GET'])
def detail(job_id):
    referrer = request.referrer
    job = ScrapeJob.query.filter_by(id=job_id).first()
    if job != None:
        file_name = None
        if job.file:
            file_name = job.file.path.split("/")[-1]
        return render_template(
            "jobs/detail.html",
            job=job,
            JobStatus=JobStatus,
            file_name=file_name)
    else:
        path = referrer if referrer else url_for('jobs.index')
        flash('Job does not exist', 'error')
        return redirect(path)