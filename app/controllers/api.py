from models.scrape_job import ScrapeJob
from models.job_attr import JobType
from flask import Blueprint, render_template, request, send_file, safe_join
controller = Blueprint('api', __name__ )


@controller.route('/api', methods=['GET'])
def api():
    return render_template("api.html")

@controller.route('/api', methods=['POST'])
def create_api_job():
    json_format = request.form['json_format']
    url = request.form['url']
    job = ScrapeJob(JobType.API, url, json_format)
    if job:
        job.run()
        return render_template("api.html", error="Running Job")
    else:
        return render_template("api.html", error="Something Went Wrong")


