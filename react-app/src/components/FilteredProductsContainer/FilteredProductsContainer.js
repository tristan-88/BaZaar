import React, { useState, useEffect } from 'react'
import { useSelector } from 'react-redux';
import { useParams, Link, NavLink } from "react-router-dom"
import SmallProductTile from '../SmallProductTile/SmallProductTile.js'
import ProductCardContainer from '../ProductCardContainer/ProductCardContainer'



const FilteredProductsContainer = ({ filteredProducts }) => {

    // const [category, setCategory] = useState(2)

    // const setFilter = (tagId) => {
    //     setCategory(tagId)
    //     filteredProducts = products.products.filter(product => (product.tag.includes(Number(category))))
    //     console.log(filteredProducts)
    // }

    // useEffect(() => {    
    // }, [category])

    // if (!products) return null

    return (
        <>
            <div className="product-list">
                {/* <p>{category}</p> */}
                {/* {products.products && <SmallProductTile product={products.products[0]} />} */}
                {filteredProducts?.map((product, i) => <SmallProductTile product={product} key={i} />)}
            </div>
        </>
    );

}

export default FilteredProductsContainer;
