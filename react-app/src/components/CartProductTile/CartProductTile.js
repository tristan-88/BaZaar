import React, { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { NavLink } from 'react-router-dom'
import './CartProductTile.css'

const CartProductTile = ({ product }) => {

  const cart = useSelector(state => state.cart)

  console.log(cart)

  return (
    <div className='cart-card-wrapper'>
      <div>
        <NavLink to={`/products/${product.id}`}>
          <img className='thumbnail' src={product.photos[0].photo_url}></img>
        </NavLink>
      </div>
      <div>
        {product.description}
      </div>
      <div>
        {product.price}
      </div>
    </div>
  )

}

export default CartProductTile;