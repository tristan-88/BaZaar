from .db import db
from .tables import product_tag


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(30), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "tag": self.tag,
        }

    tag_product = db.relationship(
        "Product", secondary=product_tag, back_populates='product_tag', cascade="all, delete")

    tag_productTag = db.relationship("Product_Tag", back_populates="productTag_tag")
