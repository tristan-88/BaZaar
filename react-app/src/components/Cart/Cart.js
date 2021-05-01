import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { createCart } from '../../store/cart'
import SmallProductTile from '../SmallProductTile/SmallProductTile'
import CartProductTile from '../CartProductTile/CartProductTile'
import './Cart.css'


function Cart() {
    const dispatch = useDispatch()

    const cart = useSelector(state => state.cart)

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
                    <div className="cart-card">
                        <h1>{`CART(${cart.products.length})`}</h1>
                    </div>
                    <div>
                        {cart.products.map(product => (
                            <CartProductTile product={product.product} />
                        ))}
                    </div>
                </div>
            }
        </>
    )
}

export default Cart;