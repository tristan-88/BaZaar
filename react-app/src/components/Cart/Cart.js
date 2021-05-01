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

    let cartItems;
    if (cart) {
        cartItems = cart.products?.map(product => (
            product.product
        ))
    }

    return (
        <>
            { cartItems &&
                <div>
                    <div className="cart-title">
                        <h1>{`Welcome, ${user.username}!`}</h1>
                    </div>
                    <div className='tagline'>
                        <h3>Here are the items in your cart.</h3>
                    </div>
                    <br></br>
                    <div className='span-divider'></div>
                    <div className='cart-items-wrapper'>
                        <div className='cart-items'>
                            {cart.products.map((product, i) => (
                                <div key={i} className='cit-tile-wrapper' id={`item-${i}`}>
                                    <CartProductTile cartId={cart.id} product={product.product} id={i} />
                                </div>
                            ))}
                        </div>
                        <div className='sidebar-wrapper'>
                            SIDEBAR
                        </div>
                    </div>
                    <div className='span-divider'></div>
                </div>
            }
        </>
    )
}

export default Cart;