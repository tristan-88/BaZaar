from .db import db
from sqlalchemy import Date


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        "products.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    created_at = db.Column(Date)

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "user_id": self.user_id,
            "content": self.content,
            "created_at": self.created_at,
        }

    review_user = db.relationship("User", back_populates="user_review", cascade="all, delete")
    review_product = db.relationship(
        "Product", back_populates="product_review", cascade="all, delete")
