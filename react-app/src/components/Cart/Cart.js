import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { loadProducts } from '../../store/product'
import { createCart } from '../../store/cart'
import CartProductTile from '../CartProductTile/CartProductTile'
import './Cart.css'


function Cart() {
    const dispatch = useDispatch()

    const cartProducts = useSelector(state => state.cart?.products)
    const products = useSelector(state => state.products?.products)

    //look at when ever something here changes reload this component
    useEffect(() => {
        dispatch(loadProducts())
        dispatch(createCart())
    }, [dispatch])


    // if (!cartProducts) return null
    let myCart;
    if (products.length && cartProducts.length) {
        myCart = products.map(product => (cartProducts.includes(product.id) ? product : ''))
            .filter(product => product !== '')
        console.log(myCart)
    }


    return (
        <>
            {cartProducts &&
                <div>
                    <div className="cart-card">
                        <h1>{`CART(${myCart.length})`}</h1>
                    </div>
                    <div>
                        {myCart.map(product => (
                            <CartProductTile product={product} />
                        ))}
                    </div>
                </div>
            }
        </>
    )
}

export default Cart;