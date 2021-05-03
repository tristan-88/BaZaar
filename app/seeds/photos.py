from faker import Faker
from app.models import (db, Photo)
import random
import requests
import json

faker = Faker()
listIds = [955918114, 955918114, 1012391523, 262204716, 1005628051, 695989003, 874339742, 923822372, 822887407, 1012391485, 715490970, 956804061, 772935506, 960377148, 642980458, 998906599, 733208463, 738285499, 722971797, 884325377, 833736287, 216841121, 975844700, 800691632, 496683918, 998421838, 981528818, 987228511, 991344178, 838967239, 675500448, 895807575, 788525634, 735737734, 860523564, 918884450, 454327110, 668498206, 543984202, 998421808, 819582719, 999916137, 998421790, 762585532, 998421784, 978178716, 958498905, 580342231, 984373693, 998421774, 852712537, 629365862, 780844050, 998421752, 774672168, 656812933, 883240599, 998421082, 959048065, 998421720, 998421722, 994196483, 643066384, 1012391343, 952237881, 595759302, 289615371, 998180476, 907097670, 1006132607, 947653158, 896938442, 863491558, 743617706, 1007395755, 957146798, 913173663, 942607489, 963692302, 1012385505, 1012391311, 972048671, 872457892, 466369956, 998421230, 774833170, 877147189, 832854181, 493834669, 627952176, 880360531, 851532560, 998421680, 998421670, 773348403, 748843897, 827676740, 970732026, 450369110, 839207371, 1012147149, 1012147149]

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
