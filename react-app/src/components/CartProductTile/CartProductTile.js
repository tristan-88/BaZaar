import React, { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { NavLink } from 'react-router-dom'
import './CartProductTile.css'
import { decrementItemCount, incrementItemCount } from "../../store/cart";

const CartProductTile = ({ product, id, cartId, qty, setTotal, total, setCartChange, cartChange }) => {
	const dispatch = useDispatch()
	// useEffect(() => {
	// 	setTotal(total + product.price * qty)
	// }, [])

	const removeItem = async (id) => {
		let item = document.getElementById(id)
		await fetch(`/api/carts/${cartId}/remove/${product.id}`)
		if (item) {
			item.remove()
		}
	}

	const decrementProduct = async () => {
		await dispatch(decrementItemCount(cartId, product.id))
		setCartChange(!cartChange)
	}

	const incrementProduct=  async () => {
		await dispatch(incrementItemCount(cartId ,product.id))
		setCartChange(!cartChange);
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
			<div className="cit-item-name">{`${product.name.split(' ').slice(0, 6).join(' ')}`}</div>
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
					<div className="">

						{`In Stock: ${product.quantity}`}
					</div>
					<div className="cit-qty">
						<button disabled={qty === 0 } onClick={decrementProduct}>-</button>
						<button disabled={qty === product.quantity } onClick={incrementProduct}>+</button>
						{`In Cart: ${qty}  `}
					</div>

					<div className="cit-price">
						{`Price: $${product.price.toFixed(2)}`}
					</div>
					<div className="cit-price">
						{`Total: $${(product.price * qty).toFixed(2)}`}
					</div>
				</div>
			</div>
		</div>
	);
}

export default CartProductTile;