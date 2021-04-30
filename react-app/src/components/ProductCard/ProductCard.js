import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link, NavLink } from "react-router-dom"
import SmallProductTile from '../SmallProductTile/SmallProductTile.js'
import "./ProductCard.css"

function ProductCard() {
    // const dispatch = useDispatch()
    const products = useSelector(state => {
        return state.products.products
    })

    if (!products) return null

    return (
        //we may want to limit on the display
        <div className="product-card-container" >
            <div className="product-list">
                {products.map((product, i) => (
                    <SmallProductTile product={product} key={i} />
                ))}
            </div>


        </div>
    );

}

export default ProductCard;