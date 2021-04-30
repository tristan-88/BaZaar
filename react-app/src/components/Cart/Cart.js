import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { loadProducts } from '../../store/product'
import SmallProductTile from '../SmallProductTile/SmallProductTile'
import './Cart.css'


function Cart() {
    const dispatch = useDispatch()

    const cartProducts = useSelector(state => state.cart.products)
    const products = useSelector(state => state.products.products)

    //look at when ever something here changes reload this component
    useEffect(() => {
        dispatch(loadProducts())

    }, [dispatch])


    return (
        <>
            {products.length &&
                <div>
                    <div className="cart-card">
                        <h1>{`CART(${products.length})`}</h1>
                    </div>
                    <div>
                        {products.map(product => (
                            <SmallProductTile product={product} />
                        ))}
                    </div>
                </div>
            }
        </>
    )
}

export default Cart;