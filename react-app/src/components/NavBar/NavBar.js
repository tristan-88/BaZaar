import React from 'react';
import { NavLink, Link } from 'react-router-dom';
import { useSelector } from 'react-redux'
import LogoutButton from './../auth/LogoutButton/LogoutButton';
import Search from '../Search/Search';
import './NavBar.css'

const NavBar = () => {
  const cart = useSelector(state => state.cart?.products)

  const user = useSelector(state => state.session?.user)

  return (
    <nav>
      <div className='navigation-bar-container'>
        <NavLink to="/" exact={true} >
          <i class="fad fa-home-lg fa-4x"></i>
        </NavLink>
        {!user && <NavLink to="/login" exact={true} activeClassName="active">
          <i class="fad fa-sign-in fa-4x"></i>
        </NavLink>}
        {!user && <NavLink to="/sign-up" exact={true} activeClassName="active">
          <i class="fad fa-user-plus fa-4x" ></i>
        </NavLink>}
        <NavLink to="/users" exact={true} activeClassName="active">
         {user && <i class="fad fa-users fa-4x"></i>}
        </NavLink>
        <LogoutButton />
        <div className="search-bar">
          <Search />
        </div>
        <NavLink to='/cart'>
          <i class="fad fa-shopping-cart fa-4x"></i> <div>{cart?.length}</div>
        </NavLink>
      </div>
    </nav>
  );
}

export default NavBar;
