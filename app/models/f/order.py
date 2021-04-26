from .db import db
from sqlalchemy import Date


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey("carts.id"), nullable=False)
    purchase_date = db.Column(Date)

    order_user = db.relationship("User", back_populates="user_order")
    order_cart = db.relationship("Cart", back_populates="cart_order")
