import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import './Cart.css'
import SmallProductTile from '../SmallProductTile/SmallProductTile'


function Cart() {
    const dispatch = useDispatch()
    //got the state
    const cartProducts = useSelector(state => state.cart?.products)
    const  [products, setProducts] = useState([])
    //look at when ever something here changes reload this component
    useEffect(() => {
     setProducts(cartProducts)
    }, [cartProducts.length, setProducts])


    return (
        <>
            {products.length &&
            <div>
                <div className="cart-card">
                    <h1>{`CART(${products.length})`}</h1>
                </div>
                <div>
                {products.map(product=>(
                    <SmallProductTile product={product}/>
                ))}
                </div>
            </div>
            }
        </>
    )
}

export default Cart;