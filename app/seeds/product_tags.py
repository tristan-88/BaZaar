from faker import Faker
from app.models.tables import (db, product_tag)
import random

faker = Faker()


def seed_product_tags():
    for i in range(20):
        db.session.execute(f'''INSERT INTO product_tag (product_id, tag_id)
                VALUES({faker.pyint(min_value=1, max_value=51)}, {faker.pyint(min_value=1, max_value=11)})           ''')
        db.session.commit()



def undo_product_tags():
    db.session.execute('''TRUNCATE product_tag RESTART IDENTITY CASCADE;''')
    db.session.commit()