from .db import db
from models import User



class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(500))
    user_id = db.Column(db.Integer, nullable=False db.foreign_key('users.id'))
    description = db.Column(db.String(2000))

    user_relationship = db.relationship("User")
