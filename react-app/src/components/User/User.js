import React from "react";
import { useSelector } from 'react-redux';
import "./User.css"
import Store from '../Store/Store';
import ShopForm from '../ShopForm/ShopForm';
import ProductForm from '../ProductForm/ProductForm';
import './User.css';
import Footer from '../Footer/Footer'

function User() {
  const user = useSelector(state => state.session.user)
  const store = useSelector(state => state.store)
  if (!user) {
    return null;
  }

  let sessionLinks;


  return (
    <div>
      <h2>Profile</h2>
      <div className="profile-info">
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
      </div>
      <img id="profile-photo" src={user.photo_url} alt="User profile picture" />
      <div className="shop-container">
        {sessionLinks}
      </div>
    </div>
  );
}

export default User;
