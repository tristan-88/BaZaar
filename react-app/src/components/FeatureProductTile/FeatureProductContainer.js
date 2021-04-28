import React from 'react';
import { NavLink } from 'react-router-dom'
import { useSelector } from 'react-redux'
import { loadProducts } from '../../store/product';
import FeatureProductTile from './FeatureProductTile'
import './FeatureProductTile.css'

const FeatureProductContainer = ({ products }) => {

  return (
    <>
      {products["0"] &&
        <div className='fpt-container-div'>
          <FeatureProductTile product={products["0"]} />
          <FeatureProductTile product={products["1"]} />
          <FeatureProductTile product={products["33"]} />
        </div>
      }
    </>
  )
}

export default FeatureProductContainer;