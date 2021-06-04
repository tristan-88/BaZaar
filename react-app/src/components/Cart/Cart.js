import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom'
import { createCart, completeOrder } from '../../store/cart'
import SmallProductTile from '../SmallProductTile/SmallProductTile'
import CartProductTile from '../CartProductTile/CartProductTile'
import './Cart.css'


function Cart() {
	const dispatch = useDispatch()
	const history = useHistory()
	const cart = useSelector(state => state.cart)
	const user = useSelector(state => state.session.user)
	const [total, setTotal] = useState(0)
	const [errors, setErrors] = useState([])

	//look at when ever something here changes reload this component
	useEffect(() => {
		dispatch(createCart())
	}, [dispatch])

	useEffect(() => {

	}, [errors])


	if (!cart.products) {
		return null
	}

	if (cart.products) {
		cart.products.forEach(product => {
			if (product.quantity > product.product.quantity && !errors.includes(`You have too many ${product.product.name.split(' ').slice(0, 6).join(' ')} in your cart.`)) {
				errors.push(`You have too many ${product.product.name.split(' ').slice(0, 6).join(' ')} in your cart.`)
			}
		})
	}

	const confirmOrder = async () => {

		let btn = window.document.getElementById('checkout-btn')
		btn.innerText = "Thank you!"
		return <Redirect path='/home' />
	}

	return (
		<>
			{cart && (
				<div>
					<div className="cart-title">
						<h1>{`Welcome, ${user.username}!`}</h1>
					</div>
					<div className="tagline">
						<h3>Here are the items in your cart.</h3>
					</div>
					<br></br>
					<div className="span-divider"></div>
					<div className="cart-items-wrapper">
						<div className="cart-items">
							{cart.products.map((product, i) => (
								<div key={i} className="cit-tile-wrapper" id={`item-${i}`}>
									<CartProductTile cartId={cart.id} qty={product.quantity} setTotal={setTotal} total={total} product={product.product} id={i} />
								</div>
							))}
						</div>
						<div className="sidebar-main-wrapper">
							<div className="sidenav">
								<div className="sb-item-total">{`Total Items: ${cart.products.length}`}</div>
								<div className="sb-shipping">
									Shipping:</div>
								<div className="radio-shipping">
									<input type="radio" value="Standard" name="shipping" /> Standard Shipping: Free
										<input type="radio" value="Express" name="shipping" /> Express: $10.00
										<input type="radio" value="OverNight" name="shipping" /> Over Night: $20.00

								</div>

								<div className="sb-total">Grand Total: ${total.toFixed(2)}</div>
								{errors.length > 0 &&
									<ul>
										{errors.map(error => <li>{error}</li>)}
									</ul>
								}
								{!errors.length &&
									<div id='checkout-btn' onClick={completeOrder}>Proceed to Checkout</div>
								}
							</div>
						</div>
					</div>
					<div className="span-divider"></div>
				</div>
			)}
		</>
	);
}

export default Cart;
