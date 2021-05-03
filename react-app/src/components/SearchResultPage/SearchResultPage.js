import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import SmallProductTile from '../SmallProductTile/SmallProductTile'
import CartProductTile from '../CartProductTile/CartProductTile'
import './SearchResultPage.css'

const SearchResultPage = () => {

  const product_results = useSelector(state => state.search.products)
  const store_results = useSelector(state => state.search.stores)

  return (
    <>
      {
        <div>
          <div className='products-div'>
            {product_results.map(product => (
              <SmallProductTile product={product} />))
            }
          </div>
        </div>
      }
    </>
  )
}

export default SearchResultPage;