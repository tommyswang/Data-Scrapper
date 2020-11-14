from flask import Blueprint, render_template, current_app, request, redirect

from models.scrape_job import ScrapeJob
from models.job_attr import JobStatus
import hashlib

controller = Blueprint('jobs', __name__)


def short_hash(value, digits):
    value = str(value)

    return hashlib.md5(value.encode('utf-8')).hexdigest()[:digits]


@controller.route('/jobs', methods=['GET'])
def index():
    jobs = ScrapeJob.query.all()
    return render_template("jobs/index.html", jobs=jobs, hash=short_hash)


@controller.route('/job/<job_id>', methods=['GET'])
def detail(job_id):
    referrer = request.referrer
    job = ScrapeJob.query.filter_by(id=job_id).first()
    if job != None:
        file_name = None
        if job.file:
            file_name = job.file.path.split("/")[-1]
        job_status_class = JobStatus
        return render_template("jobs/detail.html", job=job, job_status=job_status_class, file_name=file_name)
    else:
        msg = 'Job does not exist'
        path = referrer if referrer else '/jobs'
        return redirect(path, error=msg)