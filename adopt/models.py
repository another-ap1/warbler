from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_image="https://media.istockphoto.com/id/1075374570/vector/coming-soon.jpg?s=612x612&w=is&k=20&c=L_23y3TT68PJqePkWHJsseo8dm28dRb-kLtAlR7g9yw="

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, nullable=False, default=default_image)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

def connect_db(app):
    """connecting to database"""

    db.app = app
    db.init_app(app)