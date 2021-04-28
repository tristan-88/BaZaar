//TAGS are a component
// seasonal items are a component
// products are a component
import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { loadProducts } from '../store/product';


function HomePage() {
    const dispatch = useDispatch()
    useEffect(() => {
        dispatch(loadProducts())
    }, [dispatch])

    const products = useSelector(state => state.product)
    return (
        <>
            <h1>You are in the home page component</h1>
        </>
    )
}


export default HomePage;
