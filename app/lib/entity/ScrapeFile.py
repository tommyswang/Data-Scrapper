import uuid, hashlib

class ScrapeFile:
  def __init__(self, fileType):
    self.id = str(uuid.uuid1())
    self.name = hashlib.md5(str(self.id).encode('utf-8')).hexdigest()
    self.fileType = fileType # 1 - User Upload PDF; 2 - System Genereated CSV

  def getUrl(self, id, fileType) -> str:
    suffix = 'pdf' if fileType == 1 else 'csv'
    # Not sure where the files are going to be stored yet System Variable/Configuration File....?
    return 'BASE_URL' + hashlib.md5(str(id).encode('utf-8')).hexdigest() + '.' + suffix
