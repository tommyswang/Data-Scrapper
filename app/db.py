from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()

class DSDB:
    def __init__(self, app):
        self.db = SQLAlchemy()
        self.app = app
        self.dbStr = app.config['SQLALCHEMY_DATABASE_URI']
        self.db.init_app(app)

    def initDB(self):
        try:
            engine = create_engine(self.dbStr)  

            if database_exists(engine.url):
                self.app.logger.info(f"Skip Creating Database/Schema: {self.dbStr}")
            else:
                self.app.logger.info(f"Creating Database/Schema: {self.dbStr}")
                create_database(engine.url)
            
            # migrate database
            self.db.create_all()
            self.db.session.commit()
        
        except Exception as e:
            self.app.logger.error(f'Database Init Exception: {e}')
