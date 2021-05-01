import React, { useState, useEffect } from 'react'
import { useSelector } from 'react-redux';
import { useParams, Link, NavLink } from "react-router-dom"
import SmallProductTile from '../SmallProductTile/SmallProductTile.js'
import "./ProductCardContainer.css"

function FilteredProductsContainer({ productList }) {

    const [products, setProducts] = useState(null)

    useEffect(() => {

    }, [productList])


    if (!products) return null

    return (
        //we may want to limit on the display
        <div className="product-card-container" >
            <div className="product-list">
                {products.filter((product, i) => (
                    <SmallProductTile product={product} key={i} />
                ))}
            </div>
        </div>
    );

}

export default ProductCardContainer;
