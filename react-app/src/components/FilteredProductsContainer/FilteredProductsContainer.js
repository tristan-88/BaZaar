import React, { useState, useEffect } from 'react'
import { useSelector } from 'react-redux';
import { useParams, Link, NavLink } from "react-router-dom"
import SmallProductTile from '../SmallProductTile/SmallProductTile.js'
import ProductCardContainer from '../ProductCardContainer/ProductCardContainer'



const FilteredProductsContainer = ({ filteredProducts }) => {


    return (
        <>
            <div className="product-list">
                {filteredProducts?.map((product, i) => <SmallProductTile product={product} key={i} />)}
            </div>
        </>
    );

}

export default FilteredProductsContainer;
