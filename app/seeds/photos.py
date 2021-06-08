from faker import Faker
from app.models import (db, Photo)
import random
import requests
import json
from ..config import Config
import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('API_SECRET_KEY')

faker = Faker()
listIds = [1004734105, 964209300, 1017123500, 1029217663, 399449043, 1017119836, 982354046, 990275729, 1003161964, 950738856, 699507810, 1017114010, 996523682, 865441058, 842392316, 600798901, 1017120606, 817989527, 624097569, 792672752, 612517471, 865501555, 687517882, 657641728, 767383244, 1031087607, 992154223, 971843911, 784478257, 864248887, 955257579, 978948431, 528185312, 1031087565, 577401572, 868571364, 1017124492, 1017124496, 802682151, 1027668823, 477943156, 1031087441, 827847384, 842201996, 1022803341, 862876692, 938685194, 1031087415, 854331936, 764838840, 930170959, 1031087421, 764994905, 947047259, 990381503, 495950938, 756707212, 86519271, 962610282, 1029481867, 892440795, 969926767, 859496778, 677157521, 892410555, 1017124406, 944438353, 788903523, 678137137, 1002292312, 1031059913, 673257789, 632496432, 892441189, 683151588, 745775843, 1017124378, 931435541, 1012001605, 951583057, 1012258532, 502971119, 260679544, 864002064, 660344647, 1031087287, 530503439, 742771998, 942972440, 1031087269, 950655829, 1004680183, 1005060354, 762845500, 1017124268, 479480308, 980208806, 1004734105, 489550395, 999001745, 1011736208, 1004734105]

def seed_photos():
    i = 1
    while i < len(listIds) - 1:
        response = requests.get(
            f'https://openapi.etsy.com/v2/listings/{listIds[i]}/images/?api_key=9i7i1vu4xhs80233snqp1t4y').json()

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
