import React from 'react'
import { NavLink, useParams } from 'react-router-dom'
import { useDispatch } from 'react-redux'


const SingleProductPage = () => {

  dispatch = useDispatch()
  const { id } = useParams()

  const product = useSelector(state => state.product[`${id - 1}`])

  return (
    <>
      <div className='product-page-wrapper'>
        <div className='photo-galery'>
          <div>
            <img src={product.photos.photo_url[0]} className="main-photo" alt="nope"></img>
          </div>
          <div>
            {product.photos.map((photo, i) => (
              <img src={photo.photo_url} alt="nah" key={i}></img>
            ))}
          </div>
        </div>
        <div className='product-description'>
          {<p>{product.description}</p>}
        </div>
        <br></br>
        <div>STORE DIV</div>
        <br></br>
        <div className='reviews-container'>
          {product.revews.map((review, i) => (
            <div className='single-review'>
              <div>
                <span>{review.user_id}</span>
                <span>{review.created_at}</span>
              </div>
            </div>
          ))}
        </div>
      </div >
    </>
  )

}

export default SingleProductPage;