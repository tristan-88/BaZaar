from .db import db
from .tables import Product_Tag


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(30), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "tag": self.tag,
        }

    tag_productTag = db.relationship("Product_Tag", back_populates="productTag_tag")
