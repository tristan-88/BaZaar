const faker = require('faker')
// const fs = require('fs')

// call with num 1 less than max
const randomNumber = (num) => Math.floor(Math.random() * Math.floor(num) + 1)

// const seed_user = (num) => {

//   let i = 1
//   console.log(`
// def seed_users(): `
//   )

//   while (i <= num) {
//     const string = `
//     user${i} = User(
//         first_name= "${faker.name.firstName()}",
//         last_name= "${faker.name.lastName()}",
//         email= "${faker.internet.email()}",
//         username= "${faker.internet.userName()}",
//         address= "${faker.address.streetAddress(true)}",
//         hashed_password= "${faker.internet.password()}",
//     )`

//     console.log(string)
//     console.log("")
//     console.log(`
//     db.session.add(user${i})`
//     )
//     console.log("")
//     console.log("")

//     i++
//   }
//   console.log(`
//     db.session.commit()`)
//   console.log("")
//   console.log("")
//   console.log(`

// def undo_users():
//     db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
//     db.session.commit()
// `)
// }

// seed_user(5)

// const seed_store = (num) => {
//   let i = 1
//   console.log(`
// def seed_stores():`)
//   while (i <= num) {
//     const string = `
//     store${i} = (
//         name= "${faker.company.companyName()}",
//         location= "${faker.address.streetAddress(true)}",
//         userId= ${i},
//         description= """${faker.lorem.paragraphs(2)}"""
//     )`
//     console.log(string)
//     console.log("")
//     console.log(`
//     db.session.add(store${i})`)
//     console.log("")
//     console.log("")
//     i++
//   }
//   console.log(`
//     db.session.commit()`)
//   console.log("")
//   console.log("")
//   console.log(`
// def undo_store():
//     db.session.execute('TRUNCATE stores RESTART IDENTITY CASCADE;')
//     db.session.commit()
// `)
// }

// seed_store(6)

const seed_product = (num) => {
  let i = 0

  while (i <= num) {
    const string = `
    product${i} = Product(
        name= "${faker.commerce.productName()}",
        storeId= ${randomNumber(5)},
        price= ${faker.commerce.price(1, 250, 2)},
        quantity= ${randomNumber(20)},
        description= """${faker.lorem.paragraphs(3)}""",
    )`
    console.log(string)
    console.log("")
    console.log(`
    db.session.add(product${i})`)
    console.log("")
    console.log("")
    i++
  }
  console.log(`
    db.session.commit()`)
  console.log("")
  console.log("")
  console.log(`
def undo_store():
    db.session.execute('TRUNCATE stores RESTART IDENTITY CASCADE;')
    db.session.commit()
    `)
}

seed_product(50)

// const seed_product_tag = (num) => {
//     let i = 0
//     console.log(`
// def seed_tags():`)
//     while (i <= num) {
//         const string = `
//     tag${i} = {
//         productId: ${randomNumber(100)},
//         tagId: ${randomNumber(5)}
//     }`
//         console.log(string)
//         console.log("")
//         console.log(`
//     db.session.add(tag${i})`)
//         console.log("")
//         console.log("")
//         i++
//     }
//     console.log(`
//     db.session.commit()`)
//     console.log("")
//     console.log("")
//     console.log(`
// def undo_tag():
//     db.session.execute('TRUNCATE tag RESTART IDENTITY CASCADE;')
//     db.session.commit()`)
// }

// seed_product_tag(5)

// const seed_review = (num) => {
//     let i = 0
//     console.log(`
// def seed_reviews():`)
//     while (i <= num) {
//         const string = `
//     review${i} = {
//         productId: ${randomNumber(100)},
//         userId: ${randomNumber(100)},
//         content: "${faker.lorem.paragraph(randomNumber(5))}",
//         createdAt: ${faker.date.past()}
//     }`
//         console.log(string)
//         console.log("")
//         console.log(`
//     db.session.add(review${i})`)
//         console.log("")
//         console.log("")
//         i++
//     }
//     console.log(`
//     db.session.commit()`)
//     console.log("")
//     console.log("")
//     console.log(`
// def undo_review():
//     db.session.execute('TRUNCATE review RESTART IDENTITY CASCADE;')
//     db.session.commit()`)
// }

// seed_review(5)

// const seed_favorite = (num) => {
//     let i = 0
//     console.log(`
// def seed_favorites()`)
//     while (i <= num) {
//         const string = `
//     favorite${i} = {
//         productId: ${randomNumber(100)},
//         userId: ${randomNumber(100)}
//     }`
//         console.log(string)
//         console.log("")
//         console.log(`
//     db.session.add(favorite${i})`)
//         console.log("")
//         console.log("")
//         i++
//     }
//     console.log(`
//     db.session.commit()`)
//     console.log("")
//     console.log("")
//     console.log(`
// def undo_favorite():
//     db.session.execute('TRUNCATE favorite RESTART IDENTITY CASCADE;')
//     db.session.commit()`)
// }

// seed_favorite(5)
