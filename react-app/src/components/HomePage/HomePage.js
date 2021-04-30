//TAGS are a component
// seasonal items are a component
// products are a component
import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { loadFeatureProducts, loadProducts } from '../../store/product';
import {gettingStore} from '../../store/store'
import {createCart} from '../../store/cart'
import ProductCard from '../ProductCard/ProductCard'
import FeatureProductContainer from '../FeatureProductTile/FeatureProductContainer'
import './HomePage.css'
import ProductForm from '../ProductForm/ProductForm';

function HomePage() {
	const dispatch = useDispatch()

	const [loaded, setLoaded] = useState(false)

	useEffect(() => {
		dispatch(gettingStore())
		dispatch(loadProducts())
		dispatch(createCart())
		setLoaded(true)
	}, [dispatch, setLoaded])

	const products = useSelector(state => state.products)

	if (!products) {
		return null
	}



	return (
		<>
			<div className="banner-div">
				<img
					src="https://api.genstore.info/photos/banner-shopping.jpg"
					alt="👽"
					className="banner-img"
				/>
			</div>
			<div className="fpt-container">
				{products && <FeatureProductContainer products={products} />}
			</div>
			<div className="tags-div">
				<h1>TAGS AND CATEGORIES WILL BE HERE</h1>
			</div>
			<ProductCard />
		</>
	);
}


export default HomePage;
