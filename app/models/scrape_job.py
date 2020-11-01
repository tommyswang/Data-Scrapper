from flask_sqlalchemy import SQLAlchemy
from db import db
from job_attr import JobStatus


class ScrapeJob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), unique=False)
    jobType = db.Column(db.String(20), unique=False)
    jobInput = db.Column(db.String(300), unique=False)
    fileId = db.Column(db.String(64), unique=False)
    extra = db.Column(db.String)
	file = db.relationship("ScrapeFile")

	def __init__(self, id, jobType, jobInput, extra=None):
        self.id = id
        self.status = JobStatus.PENDING
        self.jobType = jobType
        self.jobInput = jobInput
        self.extra = extra
