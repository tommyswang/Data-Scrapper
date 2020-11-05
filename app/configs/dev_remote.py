from configs.common import *

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='root', password='abc123456', server='155.138.217.198', database='data_scrper')
