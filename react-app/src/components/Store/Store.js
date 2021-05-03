import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import "./Store.css"
import SmallProductTile from "../SmallProductTile/SmallProductTile";
import FeatureProductTile from "../FeatureProductTile/FeatureProductTile";
import ProductForm from "../ProductForm/ProductForm"
import ShopForm from "../ShopForm/ShopForm"

const Store = () => {
	const user = useSelector(state => state.session.user)
	const store = useSelector(state => state.store)


	let sessionLinks;
	if (store) {
		sessionLinks = (
			<>
				<h2 className="shop-title">My Shop!</h2>
				<div className="border-line"></div>
				<h1>Add Product</h1>
				<ProductForm />
			</>
		)
	} else {
		sessionLinks = (
			<>
				<h1>Would you like to create a shop?</h1>
				<ShopForm />
			</>
		)
	}
	if (!store) return null

	return (
		<>
			{store &&
				<div>
					<div className="store-page">
						<div className="store-info">
							<div className="store-img">
								<img
									src={store.photo_url}
									alt={"PHOTO UNAVAILBLE..."}
									className="img-store"
								/>
							</div>
							<div className="store_name_description">
								<h2>{store.name}</h2>
								<h3>Description:</h3> {store.description}
							</div>
						</div>
						<div>
							{sessionLinks}
						</div>
						<div className="store-items">
							<div className='main-item'></div>
							{store.products
								.map((product) => (
									<div className="main-products">
										<FeatureProductTile
											className="feature-products-cards"
											product={product}
										/>
									</div>
								)).slice(0, 1)}
							<div className="other-item">
								{store.products
									.map((product) => (
										<div className="other-products">
											<SmallProductTile
												className="products-cards"
												product={product}
											/>
										</div>
									)).slice(1)}
							</div>
						</div>
					</div>
				</div>}
		</>
	);

}

export default Store
