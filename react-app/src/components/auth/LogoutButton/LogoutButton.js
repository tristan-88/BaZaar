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

  return <button className='logout-button' onClick={onLogout}> <i class="fad fa-sign-out-alt" fa-f3></i></button>;
};

export default LogoutButton;
