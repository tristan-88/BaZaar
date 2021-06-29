# Bazaar
-------------------
*Created By Andrew Thurman, Nathaniel Ortega, Tristan San-Juan, and Troy Dawson - [Visit Bazaar](https://bazaar-aa.herokuapp.com/)*


## Bazaar Overview
--------------------------
Bazaar is a fullstack application built using Flask, React, & Redux that mimics the functionality of [Etsy](https://www.etsy.com/) on a smaller scale.

Users can interact with 100 active product listings directly from Etsy. Create their own listing, create their own store, and checkout items in a mock cart.

## Application Architecture
---------------------
As previously stated Bazaar is a fullstack application built with Python and Javascript libraries while integrating Postgresql as the database of choice. All of the frontend and backend logic was built by our team while the data we used to seed the database comes directly from the [Etsy Api](https://www.etsy.com/developers/documentation/reference/listingproduct). Below is the full list of technologies used.

## Backend Overview
---------------------
Bazaar is a feature heavy website. So it goes without saying that Bazaar features a robust API that our team spent many long nights creating and refactoring.

### **Backend Technologies Used**
**Flask**

Flask allowed us a great deal of versatility in how we designed our database so in this backend heavy project it was the easy choice. **`Bazaar's database is defined by 10 different models, 41 different routes, & 8 different seeder functions.`** The product listing and product photo seeders both utilize an external API call to seed the database with Etsy's active listings.

**SQLAlchemy**

SQLAlchemy is an ORM who's power allowed us to make queries that allow users to dynamically search and filter results from the database. While allowing us the developers to easily manage the data coming back from Redux.

**Postgres**

Postgres utilizes a relational database, which allows for increased data accuracy making the chances of duplicated data zero. The Flexibility of Postgres was also a key selling point, it allows for easy scaling up or down and makes future features easy to implement.


**Etsy API**

As mentioned in previous sections we utilized the Etsy Api to fill our database with product listings and product photos directly from Etsy's active listings endpoint. By using this data it gives a true sense of the variety of products available on Etsy, and by proxy Bazaar. Thanks to Etsy and this Api we were able to backwards engineer the response to fit into our own database seamlessly.


## Frontend Overview
----------------------
Bazaar also features a robust front end powered by React and Redux. Below are the Technologies and Libraries used.

### **Frontend Technologies Used**

**React**

The core of the frontend is the popular framework React. Bazaar Forgoes many of the react-libraries available in favor of raw design and engineering. Which helped us as developers better understand react and the logic involved in many of these popular libraries available to us. Bazaar includes a lot of different components that were designed for modularity, reusability, and testability.
**Redux**

Redux was used to manage the applications state and make fetch calls to the backend to perform a variety of functionality including creating, deleting, populating and sorting data.

All of the data received from the backend is stored in the store creating a slightly longer initial load time, but allowing for an extremely quick user experience after that load is completed.


## Final Thoughts
-------
This app was created in eight days by four student developers. The scope of this project is honestly quite hard to describe. We created this app using a brand new stack and it was our first attempt at a feature rich project. Having just learned Python two weeks before, redux three weeks before, and react a month before we came out of this project more confident despite the blood and tears that this app was built on. 🤦‍♂️🤦‍♀️ This project we also used proper git workflow to allow all of us to work on features individually, using pair programming, and as a collective group. Thank you so much for taking the time to read this. 🦆🐍
