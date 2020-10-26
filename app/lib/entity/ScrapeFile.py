import uuid, hashlib
from flask_sqlalchemy import SQLAlchemy
from __main__ import db

class ScrapeFile(db.Model):

  id = db.Column(db.String(64), primary_key=True)
  name = db.Column(db.String(64), unique=True)

  def __init__(self):
    self.id = str(uuid.uuid1())
    self.name = hashlib.md5(str(self.id).encode('utf-8')).hexdigest()

  def getUrl(self) -> str:
    return '/'+ self.name
