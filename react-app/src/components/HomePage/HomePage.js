//TAGS are a component
// seasonal items are a component
// products are a component
import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { loadProducts } from '../../store/product';
import ProductCard from '../ProductCard/ProductCard'
import FeatureProductContainer from '../FeatureProductTile/FeatureProductContainer'
import './HomePage.css'

function HomePage() {
    const dispatch = useDispatch()
    useEffect(() => {
        dispatch(loadProducts())
    }, [dispatch])

    const products = useSelector(state => state.product)

    if (!products) {
        return null
    }

    return (
        <>
            <h1>You are in the home page component</h1>
            <div className='fpt-container'>
                {products["0"] && <FeatureProductContainer products={products} />}
            </div>
            <ProductCard />
        </>
    )
}


export default HomePage;
