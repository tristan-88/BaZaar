from app.models import (db, Cart)
import time
import datetime
from faker import Faker

faker = Faker()


def seed_carts():
    for i in range(6):
        demo = Cart(
            user_id=(i+1),
            created_at=faker.date_time_this_year(),
            updated_at=faker.date_time_this_year(),
        )
        db.session.add(demo)
    db.session.commit()
    


def undo_carts():
    db.session.execute('TRUNCATE carts RESTART IDENTITY CASCADE;')
    db.session.commit()

