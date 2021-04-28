import React from 'react';
import { NavLink } from 'react-router-dom'

export const FeatureProductTile = (product) => {

  const product_synopsis = product.description.split('. ').slice(0, 2).join('. ')

  return (
    <>
      <div className='fpt-wrapper'>
        <div>
          <NavLink to={`/products/${product.id}`}>
            <img src={product.photos[0].photo_url} className='fpt-main-img'></img>
          </NavLink>
        </div>
        <div>
          {product.photos.map(photo => (
            <img src={photo.photo_url} key={photo.id} className="fpt-small-img"></img>
          ))}
        </div>
        <div>
          {product_synopsis}
        </div>
        <div>
          {product.price}
        </div>
      </div>
    </>
  )
}