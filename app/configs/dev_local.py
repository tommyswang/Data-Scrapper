from configs.common import *

ENV = "dev_local"
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}@{server}/{database}'.format(
    user='root', server='127.0.0.1', database='data_scrapper')
