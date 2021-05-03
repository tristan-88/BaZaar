from faker import Faker
from app.models import (db, Product_Tag)
import random


faker = Faker()


def seed_Product_Tags():
    for i in range(100):
        demo = Product_Tag(
            product_id=faker.pyint(min_value=1, max_value=25),
            tag_id=faker.pyint(min_value=1, max_value=11)
        )
        db.session.add(demo)
    db.session.commit()


def undo_Product_Tags():
    db.session.execute('''TRUNCATE product_tags RESTART IDENTITY CASCADE;''')
    db.session.commit()
