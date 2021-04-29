import React from 'react';
import { NavLink } from 'react-router-dom'
import { useSelector } from 'react-redux'
import { loadProducts } from '../../store/product';
import FeatureProductTile from './FeatureProductTile'
import './FeatureProductTile.css'

const FeatureProductContainer = ({ products }) => {

  let keys;

  if (products) {
    keys = Object.keys(products).slice(0, 3)
    console.log(keys)
  }

  return (
    <>
      {keys && (
        keys.map(key => (
          <FeatureProductTile product={products[key]} key={key} />
        )
        ))}
    </>
  )
}

export default FeatureProductContainer;