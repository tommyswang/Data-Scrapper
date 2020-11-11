from models.scrape_job import ScrapeJob
from models.job_attr import JobType
from flask import Blueprint, render_template, request, send_file, safe_join
controller = Blueprint('api', __name__ )


@controller.route('/api', methods=['GET'])
def api():
    return render_template("api.html")


@controller.route('/api', methods=['POST'])
def create_api_job():
    print("Hello")
    json_format = request.form['json_format']
    URL = request.form['url']
    print(json_format)
    job = ScrapeJob(JobType.API, URL, json_format)
    print(job)
    if job:
        job.run()
        print("Running Job")
        return render_template("api.html", error="Running Job")
    else:
        return render_template("api.html", error="Something Went Wrong")


