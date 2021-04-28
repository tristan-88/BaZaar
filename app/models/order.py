from .db import db
from sqlalchemy import Date


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey("carts.id"), nullable=False)
    purchase_date = db.Column(Date)
    shipping_address = db.Column(db.String(500))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "cart_id": self.cart_id,
            "purchase_date": self.purchase_date,
            "shipping_address": self.shipping_address
        }

    users = db.relationship("User", back_populates="orders", cascade="all, delete")
    carts = db.relationship("Cart", back_populates="orders", cascade="all, delete")
