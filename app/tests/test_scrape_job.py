import pytest
from lib.parsers.pdf_parser import PdfParser
from models.scrape_file import ScrapeFile
from models.scrape_job import ScrapeJob
from models.job_attr import *
import pathlib
import os
from main import create_app
from setup import db
from os import path
from models.job_attr import JobStatus, JobType


def setup_app_db():
    app = create_app()
    app.app_context().push()
    db.init_app(app)
    return app, db


def test_run_job():
    app, db = setup_app_db()

    job = None

    cnt_path = root_path = pathlib.Path(__file__).resolve().parents[0]
    file_path = os.path.join(cnt_path, "form.pdf")

    with open(file_path, "rb") as f:
        sf = ScrapeFile(f)
        job = ScrapeJob(JobType.PDF, sf.id)

        db.session.add(sf)
        db.session.add(job)
        db.session.commit()

        job.run()

    assert job.status == JobStatus.FINISHED


def test_creation():
    app, db = setup_app_db()
    job = None

    cnt_path = root_path = pathlib.Path(__file__).resolve().parents[0]
    file_path = os.path.join(cnt_path, "form.pdf")

    with open(file_path, "rb") as f:
        sf = ScrapeFile(f)
        job = ScrapeJob(JobType.PDF, sf.id)

        db.session.add(sf)
        db.session.add(job)
        db.session.commit()

    assert job.name != "" and job.name != None
    assert job.created != "" and job.created != None
