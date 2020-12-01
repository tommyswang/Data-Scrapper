from flask import Blueprint, render_template, request, redirect, url_for
from models.job_attr import JobType
from models.scrape_job import ScrapeJob

controller = Blueprint('html', __name__)

@controller.route('/html', methods=['GET'])
def html():
    return render_template("html.html")

@controller.route('/html', methods=['POST'])
def create_html_job():
    url = request.form['url']
    if url == '':
        return render_template("html.html", error="FAILED. ERROR INFO: No url found.")

    extra = {
        "url": url
    }

    job = ScrapeJob(JobType.HTML, url, extra)
    if job:
        job.run()
        return redirect(url_for('jobs.detail', job_id=job.id))
    else:
        return render_template("html.html", error="Parsing job was not created.")
