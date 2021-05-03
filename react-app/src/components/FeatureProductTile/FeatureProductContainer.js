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
      {topProducts &&
        topProducts.map(product => (
          <FeatureProductTile product={product} key={product.id} />
        ))
      }
    </>
  )
}

export default FeatureProductContainer;
