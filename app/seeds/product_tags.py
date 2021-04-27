from faker import Faker
from app.models.tables import (db, product_tag)
import random

faker = Faker()


def seed_product_tags():
    for i in range(20):
        demo = product_tag(
            product_id=faker.pyint(min_value=1, max_value=51),
            tag_id=faker.pyint(min_value=1, max_value=11),
        )
        db.session.add(demo)
    db.session.commit()



def undo_product_tags():
    db.session.execute('TRUNCATE stores RESTART IDENTITY CASCADE;')
    db.session.commit()