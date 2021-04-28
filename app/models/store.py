from .db import db


class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    description = db.Column(db.String(2000))
    photo_url = db.Column(db.String(1000))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "user_id": self.user_id,
            "description": self.description,
            "photo_url": self.photo_url,
            "products": [product.to_dict() for product in self.products]
        }

    users = db.relationship(
        "User", back_populates="stores", cascade="all, delete")
    products = db.relationship(
        "Product", back_populates="stores", cascade="all, delete")
