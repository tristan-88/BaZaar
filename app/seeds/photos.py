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
listIds =  [999024014, 865380215, 882205672, 1012387958, 994319169, 1016118594, 921979602, 905904751, 1016118562, 1019028445, 1030085113, 1030086583, 917611834, 1027809049, 532762302, 1020901919, 1016118478, 800586142, 972215966, 841317780, 978429252, 823768140, 812613093, 512849750, 616782829, 1010385035, 778962990, 930556763, 1030086487, 500993098, 936166914, 799721631, 781398249, 967297711, 474183894, 771314367, 768603183, 609755851, 746700823, 943883991, 886561920, 816745991, 945456716, 1016118352, 189783660, 1015475156, 1016118334, 948312333, 565521806, 929152835, 880199264, 280381106, 254756586, 860575291, 220320259, 744139679, 743646618, 782740156, 1016118320, 943338874, 616924127, 990836776, 748402800, 996249666, 601720033, 933973992, 1016118290, 981704071, 788142778, 912685920, 712806974, 1016118276, 894787850, 845059412, 768675633, 1013719006, 916194845, 703385970, 552688620, 386910218, 1030083581, 907642220, 780616343, 770213607, 928475614, 1030086309, 945140735, 948713287, 1016118226, 667831984, 949886979, 953451477, 227270122, 960696361, 890929745, 754607035, 1016118210, 497596879, 1013851568, 681737098, 865380215, 865380215]

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
