import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import SmallProductTile from '../SmallProductTile/SmallProductTile'

const SearchResultPage = () => {

  const search_results = useSelector(state => state.search)

  let store_results;
  let product_results = []
  useEffect(() => {
    if (search_results) {
      product_results = search_results.products
      store_results = search_results.stores
      console.log('*PRODUCT RESULTS*', product_results)
      console.log('*STORE RESULTS*', store_results)
    }
  }, [search_results])

  // if (!search_results.length) {
  //   return null
  // }

  return (
    <>
      <div>sup</div>
      {search_results.length && (
        <div>
          {product_results.map(product => (
            <SmallProductTile product={product} />))
          }
        </div>
      )}
    </>
  )


}

export default SearchResultPage;