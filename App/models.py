from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def saveToDB(self):
    db.session.add(self)
    db.session.commit()