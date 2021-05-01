import React from "react";
import { useDispatch, useSelector } from "react-redux";
import "./Store.css"
import SmallProductTile from "../SmallProductTile/SmallProductTile";
import FeatureProductTile from "../FeatureProductTile/FeatureProductTile";

const Store = () => {
	const dispatch = useDispatch()
    const store = useSelector(state => state.store)


    return (
			<>
				{store &&
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
							<h2>Store Name: {store.name}</h2>
							<h3>Store Description:</h3> {store.description}
						</div>
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
							)).slice(0,1)}
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
				}
			</>
		);

}

export default Store
