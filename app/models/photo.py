from .db import db


class Photo(db.Model):
    __tablename__ = "photos"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    photo_url = db.Column(db.String(2000))

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "photo_url": self.photo_url,
        }

    photo_product = db.relationship(
        "Product", back_populates="product_photo", cascade="all, delete")
