from flask import Blueprint, render_template

from models.scrape_file import ScrapeFile
from models.scrape_job import ScrapeJob

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
    job = ScrapeJob.query.filter_by(id=job_id)
    return render_template("jobs.html", job)
