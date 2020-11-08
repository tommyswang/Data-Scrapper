from flask import Blueprint, render_template, request
from models.job_attr import JobType
from models.scrape_job import ScrapeJob

controller = Blueprint('html', __name__)

@controller.route('/html', methods=['GET'])
def html():
    return render_template("html.html")

@controller.route('/html', methods=['POST'])
def create_html_job():
    url = request.form['url']
    job = ScrapeJob(JobType.HTML, url)
    if job:
        job.run()
        return render_template("html.html", info="Running Job")
    else:
        return render_template("html.html", error="Error: No Job Found.")