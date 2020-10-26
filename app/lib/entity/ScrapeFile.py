import uuid, hashlib
from flask_sqlalchemy import SQLAlchemy
from __main__ import db

class ScrapeFile(db.Model):

  id = db.Column(db.String(64), primary_key=True)
  name = db.Column(db.String(64), unique=True)
  fileType = db.Column(db.String(10), unique=False)

  def __init__(self, fileType):
    self.id = str(uuid.uuid1())
    self.name = hashlib.md5(str(self.id).encode('utf-8')).hexdigest()

  def getUrl(self) -> str:
    return hashlib.md5(str(self.id).encode('utf-8')).hexdigest()
