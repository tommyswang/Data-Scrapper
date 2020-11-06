import uuid
import hashlib
from __init__ import db
import pathlib
import os

FILE_DIR = "files"


class ScrapeFile(db.Model):

  id = db.Column(db.String(64), primary_key=True)
  name = db.Column(db.String(64), unique=True)
  path = db.Column(db.Text)

  def __init__(self, file):
    self.id = uuid.uuid1().hex.upper()[:8]
    self.name = hashlib.md5(str(self.id).encode('utf-8')).hexdigest()

    # Save file to local data storage. Save file path to database
    op = getattr(file, "save", None)
    if callable(op):  # it is a request uploaded file
      _, f_ext = os.path.splitext(file.filename)

      new_file_name = "%s%s" % (self.name, f_ext)
      self.path = self.save_uploaded_file(file, new_file_name)
    else:  # it is a python built-in file
      self.path = self.save_opened_file(file)

  def save_uploaded_file(self, file, new_file_name):
    """Save file uploaded from web request.

    Args:
      file: the file object.
      new_file_name: the file name used to store the file in storage.

    Returns:
      The relative path of the file stored in storage.
    """

    root_path = pathlib.Path(__file__).resolve().parents[1]

    filepath = os.path.join(root_path, FILE_DIR, new_file_name)

    data = file.read()

    with open(filepath, 'wb') as f:
        f.write(bytes(data))

    relative_filepath = os.path.join("/", FILE_DIR, new_file_name)

    return relative_filepath

  def save_opened_file(self, file):
    """Save Python file object.

    Args:
      file: the file object.

    Returns:
      The relative path of the file stored in storage.
    """
    root_path = pathlib.Path(__file__).resolve().parents[1]
    filename = os.path.basename(file.name)
    filepath = os.path.join(root_path, FILE_DIR, filename)

    data = file.read()

    f = open(filepath, "wb")
    f.write(bytes(data))
    f.close()

    relative_filepath = os.path.join("/", FILE_DIR, filename)
    return relative_filepath

  def getUrl(self) -> str:
    return '/' + self.name
