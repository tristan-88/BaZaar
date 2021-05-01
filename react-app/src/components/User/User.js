import React from "react";
import { useSelector } from 'react-redux';
import "./User.css"

function User() {
  const user = useSelector(state => state.session.user)

  if (!user) {
    return null;
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
          <strong>Email</strong> {user.email}
        </div>
        <div>
          <strong>Username</strong> {user.username}
        </div>
        <div>
          <strong>Address</strong> {user.address}
        </div>
        <div>
          <strong>Profile Photo</strong>
        </div>
        <div>
          <img src={user.photo_url} alt="User profile picture"/>
        </div>
      </div>
  );
}

export default User;
