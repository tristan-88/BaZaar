import React from 'react'
import { NavLink } from 'react-router-dom';
import "./SmallProductTile.css"


function SmallProductTile({ product }) {
    return (
			<div className="product-card" key={`${product.id}`}>
				<NavLink to={`/products/${product.id}`}>
					<img src={product.photos[0]?.photo_url} alt={"default photo"} className={productImg} />
					<div>{`$${product.price}0`}</div>
				</NavLink>
			</div>
		);
}

export default SmallProductTile
