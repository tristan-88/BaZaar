from app.models import (db, Product)
import requests
import json

listIds = [996226923, 996226923, 664610975, 485880527, 950015148, 761507549, 910855096, 904649500, 644502191, 953215309, 783898401, 997034144, 453801194, 998707453, 784234889, 998245656, 834823334, 723834082, 920863024, 515837234, 998325800, 712976309, 996903462, 998325784, 837676799, 826651770, 826651770]


def seed_products():
    i = 1
    while i < len(listIds) -1:
        response = requests.get(f'https://openapi.etsy.com/v2/listings/{listIds[i]}/?api_key=9i7i1vu4xhs80233snqp1t4y')
        data = response.json()
        listings = data['results']
        for item in listings:
            demo = Product(
                name=item["title"],
                store_id=(i/20)+1,
                price=item["price"],
                quantity=item["quantity"],
                description=item["description"],
            )
            db.session.add(demo)
        i += 1
    db.session.commit()

def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
