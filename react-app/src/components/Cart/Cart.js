import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { createCart } from '../../store/cart'
import SmallProductTile from '../SmallProductTile/SmallProductTile'
import CartProductTile from '../CartProductTile/CartProductTile'
import './Cart.css'


function Cart() {
    const dispatch = useDispatch()
    const cart = useSelector(state => state.cart)
    const user = useSelector(state => state.session.user)


    //look at when ever something here changes reload this component
    useEffect(() => {
        dispatch(createCart())
    }, [dispatch])

    if (!cart.products) {
        return null
    }
    let cartItems;
    if (cart) {
        const uniqueProduct = {}
        const sortedProducts = {}
        // const sortedProducts = JSON.parse(JSON.stringify(cart.products))
        // sortedProducts.sort((a,b) => a.product_id - b.product_id)
        for (const product of cart.products) {
            uniqueProduct[product.product.id] = product.product;
            if (!sortedProducts[product.product_id]) {
                 sortedProducts[product.product_id] = 0
            }
            sortedProducts[product.product_id]++
        }
        for (const key in uniqueProduct) {
            uniqueProduct[key].cartQty = sortedProducts[key]
        }
        
        cartItems = Object.values(uniqueProduct)
        console.log(uniqueProduct)
        console.log(sortedProducts)

        // cartItems = cart.products?.map(product => (
        //     product.product
        // ))
    }

    return (
			<>
				{cartItems && (
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
							{/* <div className="cart-items">
								{cart.products.map((product, i) => (
									<div key={i} className="cit-tile-wrapper" id={`item-${i}`}>
										<CartProductTile
											cartId={cart.id}
											product={product.product}
											id={i}
										/>
									</div>
								))}
							</div> */}
							<div className="cart-items">
								{cartItems.map((product, i) => (
									<div key={i} className="cit-tile-wrapper" id={`item-${i}`}>
										<CartProductTile
											cartId={cart.id}
											product={product}
                                            id={i}
										/>
									</div>
								))}
							</div>
							<div className="sidebar-main-wrapper">
								<div class="sidenav">
									<p className="sb-item-total">Items</p>
									<p className="sb-shipping">Shipping</p>
									<p className="sb-total">Total</p>
									<a href="#">Proceed to Checkout</a>
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