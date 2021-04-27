
from app.models import (db, Tag)


def seed_tags():
    tags = ['sports', 'gardening', 'jewelry', 'clothing', 'kitchen', 'collectibles', 'craft', 'decor','art', 'miscellaneous', 'home and living']
    for tag in tags:
        demo = Tag(
            tag=tag
        )
        db.session.add(demo)
    db.session.commit()



def undo_tags():
    db.session.execute('TRUNCATE stores RESTART IDENTITY CASCADE;')
    db.session.commit()