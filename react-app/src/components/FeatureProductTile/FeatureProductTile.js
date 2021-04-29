import React from 'react';
import { NavLink } from 'react-router-dom'
import './FeatureProductTile.css'

const FeatureProductTile = ({ product }) => {
  // console.log(product, 'in the tile')

  let product_synopsis;

  if (product) {
    product_synopsis = product.description.split('. ').slice(0, 2).join('. ')
  }

  return (
    <>
      { product &&
        <div className='fpt-wrapper'>
          <div>
            <NavLink to={`/products/${product.id}`}>
              {product.name}
              <img src={product.photos[0]?.photo_url} className='fpt-main-img' alt='nope'></img>
            </NavLink>
          </div>
          <div className='small-img-div'>
            {product.photos.map(photo => (
              <img src={photo.photo_url} key={photo.id} className="fpt-small-img" alt='nope'></img>
            ))}
          </div>
          <div>
            {product_synopsis}
          </div>
          {product.name}
          <NavLink to={`/products/${product.id}`}>
            {product.price}
          </NavLink>
        </div>
      }
    </>
  )
}

export default FeatureProductTile;