from app.models import (db, Favorites)


def seed_Favorites():

    favorite0 = Favorites(
        product_id=22,
        user_id=1
    )

    db.session.add(favorite0)

    favorite1 = Favorites(
        product_id=7,
        user_id=1
    )

    db.session.add(favorite1)

    favorite2 = Favorites(
        product_id=42,
        user_id=3
    )

    db.session.add(favorite2)

    favorite3 = Favorites(
        product_id=7,
        user_id=5
    )

    db.session.add(favorite3)

    favorite4 = Favorites(
        product_id=46,
        user_id=5
    )

    db.session.add(favorite4)

    favorite5 = Favorites(
        product_id=33,
        user_id=4
    )

    db.session.add(favorite5)

    favorite6 = Favorites(
        product_id=36,
        user_id=5
    )

    db.session.add(favorite6)

    favorite7 = Favorites(
        product_id=22,
        user_id=3
    )

    db.session.add(favorite7)

    favorite8 = Favorites(
        product_id=18,
        user_id=5
    )

    db.session.add(favorite8)

    favorite9 = Favorites(
        product_id=11,
        user_id=3
    )

    db.session.add(favorite9)

    favorite10 = Favorites(
        product_id=24,
        user_id=1
    )

    db.session.add(favorite10)

    favorite11 = Favorites(
        product_id=24,
        user_id=5
    )

    db.session.add(favorite11)

    favorite12 = Favorites(
        product_id=10,
        user_id=1
    )

    db.session.add(favorite12)

    favorite13 = Favorites(
        product_id=14,
        user_id=4
    )

    db.session.add(favorite13)

    favorite14 = Favorites(
        product_id=40,
        user_id=4
    )

    db.session.add(favorite14)

    favorite15 = Favorites(
        product_id=25,
        user_id=4
    )

    db.session.add(favorite15)

    favorite16 = Favorites(
        product_id=40,
        user_id=5
    )

    db.session.add(favorite16)

    favorite17 = Favorites(
        product_id=48,
        user_id=1
    )

    db.session.add(favorite17)

    favorite18 = Favorites(
        product_id=41,
        user_id=1
    )

    db.session.add(favorite18)

    favorite19 = Favorites(
        product_id=13,
        user_id=5
    )

    db.session.add(favorite19)

    favorite20 = Favorites(
        product_id=33,
        user_id=3
    )

    db.session.add(favorite20)

    favorite21 = Favorites(
        product_id=28,
        user_id=1
    )

    db.session.add(favorite21)

    favorite22 = Favorites(
        product_id=44,
        user_id=2
    )

    db.session.add(favorite22)

    favorite23 = Favorites(
        product_id=10,
        user_id=5
    )

    db.session.add(favorite23)

    favorite24 = Favorites(
        product_id=6,
        user_id=4
    )

    db.session.add(favorite24)

    favorite25 = Favorites(
        product_id=15,
        user_id=1
    )

    db.session.add(favorite25)

    favorite26 = Favorites(
        product_id=27,
        user_id=1
    )

    db.session.add(favorite26)

    favorite27 = Favorites(
        product_id=15,
        user_id=5
    )

    db.session.add(favorite27)

    favorite28 = Favorites(
        product_id=7,
        user_id=5
    )

    db.session.add(favorite28)

    favorite29 = Favorites(
        product_id=14,
        user_id=1
    )

    db.session.add(favorite29)

    favorite30 = Favorites(
        product_id=5,
        user_id=2
    )

    db.session.add(favorite30)

    favorite31 = Favorites(
        product_id=11,
        user_id=4
    )

    db.session.add(favorite31)

    favorite32 = Favorites(
        product_id=39,
        user_id=5
    )

    db.session.add(favorite32)

    favorite33 = Favorites(
        product_id=35,
        user_id=5
    )

    db.session.add(favorite33)

    favorite34 = Favorites(
        product_id=31,
        user_id=5
    )

    db.session.add(favorite34)

    favorite35 = Favorites(
        product_id=11,
        user_id=5
    )

    db.session.add(favorite35)

    favorite36 = Favorites(
        product_id=4,
        user_id=5
    )

    db.session.add(favorite36)

    favorite37 = Favorites(
        product_id=11,
        user_id=1
    )

    db.session.add(favorite37)

    favorite38 = Favorites(
        product_id=39,
        user_id=1
    )

    db.session.add(favorite38)

    favorite39 = Favorites(
        product_id=18,
        user_id=1
    )

    db.session.add(favorite39)

    favorite40 = Favorites(
        product_id=43,
        user_id=3
    )

    db.session.add(favorite40)

    favorite41 = Favorites(
        product_id=37,
        user_id=2
    )

    db.session.add(favorite41)

    favorite42 = Favorites(
        product_id=19,
        user_id=3
    )

    db.session.add(favorite42)

    favorite43 = Favorites(
        product_id=3,
        user_id=4
    )

    db.session.add(favorite43)

    favorite44 = Favorites(
        product_id=5,
        user_id=3
    )

    db.session.add(favorite44)

    favorite45 = Favorites(
        product_id=42,
        user_id=3
    )

    db.session.add(favorite45)

    favorite46 = Favorites(
        product_id=18,
        user_id=4
    )

    db.session.add(favorite46)

    favorite47 = Favorites(
        product_id=47,
        user_id=4
    )

    db.session.add(favorite47)

    favorite48 = Favorites(
        product_id=31,
        user_id=5
    )

    db.session.add(favorite48)

    favorite49 = Favorites(
        product_id=35,
        user_id=4
    )

    db.session.add(favorite49)

    favorite50 = Favorites(
        product_id=48,
        user_id=3
    )

    db.session.add(favorite50)

    db.session.commit()


def undo_Favorites():
    db.session.execute('TRUNCATE favorites RESTART IDENTITY CASCADE;')
    db.session.commit()
