import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { Redirect } from 'react-router-dom';
import { signUp } from '../../../store/session';
import { createCart } from '../../../store/cart';
import './SignUpForm.css';

const SignUpForm = () => {
  const dispatch = useDispatch()
  const user = useSelector(state => state.session.user)
  const [image, setImage] = useState(null);
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [address, setAddress] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");


  const onSignUp = async (e) => {
    e.preventDefault();

    if (password === repeatPassword) {
      await dispatch(signUp(firstname, lastname, username, email, image, password, address));
      await dispatch(createCart())
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  const updateFirstname = (e) => {
    setFirstname(e.target.value)
  }

  const updateLastname = (e) => {
    setLastname(e.target.value)
  }

  const updateAddress = (e) => {
    setAddress(e.target.value)
  }

  const updateImage = (e) => {
    const file = e.target.files[0];
    setImage(file);
  }

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <form onSubmit={onSignUp}>
      <div>
        <label>First Name</label>
        <input
          type="text"
          name="first_name"
          onChange={updateFirstname}
          value={firstname}
        ></input>
      </div>
      <div>
        <label>Last Name</label>
        <input
          type="text"
          name="last_name"
          onChange={updateLastname}
          value={lastname}
        ></input>
      </div>
      <div>
        <label>Address</label>
        <input
          type="text"
          name="address"
          onChange={updateAddress}
          value={address}
        ></input>
      </div>
      <div>
        <label>Email</label>
        <input
          type="text"
          name="email"
          onChange={updateEmail}
          value={email}
        ></input>
      </div>
      <div>
        <label>Username</label>
        <input
          type="text"
          name="username"
          onChange={updateUsername}
          value={username}
        ></input>
      </div>
      <div>
        <label>Photo Url</label>
        <input
          type="file"
          accept="image/*"
          onChange={updateImage}
        ></input>
      </div>
      <div>
        <label>Password</label>
        <input
          type="password"
          name="password"
          onChange={updatePassword}
          value={password}
        ></input>
      </div>
      <div>
        <label>Confirm Password</label>
        <input
          type="password"
          name="repeat_password"
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required={true}
        ></input>
      </div>
      <button type="submit">Sign Up</button>
    </form>
  );
};

export default SignUpForm;
