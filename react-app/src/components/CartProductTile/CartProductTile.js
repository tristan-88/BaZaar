import React, { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { NavLink } from 'react-router-dom'
import './CartProductTile.css'

const CartProductTile = ({ product, id, cartId }) => {



  const removeItem = async (id) => {
    let item = document.getElementById(id)
    await fetch(`/api/carts/${cartId}/remove/${product.id}`)
    console.log('click', id)
    if (item) {
      item.remove()
    }
  }

  return (
		<div className="cit-cart-item">
			<div>
				<NavLink to={`/products/${product.id}`}>
					<img
						className="cit-thumbnail"
						src={product.photos[0].photo_url}
					></img>
				</NavLink>
			</div>
		  <div className="cit-item-name">{`${product.name}`}</div>
		  <div className="cit-right-attributes">
			<div className="cit-item-price-X">
				<div
					className="cit-remove-btn"
					id={id}
					onClick={(e) => removeItem(`item-${e.target.id}`)}
				>
					<i className="fa fa-trash" id={id} aria-hidden="true">
						Remove
					</i>
			  </div>
			  <div className="cit-qty">
				  {`Quantity: ${product.cartQty}  ` }
			  </div>
				<div className="cit-price">
				  {`Price: $${product.price}`}
				  </div>
			  </div>
			</div>
		</div>
	);
}

export default CartProductTile;