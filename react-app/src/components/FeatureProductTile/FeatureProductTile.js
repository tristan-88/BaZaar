import React from 'react';
import { NavLink } from 'react-router-dom'
import './FeatureProductTile.css'

const FeatureProductTile = ({ product }) => {

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
              <p>Feature Product</p>
              <img src={product.photos[0]?.photo_url} className='fpt-main-img' alt='nope'></img>
            </NavLink>
          </div>
          <div className='small-img-div'>
            {product.photos.map(photo => (
              <img src={photo.photo_url} key={photo.id} className="fpt-small-img" alt='nope'></img>
            )).slice(0, 4)}
        </div>
        {/* <div className="synopsis">{`Synopsis: ${product_synopsis}`}</div> */}
        <div>{`Product: ${product.name}`}</div>
        <div><NavLink to={`/products/${product.id}`}>
            {`$${product.price}`}
          </NavLink></div>
        </div>
      }

      
    </>
  )
}

export default FeatureProductTile;