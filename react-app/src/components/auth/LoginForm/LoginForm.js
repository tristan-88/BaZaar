import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { Redirect } from "react-router-dom";
import { login } from "../../../store/session";
import { createCart } from "../../../store/cart";
import './LoginForm.css'

const LoginForm = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    await dispatch(createCart());
    if (data.errors) {
      setErrors(data.errors);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="form-body">
    <div className="form-container">
      <form onSubmit={onLogin} className="login-form">
        <div className="form-inputs">
        <div>
          {errors.map((error) => (
            <div>{error}</div>
          ))}
        </div>
        <h1>Welcome!</h1>
        <div>
          <label htmlFor="email">Email</label>
          <input
            name="email"
            type="text"
            placeholder="Email"
            value={email}
            onChange={updateEmail}
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            name="password"
            type="password"
            placeholder="Password"
            value={password}
            onChange={updatePassword}
            />
          </div>
        </div>
          <div className="button-div">
            <button type="submit">Login</button>
        </div>
      </form>
    </div>
    </div>
  );
};

export default LoginForm;
