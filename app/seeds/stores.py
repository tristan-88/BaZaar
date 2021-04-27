from app.models import (db, Store)


def seed_stores():

    store1 = Store(
        name="Rolfson, Gutkowski and Goyette",
        address="67610 Wiegand Locks Apt. 132",
        user_id=1,
        description="""Et omnis numquam. Quo incidunt error dolorum. Doloremque et eveniet repellendus soluta corrupti voluptas perspiciatis est. Qui qui magni voluptas sit similique. Illum facilis sapiente nobis dolor consequuntur minus consequatur.
        Est itaque ipsa sapiente optio autem quia eligendi voluptatem reiciendis. Aliquid repudiandae ut magni odit sit adipisci. Minus dignissimos sit nesciunt illo eum vel ea quia qui. Earum modi et perspiciatis est.""",
        photo_url="""https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fgetwallpapers.com%2Fwallpaper%2Ffull%2Ff%2Fd%2Fb%2F1129468-full-size-cute-cats-wallpaper-1080x1920-for-tablet.jpg&f=1&nofb=1"""
    )

    db.session.add(store1)

    store2 = Store(
        name="Stracke Group",
        address="29886 Rosamond Square Suite 910",
        user_id=2,
        description="""Totam consequuntur sint reprehenderit omnis possimus optio provident. Sit reprehenderit saepe sed consequuntur qui quia suscipit et eum. Cupiditate minima laborum. Minus et in architecto modi eligendi ut cupiditate.
        Nesciunt nobis aut vero alias a natus perferendis dicta. Atque quo minima tempora sed earum est quia. Sit quia soluta impedit. Ex beatae tenetur. Dolorum quia commodi qui minus ab sapiente.""",
        photo_url="""https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fgetwallpapers.com%2Fwallpaper%2Ffull%2Ff%2Fd%2Fb%2F1129468-full-size-cute-cats-wallpaper-1080x1920-for-tablet.jpg&f=1&nofb=1"""
    )

    db.session.add(store2)

    store3 = Store(
        name="Mitchell Inc",
        address="88232 Ernser Points Apt. 525",
        user_id=3,
        description="""Modi quibusdam sint voluptas sunt modi sunt. Iure consequuntur et repellendus culpa praesentium dolore. Eos illo sed ducimus esse tempora facere fugit dolore vel.
        Consequatur hic et et eos sequi suscipit dicta voluptas. Temporibus temporibus nam placeat similique nisi itaque possimus repudiandae. Minima saepe labore quia error.""",
        photo_url="""https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fgetwallpapers.com%2Fwallpaper%2Ffull%2Ff%2Fd%2Fb%2F1129468-full-size-cute-cats-wallpaper-1080x1920-for-tablet.jpg&f=1&nofb=1"""
    )

    db.session.add(store3)

    store4 = Store(
        name="Spinka - Lehner",
        address="4150 Destini Ports Suite 835",
        user_id=4,
        description="""Voluptas amet et unde quis rerum. Mollitia voluptatem reiciendis ratione. Est et earum incidunt qui. Qui earum dolore sed non qui.
        Officia est omnis error nulla. Atque at atque dolorum. Rerum voluptates voluptatem. Voluptatum ratione molestiae repudiandae error totam qui. Facilis qui in sed laboriosam ea.""",
        photo_url="""https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fgetwallpapers.com%2Fwallpaper%2Ffull%2Ff%2Fd%2Fb%2F1129468-full-size-cute-cats-wallpaper-1080x1920-for-tablet.jpg&f=1&nofb=1"""
    )

    db.session.add(store4)

    store5 = Store(
        name="Rice, Purdy and Williamson",
        address="9657 Jon Prairie Suite 040",
        user_id=5,
        description="""Consectetur aut alias quia delectus quibusdam facilis ipsa ut. Consequatur corrupti reprehenderit. Illum commodi et eaque neque alias. Ratione accusantium dolorem voluptatem earum libero. Rem quia eos architecto incidunt soluta rem ut. Laudantium quas non deleniti repudiandae deleniti similique eos.
        Neque qui iure. Ab nesciunt atque quidem. Eligendi atque ut accusantium aspernatur iusto facilis repellat. Omnis similique facilis vel facilis explicabo commodi et natus. Alias quia nesciunt dolorem et. Omnis vitae natus.""",
        photo_url="""https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fgetwallpapers.com%2Fwallpaper%2Ffull%2Ff%2Fd%2Fb%2F1129468-full-size-cute-cats-wallpaper-1080x1920-for-tablet.jpg&f=1&nofb=1"""
    )

    db.session.add(store5)

    store6 = Store(
        name="Beatty, Pollich and Ruecker",
        address="08190 Marjorie Oval Apt. 884",
        user_id=6,
        description="""Praesentium magni ut deserunt dolores consectetur voluptatem aut incidunt itaque. Tempore hic ut commodi. Sunt ea quo vero nisi qui iste commodi cum et.
        Aut sequi magni nobis iusto eos eveniet quia minus sunt. Voluptatem repudiandae et. Qui voluptates quae adipisci voluptatem recusandae qui. Aspernatur dolorem aliquid doloribus eius cupiditate illo aspernatur sed.""",
        photo_url="""https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fgetwallpapers.com%2Fwallpaper%2Ffull%2Ff%2Fd%2Fb%2F1129468-full-size-cute-cats-wallpaper-1080x1920-for-tablet.jpg&f=1&nofb=1"""
    )

    db.session.add(store6)

    db.session.commit()


def undo_stores():
    db.session.execute('TRUNCATE stores RESTART IDENTITY CASCADE;')
    db.session.commit()
