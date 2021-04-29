import React from 'react';
import { NavLink, Link } from 'react-router-dom';
import LogoutButton from './../auth/LogoutButton/LogoutButton';
import Search from '../Search/Search';
import './NavBar.css'

const NavBar = () => {
  return (
    <nav>
        <div className='navigation-bar-container'>
        <div className='home-page-button'>
          <NavLink to="/" exact={true} >
          <i class="fad fa-home-lg fa-4x"></i>
          </NavLink>
        </div>
          <div className='search-bar-container'>
          <Search />
          </div>
        <div>
        <NavLink to="/login" exact={true} activeClassName="active">
          <i class="fad fa-sign-in fa-4x"></i>
          </NavLink>
        </div>
          <NavLink to="/sign-up" exact={true} activeClassName="active">
          <i class="fad fa-user-plus fa-4x" ></i>
          </NavLink>
          <NavLink to="/users" exact={true} activeClassName="active">
          <i class="fad fa-users fa-4x"></i>
          </NavLink>
          <LogoutButton />
        </div>
    </nav>
  );
}

export default NavBar;
