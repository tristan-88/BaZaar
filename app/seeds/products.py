from app.models import (db, Product)


def seed_products():

    product0 = Product(
        name="Incredible Wooden Pizza",
        store_id=2,
        price=86.00,
        quantity=12,
        description="""Nobis doloremque sit assumenda nisi dolorum. Perspiciatis facere eveniet qui quos minus. Illum qui error quo corporis blanditiis ratione ut omnis.
        Veritatis delectus repellendus ab recusandae sed quia qui dolor ullam. In itaque vero reiciendis. Quis voluptas quidem molestiae. Est non aut aut laboriosam aut. Architecto doloremque qui. Ipsum molestiae nam magnam et quis mollitia occaecati officia.
        Suscipit repellendus distinctio quasi. Sint et et id nam. Quod voluptatem aliquid aspernatur similique voluptas cum et. Sit ea illum sed non occaecati eos ratione delectus nulla. Dicta aut quis. Sit maiores aperiam ipsam.""",
    )

    db.session.add(product0)

    product1 = Product(
        name="Licensed Soft Towels",
        store_id=4,
        price=200.00,
        quantity=4,
        description="""Nulla consequatur voluptas hic iure dolorum amet. Neque culpa deleniti fugit est recusandae qui cumque voluptate. Quisquam nisi qui aut sunt. Quam totam cumque qui. Nulla saepe ipsum. Impedit est ut.
        Alias dolore blanditiis nostrum deleniti quia voluptatibus ad autem. Nostrum temporibus voluptatem id numquam dolor id adipisci. Qui voluptatibus dolor non omnis eos.
        Architecto porro dolores hic. Voluptate sit non qui id placeat eveniet voluptas. Id est perferendis ipsa laboriosam molestiae velit. Dolore pariatur quia vero quaerat. Repellat inventore a labore saepe eveniet corrupti ex et.""",
    )

    db.session.add(product1)

    product2 = Product(
        name="Generic Metal Car",
        store_id=5,
        price=132.00,
        quantity=4,
        description="""Sunt eum et animi doloremque odit voluptatem autem. Dolorem necessitatibus doloribus. Suscipit repellendus illo ut ut sint. Soluta iste eaque enim perspiciatis dolorem libero perspiciatis quia dolorem. Rem excepturi facere quis itaque maxime. Et et quasi ex odit quia reiciendis et.
Dolorum molestiae nostrum voluptates nobis ipsam vel voluptas. Voluptas itaque omnis ipsa aut fugit ullam. Fugiat sequi magnam numquam illum. Eveniet id eos.
Consequatur dolorum nihil autem quos provident libero et recusandae. Exercitationem voluptate perferendis ut harum sunt. Eum omnis odio tempore suscipit non.""",
    )

    db.session.add(product2)

    product3 = Product(
        name="Handcrafted Cotton Pizza",
        store_id=4,
        price=55.00,
        quantity=3,
        description="""Consequuntur at eligendi consectetur alias aut. Molestiae cupiditate incidunt quia perspiciatis et qui praesentium. Qui illum ad inventore. Libero quos aspernatur ipsa vitae incidunt voluptatem.
Ad non beatae ad hic. Est cupiditate suscipit facere id fugiat. Id consequuntur temporibus. Laboriosam nesciunt repellendus reprehenderit mollitia. Iusto cupiditate quae.
Harum fugiat tempora nam harum optio. Voluptatem quod totam voluptatem qui. Iusto laudantium eum assumenda non. Corporis voluptatem deleniti nisi tenetur voluptate et. Et aspernatur tempora corrupti at architecto itaque fuga aperiam.""",
    )

    db.session.add(product3)

    product4 = Product(
        name="Licensed Plastic Shirt",
        store_id=2,
        price=49.00,
        quantity=15,
        description="""Laudantium est non quia repellendus id neque enim officia atque. Voluptatem nihil exercitationem. Voluptas quo labore consequatur beatae. Nisi vitae aliquam.
Cum eveniet omnis esse saepe in doloribus adipisci sequi. Rerum corporis totam ipsam ut placeat vel qui nesciunt est. Minima repudiandae quis deserunt exercitationem ad quam repudiandae voluptatibus. Quo non asperiores id. Amet deserunt dolorem sed quae.
Tenetur laudantium debitis quia recusandae voluptatibus nesciunt. Veniam incidunt et iure adipisci quam vero quia impedit assumenda. Voluptatem ut sint possimus. Et est harum est.""",
    )

    db.session.add(product4)

    product5 = Product(
        name="Handcrafted Granite Chair",
        store_id=1,
        price=234.00,
        quantity=4,
        description="""Sunt sit nemo qui corporis rerum at et quos blanditiis. Quos ut sit ipsum minima voluptates tempora. Iure aut eos excepturi voluptatem. Tempore ullam a. Dolores rem ea ducimus et nostrum laboriosam quasi aliquam autem. Ea et blanditiis.
Exercitationem consequuntur esse. Temporibus et nobis praesentium. Possimus eveniet commodi sapiente delectus sit nesciunt error. Ullam in nihil occaecati nisi nisi.
Dolores ut et blanditiis delectus nisi. Ut quis natus soluta et. Facere architecto corporis maxime aut molestiae. Quae aut accusantium dolorem.""",
    )

    db.session.add(product5)

    product6 = Product(
        name="Refined Cotton Sausages",
        store_id=5,
        price=26.00,
        quantity=12,
        description="""Earum labore eum. Officiis quod consequatur incidunt. Tempore consequatur impedit voluptatibus sed aut suscipit aperiam cupiditate.
Laborum dolorem officiis nemo autem omnis fugit minima eum repellat. Asperiores distinctio cum ut dolorem assumenda occaecati. Et nesciunt rerum. Odio maiores magnam. Ipsa in nemo voluptas totam at rerum. Praesentium hic error qui eum sequi consequatur non omnis praesentium.
Est soluta qui necessitatibus eveniet. Dolor et recusandae aspernatur reiciendis deserunt totam doloribus et. Culpa consequatur ratione omnis.""",
    )

    db.session.add(product6)

    product7 = Product(
        name="Practical Fresh Chicken",
        store_id=1,
        price=150.00,
        quantity=6,
        description="""Dignissimos aut commodi eum quidem a. Voluptatum id quaerat sed velit natus voluptatem nesciunt possimus corrupti. Soluta nemo deleniti molestiae dolorem sed sit quaerat voluptatem. Non vero error vitae minima vel earum doloremque exercitationem harum.
Et voluptate ducimus est deleniti. Accusamus sint assumenda deserunt nihil doloribus quasi. Consequatur esse id et voluptatem. Quisquam modi non. Voluptatibus ad vel. Deserunt repellat esse occaecati.
Impedit harum voluptas est sunt. Dolor illo quia. Inventore sit cum rem dignissimos ratione possimus et et. Aliquid et excepturi fugit aliquid dignissimos voluptatem iste expedita quaerat.""",
    )

    db.session.add(product7)

    product8 = Product(
        name="Gorgeous Cotton Bike",
        store_id=5,
        price=42.00,
        quantity=9,
        description="""Assumenda minima accusamus dolores quia voluptas repellat laborum voluptatum officia. Illo qui ut omnis ipsam porro voluptatum voluptatem qui. Quidem qui voluptas pariatur est. Et omnis suscipit quis odit aspernatur totam.
At quas sit beatae aspernatur dolore quasi omnis omnis. Dolorem ut aliquam nesciunt dolore deserunt labore quod ut est. Molestiae sunt necessitatibus sint vero et eum dicta. Et quos ipsam.
Id officia voluptatum ea illum nobis illo. Minus expedita cupiditate nobis aut sint omnis. Deserunt consequatur aliquam quisquam qui aut.""",
    )

    db.session.add(product8)

    product9 = Product(
        name="Intelligent Cotton Table",
        store_id=1,
        price=36.00,
        quantity=14,
        description="""Nisi harum impedit optio ut ut qui. Sed hic illum quisquam reprehenderit. Aut dolores aut.
Eos et quo nemo molestiae ut. Iste ea nisi sequi dolorem culpa similique ducimus rerum. Perferendis commodi corporis delectus earum unde. In libero nobis sit voluptatum. Earum doloremque magni. Voluptas hic aperiam itaque sequi illo vitae enim exercitationem.
Non quis at et ut nihil distinctio harum. Velit iusto soluta est et est harum excepturi. Ut cupiditate voluptas aut.""",
    )

    db.session.add(product9)

    product10 = Product(
        name="Handcrafted Wooden Car",
        store_id=2,
        price=25.00,
        quantity=10,
        description="""Minus consequuntur architecto voluptate molestiae natus est cupiditate. Deleniti ea quisquam doloremque. Laborum eaque illo est perspiciatis. Repudiandae et illum voluptate qui. Doloribus enim mollitia illo.
Rem ea et nihil qui quia exercitationem est repellendus. Qui non autem dolore. In non distinctio veritatis magnam minima qui consequatur in molestias.
Cupiditate reiciendis dolore cum quae animi eum et. Iste quidem et eaque aspernatur. Possimus tenetur qui voluptas. Deleniti beatae excepturi quaerat aut odit distinctio voluptas nemo consequatur.""",
    )

    db.session.add(product10)

    product11 = Product(
        name="Gorgeous Cotton Chair",
        store_id=1,
        price=116.00,
        quantity=4,
        description="""Illo fugit quia id vel sit amet iure optio culpa. Exercitationem voluptatem totam laborum odit expedita alias quia iusto doloremque. Earum iure veniam deserunt eveniet quibusdam voluptas quo deserunt. Quod iusto est atque possimus excepturi sequi non.
Cupiditate modi dicta blanditiis qui quaerat. Sed eaque sequi reprehenderit dolorum pariatur in illo. Sit reiciendis eum aliquam sit earum odit placeat.
Quae quis distinctio harum aspernatur qui tempora dolores. Aut similique inventore dolores doloremque ad aut omnis expedita. Unde nesciunt praesentium maiores corporis et sequi ipsam eius quae. Perferendis expedita excepturi. Alias sunt debitis placeat molestias ipsam.""",
    )

    db.session.add(product11)

    product12 = Product(
        name="Licensed Concrete Gloves",
        store_id=5,
        price=115.00,
        quantity=1,
        description="""Voluptate id ipsam et ut exercitationem qui. Molestiae totam et debitis commodi temporibus saepe. Fuga autem dolorum.
Assumenda quia nesciunt beatae magnam necessitatibus. Quia vel fugiat. Eum et ratione aut aut cumque est.
Ut libero voluptatem. Pariatur porro autem adipisci dolorum sint enim facere aut. Et aspernatur facere laboriosam. Ut porro id.""",
    )

    db.session.add(product12)

    product13 = Product(
        name="Ergonomic Concrete Bike",
        store_id=2,
        price=216.00,
        quantity=7,
        description="""Molestias est enim. Beatae accusamus alias corporis fugiat. Voluptatem id ut sequi. Natus veniam voluptatem et temporibus qui rem et. Facilis et debitis qui facere odio.
Expedita quia magni. Corrupti animi enim beatae perferendis voluptas quasi velit voluptate. Vel aut sapiente non dignissimos hic at a. Deserunt maiores aliquid dolorum illo. Sint vitae ea reiciendis doloremque laudantium dolorem perferendis. Cum excepturi similique sunt quia natus enim cupiditate.
Reiciendis perferendis quia et. Tempora ea veritatis itaque. Sunt eius ea deserunt quibusdam excepturi sit. Culpa molestias aliquid occaecati.""",
    )

    db.session.add(product13)

    product14 = Product(
        name="Awesome Soft Soap",
        store_id=5,
        price=58.00,
        quantity=18,
        description="""Est dolores et doloremque perferendis pariatur error debitis. Ut quia ratione aut et sit modi sit. Veniam molestiae et incidunt illum et veniam accusantium sed tempore.
Accusantium cum vero optio asperiores sapiente praesentium voluptate. Illo aut officia esse maxime voluptatibus ducimus et. Veniam eum quia.
Autem rerum quisquam voluptatem. Repellat neque perferendis qui dicta. Facilis est similique aut voluptatibus saepe harum temporibus asperiores. Ut quos pariatur qui.""",
    )

    db.session.add(product14)

    product15 = Product(
        name="Ergonomic Soft Keyboard",
        store_id=3,
        price=92.00,
        quantity=10,
        description="""Quod quo magnam. Ut libero cupiditate eveniet vitae. Earum et ut fugiat sed nam numquam ut dolores. Harum nulla quas dignissimos omnis quam quia ex optio omnis.
Nostrum quis omnis. Tempora dolorem dolores qui sunt. Placeat dolorem animi molestiae quas necessitatibus illo tempore voluptatem voluptate.
Qui vel dolor. Dignissimos amet quia odio. Magnam corrupti rerum a minima nihil omnis. Rem nam enim aut qui. Odit doloribus et quia.""",
    )

    db.session.add(product15)

    product16 = Product(
        name="Unbranded Plastic Keyboard",
        store_id=1,
        price=227.00,
        quantity=3,
        description="""Qui vero occaecati omnis qui nihil et. Quo error consequatur et eaque eum doloribus deleniti iste. Ut dolor earum voluptatem aut. Corporis autem quos aut et eaque.
Et voluptas et dolorem. Quia rerum architecto omnis quo ea iste. Nesciunt enim dolorem. Iure et omnis necessitatibus doloremque unde recusandae et veritatis vel. Dolores qui sunt magnam cupiditate. Perspiciatis dolores est aut non repellat natus porro eos cum.
Vel aliquam sunt ut libero nemo officia. Dolores dolorem id. Molestiae nostrum architecto libero autem et cupiditate eveniet. Quam accusantium dolorem vero optio harum rem. Ullam assumenda molestias aliquid.""",
    )

    db.session.add(product16)

    product17 = Product(
        name="Awesome Concrete Table",
        store_id=5,
        price=204.00,
        quantity=16,
        description="""Debitis necessitatibus cupiditate. Velit deleniti fugit voluptatem. Quis numquam harum explicabo recusandae. Qui est fuga sequi saepe.
Dolores et nobis. Sed nihil consectetur sequi nam facilis. Corrupti quo unde. Tempore culpa reprehenderit qui quia vel. Nesciunt debitis at ipsam fuga. Eius dolore temporibus repellat ut.
Rerum molestias ut excepturi omnis adipisci earum assumenda laudantium. Quia reiciendis velit minima facilis sequi libero omnis officia soluta. Voluptas numquam sunt nulla atque earum nemo sapiente autem reprehenderit. Soluta at veritatis et rerum voluptas earum unde sapiente et.""",
    )

    db.session.add(product17)

    product18 = Product(
        name="Handcrafted Granite Computer",
        store_id=5,
        price=245.00,
        quantity=20,
        description="""Et aliquam aut fuga aperiam consequatur nesciunt aliquid. Doloribus ipsam in illo eaque sapiente vel sit aliquam asperiores. Deserunt vitae temporibus dolores et dolor distinctio eos. Ipsum sequi deserunt. Eum velit laudantium totam necessitatibus voluptatibus quod vitae quisquam.
Voluptas sint sed eum. Corporis enim repellat aut. Officia sed reiciendis. Temporibus pariatur recusandae nemo hic aut modi. Praesentium sed quia quisquam quia cupiditate quo.
Quas et velit in non eaque magnam eos et et. Perspiciatis qui id dolor facilis. Ducimus aut laudantium veritatis itaque.""",
    )

    db.session.add(product18)

    product19 = Product(
        name="Practical Concrete Cheese",
        store_id=2,
        price=172.00,
        quantity=12,
        description="""Maxime consequuntur quasi aut doloremque veniam autem. Odit voluptatibus consectetur quidem quasi id tempora voluptatem laborum. Labore incidunt qui. Laborum adipisci aut velit.
Quo omnis quam ut ut repellendus nihil libero quia. Fugit quod repudiandae consequatur. Dolorem cum fuga porro quisquam. Quaerat harum ab odit et id rerum non aliquid sapiente. Facilis qui illo et soluta omnis ut recusandae aut fugit. Temporibus cum quo qui voluptatem ipsa.
Quia assumenda voluptatum. Qui voluptas totam non adipisci voluptatibus et. Quis mollitia occaecati aut. Non rem error animi. Impedit omnis sit nobis.""",
    )

    db.session.add(product19)

    product20 = Product(
        name="Handmade Fresh Gloves",
        store_id=4,
        price=65.00,
        quantity=16,
        description="""Architecto dolor voluptas. Quo perspiciatis nisi ut cupiditate facere et. Expedita ducimus unde quibusdam aspernatur temporibus doloribus aut non. Enim fuga hic necessitatibus et animi eum ipsa eaque ex. Quasi qui facere dolorum voluptas voluptatum delectus.
Sint incidunt dolore. Sed quis eum occaecati eligendi qui. Quam fugiat autem magnam quia aspernatur ipsum. Voluptates iure quo. Tempore eos cupiditate dolores quasi excepturi et nisi debitis aut.
Aperiam natus quos aliquam molestiae dicta ullam praesentium. Dolores eum reiciendis dolor maxime. Consequatur minima assumenda illum odit consectetur. Magnam consectetur ducimus ut deserunt rerum dolorem dolores beatae.""",
    )

    db.session.add(product20)

    product21 = Product(
        name="Rustic Wooden Gloves",
        store_id=4,
        price=66.00,
        quantity=14,
        description="""Accusamus facilis eligendi aspernatur voluptas. Dolorem eveniet vel. Et doloribus aut labore. Libero blanditiis ducimus rem quod sint nesciunt quis. Dolorum ut voluptatum.
Sed ipsam quo mollitia. Est eos laudantium vero dolorem. Rerum quod voluptas qui eligendi porro placeat. Et ratione ex cupiditate rerum est nulla qui.
Totam nihil aperiam quo qui et similique ipsa aperiam. Molestiae ipsa dicta molestias id consectetur. Aliquam voluptatem molestiae. Illum architecto eveniet praesentium est. Illo excepturi sint ducimus corrupti praesentium odio.""",
    )

    db.session.add(product21)

    product22 = Product(
        name="Practical Cotton Bacon",
        store_id=1,
        price=120.00,
        quantity=6,
        description="""Consequatur repellat quaerat. Quis inventore sit ea est et ratione sed voluptas. Laborum praesentium iusto cum corrupti ut sed omnis beatae hic. Blanditiis ex atque. Ratione rem soluta qui nisi.
Qui eos dolorem consequuntur sint quis quas quod. Labore numquam beatae ut voluptates quae et quae et labore. Consequatur ipsam voluptas libero necessitatibus saepe. Sit corporis fugit qui voluptatum sit veritatis aut non. Inventore non et quasi reiciendis inventore. Perspiciatis incidunt vitae voluptatem sunt debitis repudiandae libero ipsam id.
Ab totam provident et perspiciatis ut qui aut. Necessitatibus dolorum autem qui aspernatur sapiente. Vitae iure omnis. Aut eligendi vitae architecto iste nihil perspiciatis animi voluptatem vitae.""",
    )

    db.session.add(product22)

    product23 = Product(
        name="Awesome Cotton Sausages",
        store_id=5,
        price=233.00,
        quantity=14,
        description="""Est deserunt porro illum voluptatem sit harum ipsa ut aut. Modi magni ut. Sit cupiditate ut labore quo consectetur labore ut rerum. Sed rerum non et suscipit facilis.
Ut et blanditiis natus sed nam. A adipisci perferendis numquam molestiae quia nihil labore eveniet dolorum. Harum ut excepturi aut et inventore corrupti laborum. Qui et id molestiae voluptates consectetur vero. Fuga dolore voluptates aut blanditiis.
Animi veritatis nihil soluta est. Consequatur consectetur quo velit rem ipsa et. Expedita eius est modi ratione fugiat voluptates laboriosam.""",
    )

    db.session.add(product23)

    product24 = Product(
        name="Incredible Metal Tuna",
        store_id=3,
        price=8.00,
        quantity=13,
        description="""Deserunt tempora totam dolor neque. Veniam sed aut optio at temporibus qui. Debitis sequi ipsam. Sit aliquid dolorum occaecati et earum rerum expedita temporibus quia. Iste voluptatem maxime sit libero accusamus quas rerum ut. Et animi eius at accusantium repellat non minima nisi.
Iste mollitia deleniti et voluptate minus exercitationem suscipit. Autem sit magnam ut aperiam est modi. Et sed necessitatibus sint praesentium nostrum quas est. Repellat ipsam occaecati aut. Quis autem vero eveniet nesciunt ipsum est delectus saepe.
Aut tempore atque nostrum eos. Voluptatem dolores repudiandae impedit quaerat officia fuga ut rem nisi. Quis earum optio. Hic necessitatibus aperiam sint laboriosam quas ut facere.""",
    )

    db.session.add(product24)

    product25 = Product(
        name="Handcrafted Metal Chair",
        store_id=2,
        price=62.00,
        quantity=12,
        description="""Deleniti consequatur cupiditate pariatur aut voluptatibus aut perspiciatis. Ducimus atque tempora est sint aut aut. Repudiandae ut laborum earum libero. Ea eum eum nulla nam est nobis sunt rerum voluptatum.
Reprehenderit ut nam sequi aut. Est fugiat saepe aut aliquam. Quaerat deserunt non vitae quidem voluptates omnis.
Quis esse modi saepe sint totam doloremque molestias. Labore placeat veritatis illo minima accusantium. Expedita nobis facere iure odit molestiae velit voluptas quia. Reiciendis officiis alias sit nulla.""",
    )

    db.session.add(product25)

    product26 = Product(
        name="Unbranded Concrete Shirt",
        store_id=3,
        price=104.00,
        quantity=7,
        description="""Officia sed quis. Voluptates et reprehenderit quidem ipsum eos ut dolor. Placeat qui eos est tempore harum omnis. Voluptatem ea quam quis omnis ipsum pariatur porro et. Maiores ipsa dolorum pariatur eius. Vitae laborum veniam at aliquid placeat atque architecto tempore.
Facilis dolor architecto ab. Quia recusandae quam debitis velit minima quia similique quo consequuntur. Ipsam tenetur doloribus dolores et quia quo mollitia. Quisquam ad fuga occaecati. Cupiditate id dolores provident quia et eius rerum velit ad.
Soluta laboriosam sit nostrum consequatur aliquam. Cum ut rerum eius praesentium. Ea ullam ipsam.""",
    )

    db.session.add(product26)

    product27 = Product(
        name="Generic Frozen Pizza",
        store_id=4,
        price=67.00,
        quantity=19,
        description="""Tempora iusto est dolores cum laborum natus. Et repudiandae est rerum autem. Tempore qui illo molestiae. Maiores tenetur et ducimus debitis distinctio non repellendus. Est magni dolores. Magnam debitis vero porro labore necessitatibus omnis.
Corrupti ut ad repudiandae consectetur voluptas eos fuga. Dignissimos animi asperiores voluptates cupiditate. Culpa tenetur sunt enim consequatur porro quis. Vitae similique et quae velit. Illo aut voluptate dolores quibusdam in magni cum.
Voluptatem quasi blanditiis. Provident corrupti quasi quia tempore eaque temporibus. Aut quidem voluptate qui et dolore pariatur consectetur.""",
    )

    db.session.add(product27)

    product28 = Product(
        name="Refined Soft Mouse",
        store_id=3,
        price=139.00,
        quantity=11,
        description="""Suscipit ex officia expedita sequi accusamus mollitia et ullam. Explicabo veritatis saepe fugit ut voluptatem beatae et. Illum iure quae voluptatum nam error nisi cum. Minus excepturi sequi optio quos. Harum alias sed. Error est repellendus qui sunt ut odio reiciendis et inventore.
Repudiandae sed hic porro. Veritatis sapiente nihil ut ex consequatur voluptate voluptas. Ipsa cumque aspernatur illum cum et labore atque laboriosam. Dignissimos quos et aut libero illo laboriosam.
Laborum commodi sed voluptas laudantium tempore. Itaque voluptatem veniam incidunt ut dolore exercitationem. Nisi eius tempore vero blanditiis odio omnis necessitatibus velit.""",
    )

    db.session.add(product28)

    product29 = Product(
        name="Small Steel Sausages",
        store_id=2,
        price=163.00,
        quantity=10,
        description="""Aut ad maiores voluptatum nesciunt laudantium. Error quod ut officiis voluptatem assumenda. Nobis ratione eveniet ea voluptas fugit neque suscipit molestiae modi. Suscipit quo at aut voluptatem a provident eveniet vel porro. Nam voluptatem nam doloremque dolorem nostrum provident temporibus quis. Incidunt quos aut a.
Quidem eius distinctio temporibus adipisci pariatur laborum numquam. Aperiam ut eum. Aut rerum est qui non voluptas.
Doloremque placeat labore ut unde suscipit. Qui fugiat explicabo itaque occaecati impedit enim ut quas in. Iusto eveniet laborum quibusdam reprehenderit saepe rerum sed. Illo cumque voluptas asperiores aut ut facere. Non vitae qui placeat temporibus ipsa quos optio vero.""",
    )

    db.session.add(product29)

    product30 = Product(
        name="Gorgeous Steel Keyboard",
        store_id=5,
        price=129.00,
        quantity=4,
        description="""Necessitatibus aliquam error voluptatem illo ipsa autem rerum. Nemo atque qui quod. Dolore eos est esse aut pariatur velit aut. Voluptates dolores aut et cumque qui voluptatibus. Illo neque alias voluptate occaecati impedit.
Corporis voluptatem harum et. Doloribus tempora ex illo repellendus impedit et laudantium. Eos consequatur dignissimos et facere eligendi. Est fugiat vero quaerat nam incidunt omnis qui. Ut magnam labore.
Cum qui repellat cum qui cumque expedita doloremque inventore. Rem esse quasi quo aliquam repellat architecto quas cum eum. Fugiat porro placeat deleniti modi velit nihil nihil eligendi quis. Quaerat ab sint facere laudantium tempore magnam.""",
    )

    db.session.add(product30)

    product31 = Product(
        name="Tasty Plastic Gloves",
        store_id=5,
        price=66.00,
        quantity=2,
        description="""Rerum quaerat et est exercitationem tenetur animi dolorem non atque. Debitis fugiat voluptatibus sed rem aut. Voluptatem id eligendi magnam nulla. Qui ipsa ipsum reprehenderit necessitatibus quis non. Inventore commodi et.
Aut vero nostrum distinctio veritatis temporibus. Doloremque quam ipsa libero. Culpa vel possimus aut dolore ullam adipisci et iste asperiores. Aliquam facere temporibus iste consectetur. Quis et et occaecati iusto doloribus sint voluptatum.
Consectetur perspiciatis voluptas. Rerum ipsam voluptas. Id ut non dolorem quod in et nemo dolor quaerat. Architecto vel earum sit eius velit. Architecto quasi repellendus voluptas quas expedita hic.""",
    )

    db.session.add(product31)

    product32 = Product(
        name="Ergonomic Rubber Chips",
        store_id=3,
        price=90.00,
        quantity=10,
        description="""Tempora tempore praesentium. Consequatur tempora omnis sunt eos ratione. Sit perferendis aut atque adipisci. Assumenda vel quia magni sunt rerum temporibus impedit. Doloremque provident hic mollitia voluptas.
Consequatur esse totam cumque quia sunt eum aut. Itaque quia voluptas. Omnis atque aut non. Consectetur aut aut in nam.
Exercitationem tempore quo accusantium amet sapiente eos exercitationem. Et rem velit sint aperiam recusandae veniam. Fugit assumenda ullam eos amet. Labore voluptatem iusto eos explicabo reprehenderit iure tempora. Itaque nulla minus est autem quam a.""",
    )

    db.session.add(product32)

    product33 = Product(
        name="Licensed Plastic Tuna",
        store_id=2,
        price=202.00,
        quantity=16,
        description="""Rerum quos molestiae quo mollitia. Odio a culpa eaque iusto modi. Qui ipsam adipisci porro dolorum omnis dolor hic earum est. Ipsam maxime nemo qui inventore sunt neque iusto aspernatur. Consequatur unde atque dignissimos doloremque sunt aspernatur minima voluptatem.
Sed quibusdam ad doloribus ut laboriosam. Quod architecto voluptas velit et praesentium qui similique reprehenderit ad. Quia nulla amet temporibus. Facilis in dolores ut quia soluta vero vitae.
Odit voluptates aut eligendi occaecati qui nam. Debitis est id est placeat aliquid quam a quidem debitis. Voluptatem molestias impedit est incidunt quia qui qui ipsum assumenda. Est aut corrupti iusto nemo dolor officia blanditiis dolorem. Occaecati quaerat eligendi.""",
    )

    db.session.add(product33)

    product34 = Product(
        name="Intelligent Rubber Gloves",
        store_id=1,
        price=35.00,
        quantity=15,
        description="""Minima eveniet quam accusamus consectetur maiores animi ad qui. Sed cupiditate beatae voluptas ratione ipsum aliquam animi dicta. Vitae maxime et architecto deleniti. Pariatur earum porro eveniet consequatur eum. Recusandae enim ut accusantium numquam deserunt esse. Sapiente a animi suscipit odio repellat eligendi tempore ducimus voluptatum.
Est magni ea et et non ut accusantium. Beatae nihil ut laborum omnis. Nam labore qui porro. Ut reprehenderit quaerat sint voluptates.
Non illum id. Hic necessitatibus fuga ad minus quis ratione porro non. Molestiae molestias sint laborum asperiores deserunt dolores. Et sed iusto accusamus esse amet est officia consequatur totam. Omnis officiis cum dicta voluptate in voluptatem explicabo consequatur. Voluptate est itaque perferendis.""",
    )

    db.session.add(product34)

    product35 = Product(
        name="Practical Frozen Soap",
        store_id=5,
        price=175.00,
        quantity=15,
        description="""Tenetur accusamus odit autem sunt sit qui consequuntur fugit qui. Quis explicabo temporibus aliquid accusantium minus esse culpa quidem non. A doloribus quia nisi alias rerum molestiae voluptas fugit. Et tempore cumque quo qui maxime nihil. Et exercitationem optio eum nesciunt.
Et adipisci quia. Sint recusandae excepturi explicabo non ducimus perspiciatis esse. Officiis fuga repudiandae placeat consectetur eum ut doloribus quam corporis. Sed cumque fuga. Molestiae qui eum voluptatem deleniti incidunt velit vero explicabo. Dolores et consequatur tempore est libero quaerat tempora sit.
Mollitia corrupti nemo odit. Quibusdam expedita sequi. Iure in autem eum consequatur harum ad iusto reiciendis. Officia odio quis voluptatem iste enim qui dolorem aliquam. Consectetur enim natus. Maiores quam aliquam quo sapiente.""",
    )

    db.session.add(product35)

    product36 = Product(
        name="Intelligent Granite Shirt",
        store_id=1,
        price=6.00,
        quantity=18,
        description="""Est mollitia perferendis et et. Debitis architecto voluptates qui aut. Sunt ut ex possimus adipisci ut necessitatibus ratione perferendis et. Dignissimos sunt facere qui nulla ad voluptas.
Autem et voluptates tempore odit doloremque quia eveniet. Adipisci nulla maiores tempora deserunt quia sed. Nostrum inventore aut eligendi voluptatum labore fuga doloribus. Iure voluptatibus sit quibusdam id necessitatibus voluptatibus repudiandae et. Labore possimus dolor. Sed quasi asperiores officia rerum quis fugit illum est sint.
Non magnam eaque rerum. Natus illum voluptas. Voluptatibus laborum corporis quasi voluptatibus temporibus est. Nobis qui deserunt beatae et. Blanditiis accusantium voluptas id alias ad dolorem officiis impedit.""",
    )

    db.session.add(product36)

    product37 = Product(
        name="Licensed Metal Bacon",
        store_id=1,
        price=181.00,
        quantity=7,
        description="""Ea modi pariatur voluptatem aut sit nihil veniam quod. At sunt itaque. Minima dolorum delectus et. Voluptate autem aut iure qui.
Harum blanditiis tempora unde omnis. Et dolorum dolorum sint eius in voluptatibus est quod. Error maiores porro dolorum fugit quas.
Reiciendis numquam ut commodi delectus. Voluptatem accusantium sed voluptatibus non sint adipisci perspiciatis voluptatum. Dolorum laboriosam asperiores et ea tempore ut sunt tempora. Quis ut ut accusantium. Necessitatibus harum occaecati corporis ullam corrupti.""",
    )

    db.session.add(product37)

    product38 = Product(
        name="Awesome Cotton Chicken",
        store_id=4,
        price=187.00,
        quantity=19,
        description="""Laboriosam quo sit deleniti iure possimus. Consequatur illo illo iure voluptatibus sunt culpa sit. Possimus asperiores repudiandae consequatur et amet sunt pariatur voluptatem facilis. Incidunt et nulla assumenda omnis reprehenderit pariatur est ullam.
Facere magni et et aut fuga. Voluptatibus similique neque repudiandae. Quo blanditiis dolores consequatur. Nesciunt similique saepe quaerat ut et. Autem deserunt pariatur nam excepturi. Voluptatibus omnis qui amet saepe voluptatem eum qui qui.
Repudiandae voluptatem natus perspiciatis exercitationem. Pariatur molestiae et perferendis voluptatem. Aperiam quisquam minima qui. Harum temporibus ex. Atque quia magni quod exercitationem qui enim dolores. Praesentium deleniti eaque explicabo expedita aperiam voluptas.""",
    )

    db.session.add(product38)

    product39 = Product(
        name="Ergonomic Rubber Sausages",
        store_id=5,
        price=220.00,
        quantity=15,
        description="""Ea nostrum id reiciendis et ipsam maiores consectetur omnis. Rerum amet unde. A excepturi consectetur a suscipit rerum eveniet et eum. Aperiam qui animi omnis rerum eum. Cum dolor expedita vel quo excepturi maxime. Doloremque facilis blanditiis ad et accusamus quod.
Eius corrupti tempore eaque aperiam iste doloribus. Quis quo assumenda voluptatem. Quod aut consequatur possimus nihil ullam aut voluptate.
Vel ab aut in excepturi id est libero cumque pariatur. Nostrum officiis qui commodi neque enim. Placeat tempore maiores aspernatur possimus sit sit quam nobis. Voluptatem optio consectetur et dolor aut quis omnis illum. Et dolores eum.""",
    )

    db.session.add(product39)

    product40 = Product(
        name="Rustic Frozen Keyboard",
        store_id=2,
        price=35.00,
        quantity=1,
        description="""Possimus repellendus sunt quae recusandae officiis. Molestias voluptate magni vitae repellat quia ut illo ipsa delectus. Veniam et doloremque.
Mollitia non veritatis. Est est quia dicta qui porro voluptates accusamus est eius. Reprehenderit explicabo maiores autem ea quod dolorem architecto sunt modi. Aut commodi ut. Qui ea ut fugit.
Accusantium sed enim non ut nobis non. Ut quia molestiae quae voluptatibus quia vero. Tempora iusto et.""",
    )

    db.session.add(product40)

    product41 = Product(
        name="Generic Granite Fish",
        store_id=4,
        price=172.00,
        quantity=8,
        description="""Beatae eaque iusto dignissimos natus saepe atque illo sit quo. Ex laudantium perspiciatis. Quasi exercitationem ipsa maiores. Laboriosam eius at ut sunt consequatur ipsam est. Odit molestiae aut quae dolorem impedit est dolore. Distinctio commodi accusantium.
Magnam maiores suscipit unde hic voluptatibus a magnam. Placeat omnis labore aut officia temporibus. Aspernatur sed quasi fugit in est rem. Vitae inventore earum et ratione aspernatur dolore rerum.
In suscipit qui similique quasi sunt sint officiis nam ut. Eveniet ea repudiandae aut placeat qui aliquid est voluptatem. Minima vero facere corrupti facere aut omnis. Qui omnis quo placeat cumque harum odio impedit nemo modi. Et veniam magni beatae alias qui veritatis praesentium totam velit. Ut incidunt vel id nisi quod dicta.""",
    )

    db.session.add(product41)

    product42 = Product(
        name="Handcrafted Rubber Tuna",
        store_id=4,
        price=22.00,
        quantity=2,
        description="""Ut quae et quia. Ea suscipit nostrum. Maiores iste modi repellat hic qui. Et nam dolor officia in facilis placeat pariatur blanditiis. Molestiae soluta perferendis iusto pariatur quae quae iste est veritatis.
Aut aliquam nisi minus adipisci sed reprehenderit. Nulla dolor iste ut architecto sapiente dolores placeat facilis eveniet. Est quos corporis in ipsam eaque qui. Modi itaque provident aut placeat consequatur. Cum mollitia et exercitationem numquam in.
Consequatur qui aliquam occaecati quia dolorum. Nobis id sint et ut ex dolore aut ea optio. Ut a quas eius tenetur ut. Molestiae impedit et atque modi atque voluptas est ut. Cupiditate quia aliquam vero totam omnis beatae. Repellat est ex qui temporibus molestiae et.""",
    )

    db.session.add(product42)

    product43 = Product(
        name="Sleek Plastic Cheese",
        store_id=1,
        price=236.00,
        quantity=3,
        description="""Dolor eligendi expedita. Illum mollitia et adipisci est saepe ipsam. Qui qui ea perspiciatis eum odit. Animi dolor dolores aut officia hic.
Eum et in ea ex est suscipit. Quo assumenda eligendi sint magnam provident quia dolor qui. Sit facilis autem asperiores officiis distinctio dolores. Fugit maxime ad et exercitationem omnis et beatae alias eum. Atque non fugiat at voluptatem qui repellat aperiam qui.
Quia mollitia ut et. Dolores omnis molestias sit magnam illo culpa officiis hic. Ullam quo eum in fugiat mollitia. Alias eveniet dignissimos quo ut.""",
    )

    db.session.add(product43)

    product44 = Product(
        name="Licensed Plastic Towels",
        store_id=1,
        price=239.00,
        quantity=7,
        description="""Repellendus aliquid aut vero nam cupiditate. Ab quas ut vel autem qui provident. Earum et ex unde dolores. Dolor vitae quia consectetur repudiandae.
Deleniti adipisci corporis numquam laborum recusandae in. Autem nisi voluptatem incidunt sed eos quo cum. Voluptatem quo minus corrupti facere incidunt pariatur reprehenderit facere. Repudiandae dolorum iure a.
Esse similique ipsa temporibus est reprehenderit. Aliquid voluptatem reiciendis culpa sunt. Eligendi et dolorum quisquam quis sunt atque. Veritatis quam officia et nulla voluptatem ea.""",
    )

    db.session.add(product44)

    product45 = Product(
        name="Licensed Wooden Chips",
        store_id=2,
        price=59.00,
        quantity=19,
        description="""Aliquid explicabo nam earum molestiae consequuntur animi ipsum. Officiis sapiente ea odit in voluptates beatae provident magni. Eum nihil aut.
Rerum quis in qui. Modi numquam eius dicta ut ea quod quos commodi minus. At voluptas qui eum aut quidem consequatur.
Animi dolorem quod repellendus sapiente qui. Deleniti beatae sint excepturi ut. Est pariatur delectus est quo occaecati. Tempore corporis aut maxime sint officiis eaque excepturi.""",
    )

    db.session.add(product45)

    product46 = Product(
        name="Incredible Steel Ball",
        store_id=2,
        price=177.00,
        quantity=2,
        description="""Dolorem laudantium eveniet dolor distinctio. Provident natus ipsam dignissimos voluptates. Omnis illum eligendi nulla velit sequi sapiente voluptate. Veritatis distinctio ea excepturi exercitationem. Molestiae hic inventore voluptas iusto ipsam. Illum rerum maiores a.
Dolores dicta dolores ad laborum soluta qui itaque quae blanditiis. Velit laudantium est optio sed sit quia. Ipsa totam modi cum laudantium minima ut velit beatae. Accusamus maxime iure non autem aut quia ab repudiandae. Qui pariatur sint. Quia explicabo et quia qui doloribus rem nam.
Quibusdam illo ipsam nostrum. Laboriosam quas autem dicta. Non dolorem itaque. Ullam fuga quo. Consectetur maxime consectetur vitae nobis. Maxime cumque sed.""",
    )

    db.session.add(product46)

    product47 = Product(
        name="Tasty Metal Pants",
        store_id=5,
        price=115.00,
        quantity=2,
        description="""Rerum ab ad sed ducimus rerum nostrum. Ea nihil dignissimos in voluptatum repudiandae. Non aut voluptas omnis nesciunt sit earum. Ad nobis quaerat et nihil delectus quia aliquid consequatur.
Laboriosam tempora aut quia enim voluptatum. Veniam explicabo nihil et. Ipsam aut rerum libero corporis inventore nam. Nam ut illum impedit earum corporis. Natus architecto debitis repellendus perferendis eligendi officiis quos corrupti et. Dolorem a est ut eligendi sit molestiae enim provident.
Cumque non odio iure expedita laborum ab culpa ut fuga. Totam ut odio magni nisi eos sapiente exercitationem quisquam rerum. Saepe nobis illo qui molestiae esse. Qui sed nihil perferendis sint perspiciatis ipsum sit quasi.""",
    )

    db.session.add(product47)

    product48 = Product(
        name="Ergonomic Wooden Table",
        store_id=2,
        price=244.00,
        quantity=19,
        description="""Fugit debitis deserunt omnis. Officiis fugiat aut aut veniam omnis nam ratione. Voluptate tempora sunt asperiores ex beatae ducimus repellat placeat. Ut iusto ut maxime labore commodi eaque ut.
Et maiores minus id deserunt quia autem porro blanditiis voluptas. Maiores atque error maxime nostrum culpa eaque. Mollitia delectus aut reprehenderit et aut minus dicta accusantium. Culpa saepe voluptatem aspernatur. Quo provident enim quo.
Ratione ullam mollitia quis ipsum aliquam sunt non. Ut dignissimos assumenda consequatur. Aliquam ea minima recusandae ut ratione.""",
    )

    db.session.add(product48)

    product49 = Product(
        name="Gorgeous Frozen Fish",
        store_id=2,
        price=224.00,
        quantity=3,
        description="""Quia suscipit in commodi totam temporibus sunt iure. Excepturi saepe maiores et sed ut. Odio et iste aut illo eaque ipsam ratione excepturi est. Nihil a non cum et inventore.
Eum dolore reprehenderit. Aut itaque enim voluptas. Sed atque aliquid tenetur ut accusantium incidunt fuga atque perspiciatis. Quia quas laborum.
Sunt consequatur autem. Deleniti fugiat asperiores suscipit magnam voluptatibus a. Mollitia facilis nam. Consequatur deleniti inventore eius. A sed eum magni earum.""",
    )

    db.session.add(product49)

    product50 = Product(
        name="Intelligent Metal Mouse",
        store_id=4,
        price=22.00,
        quantity=12,
        description="""Est aut laudantium aut consequatur. Dolorem consectetur dicta suscipit vel necessitatibus consequuntur neque minima qui. Quisquam saepe quo omnis velit incidunt. Consequatur dolores possimus et excepturi.
Accusamus molestiae perferendis hic eos sed. Distinctio a ea possimus id perferendis est ducimus neque omnis. Odio libero inventore. Soluta commodi odio dolor magni.
Saepe omnis eaque numquam recusandae. Cupiditate perspiciatis dolorem optio consequatur dolorum voluptas magni quia. Sed mollitia ut voluptatem veritatis. Deleniti tenetur velit. Accusamus facere magnam porro id animi officia. Hic ea laboriosam facere aliquid omnis molestiae ipsam dolor.""",
    )

    db.session.add(product50)

    db.session.commit()


def undo_products():
    db.session.execute('TRUNCATE stores RESTART IDENTITY CASCADE;')
    db.session.commit()
