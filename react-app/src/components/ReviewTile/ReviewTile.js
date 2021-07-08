import React, { useEffect} from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, useParams, useHistory } from 'react-router-dom'
import "./ReviewTile.css"


function ReviewTile ({review}){

    return (
      // <div className="review-body">
      // {product.reviews.length && product.reviews.map((review) => (

      //     <div className='single-review'  key={review.id}>
      //       <div className="user_created">
      //         <div className="user-name">{review.user_name }</div>
      //         <div className="created_at">{review.created_at}</div>
      //     </div>
      //       <div className="review-content">
      //       {review.content}
      //       </div>
      //     </div>
      //   ))}
      // </div>

      <div className="review-body">
        {
          <div className="single-review" key={review.id}>
            <div className="user_created">
              <div className="user-name">{review.user_name}</div>
              <div className="created_at">{review.created_at}</div>
            </div>
            <div className="review-content">
              {review.content.replace(/[\])}[{(]/g, "")}
            </div>
          </div>
        }
      </div>
    );

}

export default ReviewTile
