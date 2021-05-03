from faker import Faker
from app.models import (db, Photo)
import random
import requests
import json

faker = Faker()
listIds = [996226923, 996226923, 664610975, 485880527, 950015148, 761507549, 910855096, 904649500, 644502191, 953215309, 783898401, 997034144, 453801194, 998707453, 784234889, 998245656, 834823334, 723834082, 920863024, 515837234, 998325800, 712976309, 996903462, 998325784, 837676799, 826651770, 826651770]

def seed_photos():
    i = 1
    while i < len(listIds) -1:
        response = requests.get(f'https://openapi.etsy.com/v2/listings/{listIds[i]}/images/?api_key=9i7i1vu4xhs80233snqp1t4y').json()
        photosObj = response['results']
        for photo in photosObj:
            demo = Photo(
                product_id=i,
                photo_url=photo["url_fullxfull"]
            )
            db.session.add(demo)
        i += 1
    db.session.commit()


def undo_photos():
    db.session.execute('''TRUNCATE photos RESTART IDENTITY CASCADE;''')
    db.session.commit()
