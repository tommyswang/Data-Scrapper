<<<<<<< HEAD
=======

>>>>>>> master
from configs.common import *
import os

ENV = "production"
SERVER_NAME = "apps.hdap.gatech.edu"
SCRIPT_NAME = "/data-scrapper-app"

'''
DB
DB Container:
    data-scrapper-db-service is our DB Service name and this is set in values.yaml
    GA Tech HDAP uses the following pattern 
    ${Host name}.${App scope is provided by this course}
    data-scrapper-db-service.ns-data-scrapper
    DB Service root user and its password are also set via ENV in values.yaml in a different container
APP Container:
    DB_USER, DB_PASS, DB_CONN are set in DOCKERFILE. 
    //TODO I want to move all Env settings in values.yaml 
'''

DB_USER = os.environ.get("DB_USER", "root")
DB_PASS = os.environ.get("DB_PASS", "abc123456")
DB_CONN = os.environ.get("DB_CONN", "data-scrapper-db-service.ns-data-scrapper")

<<<<<<< HEAD
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user=DB_USER, password=DB_PASS, server=DB_CONN, database='data_scrapper')
=======
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user=DB_USER, password=DB_PASS, server=DB_CONN, database='data_scrapper')
>>>>>>> master
