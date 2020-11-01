from flask_sqlalchemy import SQLAlchemy
from db import db


class ScrapeJob(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  status = db.Column(db.String(50), unique=False)
  jobType = db.Column(db.String(20), unique=False)
  jobInput = db.Column(db.String(300), unique=False)
  fileId = db.Column(db.String(64), unique=False)

  def __init__(self, id, status, jobType, jobInput, fileId):
    self.id = id
    self.status = status
    self.jobType = jobType
    self.jobInput = jobInput
    self.fileId = fileId
