//TAGS are a component
// seasonal items are a component
// products are a component
import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { loadProducts } from '../../store/product';
import ProductCard from '../ProductCard/ProductCard'
import FeatureProductContainer from '../FeatureProductTile/FeatureProductContainer'
import './HomePage.css'
import ProductForm from '../ProductForm/ProductForm';

function HomePage() {
    const dispatch = useDispatch()
	const products = useSelector(state => state.product.products)
	const user = useSelector(state => state.session.user)

	useEffect(() => {
		if (user) {

		}
        dispatch(loadProducts())
    }, [dispatch])

	console.log(user)
    if (!products) {
        return null
    }

	let sessionLinks;
	if (user) {
	  sessionLinks = (
		<ProductForm />
	  )
	  } else {
		sessionLinks = (
		  <>
		  </>
	  )
	}

    return (
			<>
				{sessionLinks}
				<div className="banner-div">
					<img
						src="https://api.genstore.info/photos/banner-shopping.jpg"
						alt="👽"
						className="banner-img"
					/>
				</div>
				<div className="fpt-container">
					{products["0"] && <FeatureProductContainer products={products} />}
				</div>
				<div className="tags-div">
					<h1>TAGS AND CATEGORIES WILL BE HERE</h1>
				</div>
				<ProductCard />
			</>
		);
}


export default HomePage;
