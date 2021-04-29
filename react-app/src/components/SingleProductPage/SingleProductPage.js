import React from 'react'
import { useSelector } from 'react-redux'
import { NavLink, useParams } from 'react-router-dom'
import './SingleProductPage.css'
// import { useDispatch } from 'react-redux'


const SingleProductPage = () => {

  // const dispatch = useDispatch()

  const { id } = useParams()
  const p_id = parseInt(id)
  const product = useSelector(state => state.product[p_id - 1])

  if (product) {
    const url_list = product.photos.map(photo => photo.photo_url)



    return (
      <>

        { url_list.length && (
          <div className='product-page-wrapper'>
            <div className='photo-galery'>
              <div>
                <img src={url_list[0]} className="main-photo" alt="nope"></img>
              </div>
              <div>
                {url_list.map(url => (
                  <img src={url} className='small-img'></img>
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
              {product.reviews.length && product.revews.map((review, i) => (
                <div className='single-review'>
                  <div>
                    <span>{review.user_name}</span>
                    <span>{review.created_at}</span>
                  </div>
                  <div>
                    {review.content}
                  </div>
                </div>
              ))}
            </div>
          </div >
        )}
      </>
    )
  }

  return null

}

export default SingleProductPage;