from faker import Faker
from app.models.tables import (db, cart_product)
import random

faker = Faker()


def seed_cart_products():
    for i in range(5):
        db.session.execute(f'''INSERT INTO cart_product (product_id, cart_id)
                VALUES({faker.pyint(min_value=1, max_value=51)},
                {faker.pyint(min_value=1, max_value=6)})''')
        db.session.commit()
        
        
def undo_cart_products():
    db.session.execute('''TRUNCATE cart_product RESTART IDENTITY CASCADE;''')
    db.session.commit()