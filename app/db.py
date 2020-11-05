from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()

class DSDB:
    def __init__(self, app):
        self.db = db
        self.app = app
        self.db.init_app(app)
        

    def initDB(self):
        try:
            engine = create_engine(self.app.config['SQLALCHEMY_DATABASE_URI'])  

            if not database_exists(engine.url):
                create_database(engine.url)
            
            # migrate database
            self.db.create_all()
            self.db.session.commit()
        
        except Exception as e:
            self.app.logger.error(f'Database Init Exception: {e}')
