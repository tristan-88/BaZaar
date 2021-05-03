import React, { useEffect} from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, useParams, useHistory } from 'react-router-dom'
import "./ReviewTile.css"


function ReviewTile ({product}){

    return (
        <div className="review-body">
            {product.reviews.length && product.reviews.map((review) => (
            <div className='single-review'>
              <div className="user_created">
                <div className="user-name">{review.user_name}</div>
                <div className="created_at">{review.created_at}</div>
              </div>
              <div>
                {review.content}
              </div>
            </div>
          ))}
        </div>
    )

}

export default ReviewTile
