import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, useParams, Redirect } from 'react-router-dom'
import { loadSingleProduct } from '../../store/product'
import { addToCart } from '../../store/cart'
import './SingleProductPage.css'
// import { useDispatch } from 'react-redux'


const SingleProductPage = () => {
  const dispatch = useDispatch()
  let buttonText = 'Add to Cart!'
  const { id } = useParams()
  const product_id = parseInt(id)
  let cart = useSelector(state => state.cart)
  let product = useSelector(state => state.products.products)

  useEffect(() => {
    dispatch(loadSingleProduct(product_id))
  }, [dispatch, product.length])

  if (product.length) {
    product = product[0]
  }

  const addOneToCart = () => {
    console.log('click!')
    if (cart?.id) {
      console.log('GO TO CART')
      let btn = window.document.getElementById('add-btn')
      btn.innerText = "Thank you!"
      console.log(btn)
      dispatch(addToCart(cart.id, product_id))
      return <Link to='/cart' />
    }

    console.log('GO TO LOGIN')
    return <Link to='/login/' />
  }

  return (
    <>
      {product.name &&
        (
          <div className='product-page-wrapper'>
            <div className='photo-gallery'>
              <div>
                <img src={product.photos[0].photo_url} className="main-img" alt="nope"></img>
              </div>
              <div>
                {product.photos.map(photo => (
                  <img src={photo.photo_url} className='small-img'></img>
                ))}
              </div>
            </div>
            <div className='product-description'>
              {<p>{product.description}</p>}
            </div>
            <div>
              <button id='add-btn' onClick={addOneToCart}>{buttonText}</button>
            </div>
            <div className='store-div'>STORE DIV</div>
            <div className='reviews-container'>
              {product.reviews.length && product.reviews.map((review, i) => (
                <div className='single-review'>
                  <div>
                    <span key={i}>{review.user_name}</span>
                    <span key={i + 1}>{review.created_at}</span>
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

export default SingleProductPage;