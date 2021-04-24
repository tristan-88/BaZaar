from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  first_name = db.Column(db.String(30))
  last_name = db.Column(db.String(30))
  email = db.Column(db.String(255), nullable = False, unique = True)
  username = db.Column(db.String(40), nullable = False, unique = True)
  address = db.Column(db.String(500))
  hashed_password = db.Column(db.String(255), nullable = False)


  @property
  def password(self):
    return self.hashed_password


  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)


  def check_password(self, password):
    return check_password_hash(self.password, password)


  def to_dict(self):
    return {
      "id": self.id,
      "first_name": self.firstName,
      "last_name": self.lastName,
      "username": self.username,
      "email": self.email
      "address": self.address
    }

  store_relationship = db.relationship("Store")