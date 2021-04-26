from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Date


# Tables

favorites = db.Table(
    "favorites",
    db.Column("user_id", db.Integer, db.ForeignKey(
        "users.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey(
        "products.id"), primary_key=True),
)


product_tag = db.Table(
    "product_tag",
    db.Column("product_id", db.Integer, db.ForeignKey(
        'products.id'), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True)
)


product_photo = db.Table(
    "product_photo",
    db.Column("product_id", db.Integer, db.ForeignKey(
        'products.id'), primary_key=True),
    db.Column("photo_id", db.Integer, db.ForeignKey(
        "photos.id"), primary_key=True)
)


cart_product = db.Table(
    "cart_product",
    db.Column("product_id", db.Integer, db.ForeignKey(
        'products.id'), primary_key=True),
    db.Column("cart_id", db.Integer, db.ForeignKey(
        "carts.id"), primary_key=True)
)




# Classes
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    address = db.Column(db.String(500))
    photo_url = db.Column(db.String(500))
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
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "email": self.email,
            "address": self.address
        }

    user_store = db.relationship(
        "Store", back_populates="store_user", uselist=False)
    user_cart = db.relationship("Cart", back_populates="cart_user")
    user_review = db.relationship("Review", back_populates="review_user")
    user_product = db.relationship(
        "Product", back_populates="product_user", secondary=favorites)
    user_order = db.relationship("Order", back_populates="order_user")


class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(Date)
    updated_at = db.Column(Date)
    order_id = db.Column(db.Integer, nullable=True)

    cart_user = db.relationship("User", back_populates="user_cart")
    cart_order = db.relationship("Order", back_populates="order_cart")


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey("carts.id"), nullable=False)
    purchase_date = db.Column(Date)

    order_user = db.relationship("User", back_populates="user_order")
    order_cart = db.relationship("Cart", back_populates="cart_order")


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    price = db.Column(db.Numeric(6, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(2000), nullable=False)

    product_store = db.relationship(
        "Store", back_populates="store_product")
    product_review = db.relationship("Review", back_populates="review_product")
    product_user = db.relationship(
        "User", secondary=favorites, back_populates="user_product")
    product_tag = db.relationship("Tag", secondary=product_tag, back_populates="tag_product")
    product_photo = db.relationship("Photo", back_populates="photo_product", secondary=product_photo)


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        "products.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    created_at = db.Column(Date)

    review_user = db.relationship("User", back_populates="user_review")
    review_product = db.relationship(
        "Product", back_populates="product_review")


class Store(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(2000))

    store_user = db.relationship("User", back_populates='user_store')
    store_product = db.relationship("Product", back_populates="product_store")

class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(30), nullable=False)

    tag_product = db.relationship(
        "Product", secondary=product_tag, back_populates='product_tag')


class Photo(db.Model):
    __tablename__ = "photos"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    photo_url = db.Column(db.String(2000))

    photo_product = db.relationship(
        "Product", back_populates="product_photo",secondary=product_photo)
