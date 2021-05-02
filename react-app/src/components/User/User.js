import React from "react";
import { useSelector } from 'react-redux';
import "./User.css"
import Store from '../Store/Store';
import ShopForm from '../ShopForm/ShopForm';
import ProductForm from '../ProductForm/ProductForm';

function User() {
  const user = useSelector(state => state.session.user)
  const store = useSelector(state => state.store)
  if (!user) {
    return null;
  }

  let sessionLinks;
  if (store) {
    sessionLinks = (
      <>
        <strong>My Shop!</strong>
        <Store />
        <h1>Add Product</h1>
        <ProductForm />
      </>
    )
  } else {
    sessionLinks = (
      <>
        <h1>Would you like to create a shop?</h1>
        <ShopForm />
      </>
    )
  }

  return (
      <div>
        <div>
          <strong>First Name: </strong> {user.first_name}
        </div>
        <div>
          <strong>Last Name: </strong> {user.last_name}
        </div>
        <div>
          <strong>Email: </strong> {user.email}
        </div>
        <div>
          <strong>Username: </strong> {user.username}
        </div>
        <div>
          <strong>Address: </strong> {user.address}
        </div>
        <div>
          <strong>Profile Photo</strong>
        </div>
        <div>
          <img src={user.photo_url} alt="User profile picture"/>
        </div>
        <div>
          {sessionLinks}
        </div>
      </div>
  );
}

export default User;
