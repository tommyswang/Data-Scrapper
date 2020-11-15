from configs.common import *

ENV = "production"
SERVER_NAME = "apps.hdap.gatech.edu"
SCRIPT_NAME = "/data-scrapper-app"

# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    # user='root', password='abc123456', server='155.138.217.198', database='data_scrper')

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='root', server='127.0.0.1', database='data_scrapper', password='abc123456')
