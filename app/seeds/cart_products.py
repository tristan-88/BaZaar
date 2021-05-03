from faker import Faker
from app.models import (db, Cart_Product)
import random


faker = Faker()



def seed_Cart_Products():
    for i in range(70):
        demo = Cart_Product(product_id=faker.pyint(min_value=1, max_value=25), cart_id=faker.pyint(min_value=1, max_value=6))
        db.session.add(demo)
    db.session.commit()


def undo_Cart_Products():
    db.session.execute('''TRUNCATE cart_products RESTART IDENTITY CASCADE;''')
    db.session.commit()


