from .db import db
from sqlalchemy import Date, DateTime
import datetime


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        "products.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "user_id": self.user_id,
            "content": self.content,
            "created_at": self.created_at,
            "username": self.users.username,
        }

    users = db.relationship("User", back_populates="reviews")
    products = db.relationship(
        "Product", back_populates="reviews")
