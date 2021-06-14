from faker import Faker
from app.models import (db, Cart_Product)
import random


faker = Faker()



def seed_Cart_Products():
    for i in range(50):
        demo = Cart_Product(product_id= i+1, cart_id=faker.pyint(min_value=1, max_value=6), quantity=faker.pyint(min_value=1, max_value=3))
        db.session.add(demo)
    db.session.commit()


def undo_Cart_Products():
    db.session.execute('''TRUNCATE cart_products RESTART IDENTITY CASCADE;''')
    db.session.commit()


