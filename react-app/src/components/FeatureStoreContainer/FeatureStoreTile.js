import React from 'react';
import { NavLink } from 'react-router-dom'
import './FeatureStoreTile.css'

const FeatureStoreTile = ({ store }) => {

  let store_synopsis;

  if (Object.entries(store).length) {
    store_synopsis = store?.description.split('. ').slice(0, 2).join('. ')
  }

  return (
    <>
      { store &&
        <div className='fst-wrapper'>
          <div>
            <img src={store.photo_url} className='fst-main-img' alt='nope'></img>
          </div>
          <div>{`store: ${store.name}`}</div>
          <div>
            {`${store.description}`}
          </div>
        </div>
      }
    </>
  )
}

export default FeatureStoreTile;
