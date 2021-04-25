const faker = require('faker')
const bcrypt = require('bcryptjs')


// call with num 1 less than max
const randomNumber = (num) => Math.floor(Math.random() * Math.floor(num) + 1)

// const seed_user = (num) => {

//   let i = 0
//   while (i < num) {

//     const user = {
//       first_name: faker.name.firstName(),
//       last_name: faker.name.lastName(),
//       email: faker.internet.email(),
//       username: faker.internet.userName(),
//       address: faker.address.streetAddress(true),
//       hashed_password: bcrypt.hashSync(faker.internet.password()),
//     }

//     console.log(user)
//     i++
//   }

// }

// seed_user(100)


// const seed_store = (num) => {
//   let i = 0
//   while (i < 0) {
//     const store = {
//       location: faker.address.streetAddress(true),
//       user_id: randomNumber(99),
//       description: faker.lorem.paragraphs(2)
//     }

//     console.log(store)
//     i++
//   }
// }

// seed_store(100)

// const seed_product = (num) => {
//   let i = 0
//   while (i < num) {

//     const product = {
//       name: faker.commerce.productName(),
//       store_id: randomNumber(19),
//       price: faker.commerce.price(1, 250, 2),
//       quantity: randomNumber(20),
//       description: faker.lorem.paragraphs(3),
//     }

//     console.log(product)
//     i++
//   }

// }

// seed_product(100)

// const seed_product_tag = (num) => {
//   let i = 0
//   while (i < num) {
//     const tag = {
//       product_id: randomNumber(100),
//       tag_id: randomNumber(5)
//     }
//     console.log(tag)
//     i++
//   }
// }

// seed_product_tag(200)

// const seed_review = (num) => {
//   let i = 0
//   while (i < num) {
//     const review = {
//       product_id: randomNumber(100),
//       user_id: randomNumber(100),
//       content: faker.lorem.paragraph(randomNumber(5)),
//       createdAt: faker.date.past()
//     }

//     i++
//   }
// }

// seed_review(300)

// const seed_favorite = (num) => {
//   let i = 0
//   while (i < num) {
//     const favorite = {
//       product_id: randomNumber(100),
//       user_id: randomNumber(100)
//       created_at: faker.date.past()
//     }
//     console.log(favorite)
//     i++
//   }
// }

// seed_favorite(500)
