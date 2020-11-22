from models.scrape_job import ScrapeJob
from models.job_attr import JobType
from flask import Blueprint, render_template, request, redirect, url_for
controller = Blueprint('api', __name__ )


@controller.route('/api', methods=['GET'])
def api():
    return render_template("api.html")

@controller.route('/api', methods=['POST'])
def create_api_job():
    json_format = request.form['json_format']
    url = request.form['url']

    if json_format == None or json_format == "":
        json_format = "flat"

    extra = {
        "url": url,
        "json_format": json_format
    }

    job = ScrapeJob(JobType.API, url, extra)
    if job:
        job.run()
        return redirect(url_for('jobs.detail', job_id=job.id))
    else:
        return render_template("api.html", error="Parsing job was not created.")
