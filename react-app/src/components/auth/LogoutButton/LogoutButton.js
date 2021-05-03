import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { logout } from "../../../store/session";
import { removeCart } from "../../../store/cart"
import { removeProducts } from "../../../store/product";
import './LogoutButton.css'


const LogoutButton = () => {
  const user = useSelector(state => state.session.user)
  const dispatch = useDispatch()
  const onLogout = async (e) => {
    await dispatch(logout());
  };

  return(
    <div
     onClick={onLogout}>
     {/* <button type='submit'>LogOut</button> */}
     {user && <i class="fad fa-sign-out fa-5x" style={{fontSize:'1.5em', color:'darkorange'}}></i>}
    </div>

  )
};

export default LogoutButton;
