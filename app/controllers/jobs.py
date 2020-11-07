from flask import Blueprint, render_template
from models.scrape_file import ScrapeFile
from models.scrape_job import ScrapeJob

controller = Blueprint('job', __name__)

@controller.route('/job/<job_id>', methods=['GET'])
def detail(job_id):
    job = ScrapeJob.query.filter_by(id=job_id)
    return render_template("jobs.html", job)

