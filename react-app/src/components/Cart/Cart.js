import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { loadProducts } from '../../store/product'
import SmallProductTile from '../SmallProductTile/SmallProductTile'
import './Cart.css'


function Cart() {
    const dispatch = useDispatch()

    const cartProducts = useSelector(state => state.cart.products)
        .map(product => product.id)
    const products = useSelector(state => state.products.products)

    //look at when ever something here changes reload this component
    useEffect(() => {
        dispatch(loadProducts())
        console.log(cartProducts)
    }, [dispatch])

    let myCart;
    if (products) {
        myCart = products.map(product => (cartProducts.includes(product.id) ? product : ''))
            .filter(product => product !== "")
    }

    return (
        <>
            {myCart.length &&
                <div>
                    <div className="cart-card">
                        <h1>{`CART(${myCart.length})`}</h1>
                    </div>
                    <div>
                        {myCart.map(product => (
                            <SmallProductTile product={product} />
                        ))}
                    </div>
                </div>
            }
        </>
    )
}

export default Cart;