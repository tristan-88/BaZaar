import React, { useEffect} from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, useParams, useHistory } from 'react-router-dom'
import { loadSingleProduct } from '../../store/product'
import Footer from '../Footer/Footer'
import { addToCart } from '../../store/cart'
import ReviewCard from '../ReviewCard/ReviewCard'
import './SingleProductPage.css'
// import ReviewForm from '../ReviewForm/ReviewForm'
// import { useDispatch } from 'react-redux'


const SingleProductPage = () => {
  const history = useHistory()
  const dispatch = useDispatch()
  let buttonText = 'Add to Cart'
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
    if (cart?.id) {
      let btn = window.document.getElementById('add-btn')
      btn.innerText = "Thank you!"
      dispatch(addToCart(cart.id, product_id))
      return history.push('/cart')

    }
    return history.push('/login')
  }

  return (
    <>
      {product.name &&
        (
        <div className='product-page-wrapper'>
          <div className="picture_desc">
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
              <h2>{product.name}</h2>
              {<p>{product.description}</p>}
              <div className="button-add-cart">
              <button id='add-btn' onClick={addOneToCart}>{buttonText}</button>
            </div>
            </div>
          </div>

          <div className='store-div'>
            <h1>STORE DIV</h1>
            </div>
          <div className='reviews-container'>
            <h2>REVIEWS</h2>
                  <ReviewCard product={product}/>
            </div>
            <Footer/>
          </div >
        )}
    </>
  )

}

export default SingleProductPage;
