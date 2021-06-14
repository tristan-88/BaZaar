import React from 'react';
import { NavLink } from 'react-router-dom'
import './FeatureProductTile.css'

const FeatureProductTile = ({ product }) => {

  let product_synopsis;

  if (Object.entries(product).length) {
    product_synopsis = product?.description.split('. ').slice(0, 2).join('. ')
  }
  const productDescription = product.name.slice(0, 25) + '...'

  return (
    <>
      { product &&
        <>
          <div className='fpt-wrapper'>
            <NavLink className="main-img-wrapper" to={`/products/${product.id}`}>
              <div className="fpt-main-img-container">
                <img src={product.photos[0]?.photo_url} className='fpt-main-img' alt='nope'></img>
              </div>
            </NavLink>
            <div className='small-img-div'>
              {product.photos.map(photo => (
                <img src={photo.photo_url} key={photo.id} className="fpt-small-img" alt='nope'></img>
              )).slice(0, 4)}
            </div>
            {/* <div className="synopsis">{`Synopsis: ${product_synopsis}`}</div> */}
            <div>{`${productDescription}`}</div>
            <div><NavLink to={`/products/${product.id}`}>
              {`$${product.price.toFixed(2)}`}
            </NavLink></div>
          </div>
        </>

      }


    </>
  )
}

export default FeatureProductTile;
