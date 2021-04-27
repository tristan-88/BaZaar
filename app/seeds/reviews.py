from faker import Faker
from app.models import (db, Review)
import datetime
import random
import time

faker = Faker()


def seed_reviews():
    # start_date = datetime.date(2020, 1, 1)
    # end_date = datetime.date(2021, 2, 1)

    # time_between_dates = end_date - start_date
    # days_between_dates = time_between_dates.days
    # random_number_of_days = random.randrange(days_between_dates)
    # random_date = start_date + datetime.timedelta(days=random_number_of_days)
    for i in range(50):
        demo = Review(
            product_id=faker.pyint(min_value=1, max_value=51),
            user_id=faker.pyint(min_value=1, max_value=6),
            content=faker.sentence(),
            created_at=faker.date_time_this_year()
        )
        db.session.add(demo)
    db.session.commit()



def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()