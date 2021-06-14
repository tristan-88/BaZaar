import React from 'react'
import { NavLink } from 'react-router-dom';
import "./SmallProductTile.css"


function SmallProductTile({ product }) {
	return (
		<div className="product-card" key={`${product.id}`}>
			<NavLink to={`/products/${product.id}`}>
				<img src={product.photos[0]?.photo_url} alt={"default photo"} className="product-img" />
				<div>
					<div>{`$${product.price.toFixed(2)}`}</div>
					<div>{`Qty: ${product.quantity}`}</div>
				</div>
			</NavLink>
		</div>
	);
}

export default SmallProductTile
