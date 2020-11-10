from configs.common import *
import os

ENV = "dev_local"

db_pwd = os.environ.get('MYSQL_ROOT_PWD', None)

if db_pwd:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
        user='root', server='127.0.0.1', database='data_scrapper', password=db_pwd)
else:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}@{server}/{database}'.format(
        user='root', server='127.0.0.1', database='data_scrapper')
