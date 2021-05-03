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
	const user = useSelector(state => state.session.user)
	const [loaded, setLoaded] = useState(false)

	useEffect(() => {
		if (user) {
			dispatch(getStore())
			dispatch(loadProducts())
			dispatch(createCart())
			setLoaded(true)
		} else {
			dispatch(loadProducts())
			dispatch(createCart())
			setLoaded(true)
		}
	}, [dispatch, setLoaded])

	const products = useSelector(state => state.products)
	const filteredProducts = useSelector(state => state.products.filteredProducts)
	if (!products) {
		return null
	}

	const setFilter = async (tagId) => {
		await dispatch(loadFilteredProducts(Number(tagId)))
	}

	return (
		<>
			<div className="banner-div">
				<img
					src="https://github.com/Drewthurm21/portfolio/blob/main/images/homepage-banner.jpeg?raw=true"
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
			<div classname='filtered-products-wrapper'>
				<FilteredProductsContainer products={products} />
			</div>
			<ProductCardContainer />
		</>
	);
}


export default HomePage;
