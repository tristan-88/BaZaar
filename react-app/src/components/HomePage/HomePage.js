//TAGS are a component
// seasonal items are a component
// products are a component
import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { createCart } from '../../store/cart'
import { getStore } from '../../store/store'
import { loadFeatureProducts, loadProducts, loadFilteredProducts } from '../../store/product';
import SmallProductTile from '../SmallProductTile/SmallProductTile'
import ProductCardContainer from '../ProductCardContainer/ProductCardContainer'
import FeatureProductContainer from '../FeatureProductTile/FeatureProductContainer'
import FilteredProductsContainer from '../FilteredProductsContainer/FilteredProductsContainer'
import './HomePage.css'


function HomePage() {
	const dispatch = useDispatch()
	// allows access to the redux store
	const user = useSelector(state => state.session.user)
	// sets user to equal the {session {user}}
	const [loaded, setLoaded] = useState(false)

	useEffect(() => {
		if (user) { // if a user exists do these things
			dispatch(getStore()) // load the store
			dispatch(loadProducts()) // load all products
			dispatch(createCart()) // load a cart
			setLoaded(true) // load the state
		} else {
			dispatch(loadProducts()) // load products
			setLoaded(true) // load the state
		}
	}, [dispatch, setLoaded])

	const products = useSelector(state => state.products) // set products to equal the products value in the state
	const filteredProducts = useSelector(state => state.products.filteredProducts) // set filtered products to equal the filtered products slice
	if (!products) {
		return null //guard clause if the product does not exsist
	}

	const setFilter = async (tagId) => { //
		await dispatch(loadFilteredProducts(Number(tagId)))
	} // load the filter dispatch by passing in the id on line 58-68
	return (
		<>
			<div className="banner-div">
				<img
					src="https://github.com/tristan-88/BaZaar/blob/main/react-app/public/images/banner.png?raw=true"
					alt="👽"
					className="banner-img"
				/>
			</div>
			<div className='fpt-container'>
				<FeatureProductContainer />
			</div>
			<div className="tags-div">
				<div onClick={(e) => setFilter(e.target.id)} id='1' className='sports-tag-div'>Sports</div>
				<div onClick={(e) => setFilter(e.target.id)} id='2' className='gardening-tag-div'>Home & Gardening</div>
				<div onClick={(e) => setFilter(e.target.id)} id='3' className='jewelry-tag-div'>Jewelry</div>
				<div onClick={(e) => setFilter(e.target.id)} id='4' className='clothing-tag-div'>Clothing</div>
				<div onClick={(e) => setFilter(e.target.id)} id='5' className='kitchen-tag-div'>Kitchen</div>
				<div onClick={(e) => setFilter(e.target.id)} id='6' className='collectibles-tag-div'>Collectibles</div>
				<div onClick={(e) => setFilter(e.target.id)} id='7' className='craft-tag-div'>Arts & Crafts</div>
				<div onClick={(e) => setFilter(e.target.id)} id='8' className='decor-tag-div'>Home Decor</div>
				<div onClick={(e) => setFilter(e.target.id)} id='9' className='art-tag-div'>Art</div>
				<div onClick={(e) => setFilter(e.target.id)} id='10' className='misc-tag-div'>Misc</div>
				<div onClick={(e) => setFilter(e.target.id)} id='11' className='home-tag-div'>Home & Living</div>
			</div>
			<div className="filtered-container">
				{filteredProducts && filteredProducts.map(product => <SmallProductTile product={product} />)}
			</div>
			<div>
			</div>
			<div className='filtered-products-wrapper'>
				<FilteredProductsContainer products={products} />
			</div>
			<ProductCardContainer />
		</>
	);
}


export default HomePage;
