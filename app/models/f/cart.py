from .db import db
from sqlalchemy import Date


class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False db.ForeignKey("users.id"))
    created_at = db.Column(Date)
    updated_at = db.Column(Date)
    order_id = db.Column(db.Integer, nullable=True)

    cart_user = db.relationship("User", back_populates="user_cart")
    cart_order = db.relationship("Order", back_populates="order_cart")
