import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link, NavLink } from "react-router-dom"
import SmallProductTile from '../SmallProductTile/SmallProductTile.js'
import "./ProductCardContainer.css"

function ProductCardContainer() {
    // const dispatch = useDispatch()
    const products = useSelector(state => {
        return state.products.products
    })

    if (!products) return null

    return (
        //we may want to limit on the display
        <div className="product-card-container" >
            <div className="product-list">
                {products.slice(0, 10).map((product, i) => (
                    <SmallProductTile product={product} key={i} />
                ))}
            </div>
            <br></br>
            <h1>next 10</h1>
            <div className="product-list">
                {products.slice(10, 20).map((product, i) => (
                    <SmallProductTile product={product} key={i} />
                ))}
            </div>

        </div>
    );

}

export default ProductCardContainer;
