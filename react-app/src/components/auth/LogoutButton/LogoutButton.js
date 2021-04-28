import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../../store/session";
import { removeCart } from "../../../store/cart"
import { removeProducts } from "../../../store/product";
import './LogoutButton.css'
const LogoutButton = () => {
  const dispatch = useDispatch()
  const onLogout = async (e) => {
    await dispatch(removeCart());
    await dispatch(logout());
  };

  return <button onClick={onLogout}>Logout</button>;
};

export default LogoutButton;
