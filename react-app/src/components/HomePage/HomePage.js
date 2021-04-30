//TAGS are a component
// seasonal items are a component
// products are a component
import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { loadFeatureProducts, loadProducts } from '../../store/product';
import ProductCardContainer from '../ProductCardContainer/ProductCardContainer'
import FeatureProductContainer from '../FeatureProductTile/FeatureProductContainer'
import './HomePage.css'
import ProductForm from '../ProductForm/ProductForm';

function HomePage() {
	const dispatch = useDispatch()

	const [loaded, setLoaded] = useState(false)

	useEffect(() => {
		dispatch(loadProducts())
		setLoaded(true)
	}, [dispatch, setLoaded])

	const products = useSelector(state => state.products)

	if (!products) {
		return null
	}

	const setFilter = (id) => {
		console.log(id)
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
			<ProductCardContainer />
		</>
	);
}


export default HomePage;
