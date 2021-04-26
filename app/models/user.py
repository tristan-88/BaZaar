from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    address = db.Column(db.String(500))
    hashed_password = db.Column(db.String(255), nullable=False)

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

    user_store = db.relationship(
        "Store", back_populates="store_user", uselist=False)
    user_cart = db.relationship("Cart", back_populates="cart_user")
    user_review = db.relationship("Review", back_populates="review_user")
    user_product = db.relationship(
        "Product", secondary=favorites, back_populates="product_user")
    user_order = db.relationship("Order", back_populates="order_user")
