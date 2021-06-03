import React, { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { loadFeatureProducts } from '../../store/product';
import FeatureProductTile from './FeatureProductTile'
import './FeatureProductTile.css'

const FeatureProductContainer = () => {

  const dispatch = useDispatch()

  const [topProducts, setTopProducts] = useState(null)

  useEffect(() => {
    dispatch(loadFeatureProducts())
  }, [dispatch])

  const featuredProducts = useSelector(state => state.products.featureProducts)

  useEffect(() => {
    if (featuredProducts.length) {
      setTopProducts(featuredProducts)
    }
  }, [featuredProducts, setTopProducts])

  return (
    <>
      <div className="feature-title">
        <h1>Featured Products</h1>
      </div>
      <div className="feature-product">
        {topProducts &&

          topProducts.map(product => (
            <FeatureProductTile product={product} key={product.id} />
          )).slice(0, 4)

        }
      </div>
    </>

  )
}

export default FeatureProductContainer;
