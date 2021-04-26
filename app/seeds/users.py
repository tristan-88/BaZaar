# from werkzeug.security import generate_password_hash
from app.models import (db, User)

# Adds a demo user, you can add other users here if you want


def seed_users():
    demo = User(
        first_name='Demo',
        last_name='demo',
        email='demo@aa.io',
        username='Demo',
        address='3343 Breanne Green Apt. 660',
        password='password'
    )

    db.session.add(demo)

    user1 = User(
        first_name="Gus",
        last_name="Koepp",
        email="Hudson78@yahoo.com",
        username="Noemy34",
        address="3343 Breanne Green Apt. 660",
        password="zfeMR_6S2TXLf5m",
    )

    db.session.add(user1)

    user2 = User(
        first_name="Lillie",
        last_name="Kertzmann",
        email="Lavern_Barrows33@yahoo.com",
        username="Adrien_Runolfsson69",
        address="430 Goldner Viaduct Apt. 743",
        password="tKDL5DQ0oJ6AGUc",
    )

    db.session.add(user2)

    user3 = User(
        first_name="Dariana",
        last_name="Zboncak",
        email="Abbigail51@yahoo.com",
        username="Michele1",
        address="83452 Davon Cape Suite 132",
        password="TFSUKGohududev6",
    )

    db.session.add(user3)

    user4 = User(
        first_name="Erna",
        last_name="Boehm",
        email="Bernard77@gmail.com",
        username="Camren3",
        address="6559 Crystel Squares Apt. 904",
        password="YEcHlclhFWZSLMx",
    )

    db.session.add(user4)

    user5 = User(
        first_name="Aniya",
        last_name="Emmerich",
        email="Johnpaul_Okuneva@gmail.com",
        username="Emmy.Spencer",
        address="68267 Waino Glens Apt. 148",
        password="7_yzUQQLCYp_o5t",
    )

    db.session.add(user5)

    db.session.commit()


def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
