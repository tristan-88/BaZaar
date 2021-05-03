import React, {useEffect, useState}from 'react';
import { NavLink, Link } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux'
import LogoutButton from './../auth/LogoutButton/LogoutButton';
import Search from '../Search/Search';
import './NavBar.css'
import createCart from '../../store/cart'


const NavBar = () => {
  const dispatch = useDispatch()
  const cart = useSelector(state => state.cart?.products)

  const user = useSelector(state => state.session?.user)

      const [loaded, setLoaded] = useState(false)
  useEffect(() => {
     dispatch(createCart)
    },[dispatch])

  return (

    <nav>
      <div className='navigation-bar-container'>
        <NavLink to="/" exact={true} >
          <i class="fad fa-home-lg fa-4x" style={{ fontSize: '1.5em', color: 'darkorange' }}></i>
        </NavLink>
        <Search />
        <div className='interface-buttons'>
          <div className='login-button'>
            {!user && <NavLink to="/login" exact={true} activeClassName="active">
              <i class="fad fa-sign-in fa-4x" style={{ fontSize: '1.5em', color: 'darkorange' }}></i>
            </NavLink>}
          </div>
          {!user && <NavLink to="/sign-up" exact={true} activeClassName="active">
            <i class="fad fa-user-plus fa-4x" style={{ fontSize: '1.5em', color: 'darkorange' }}></i>
          </NavLink>}
          <NavLink to="/users" exact={true} activeClassName="active">
            {user && <i class="fad fa-users fa-4x" style={{ fontSize: '1.5em', color: 'darkorange' }}></i>}
          </NavLink>
          <NavLink to='/store' >
            <i class="fas fa-store-alt" style={{ fontSize: '1.5em', color: 'darkorange' }}></i>
          </NavLink>
          
          <NavLink to='/cart'>
            <i class="fad fa-shopping-cart fa-4x" style={{ fontSize: '1.5em', color: 'darkorange' }}></i> <div>{cart?.length}</div>
          </NavLink>
          <LogoutButton />
        </div>
      </div>
    </nav>

  );
}

export default NavBar;
