from flask import Blueprint, render_template
from models.scrape_file import ScrapeFile
from models.scrape_job import ScrapeJob

controller = Blueprint('job', __name__)

@controller.route('/job/<job_id>', methods=['GET'])
def detail(job_id):
    job = ScrapeJob.query.filter_by(id=job_id)
    if job.status == "failed":
        return render_template("jobs.html", download_link = "", message = "Something went wrong. Please try again.", button = "hidden")
    else:
        return render_template("jobs.html", download_link = job.file.path, message = "You data has finished extracting.", button = "btn btn-success")

