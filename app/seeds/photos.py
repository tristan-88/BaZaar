from faker import Faker
from app.models import (db, Photo)
import random

faker = Faker()


def seed_photos():
    for i in range(20):
        demo = Photo(
            product_id=faker.pyint(min_value=1, max_value=51),
            photo_url='''https://i.natgeofe.com/n/9135ca87-0115-4a22-8caf-d1bdef97a814/75552.jpg?w=636&h=424 '''
        )
        db.session.add(demo)
    db.session.commit()


def undo_photos():
    db.session.execute('''TRUNCATE photos RESTART IDENTITY CASCADE;''')
    db.session.commit()
