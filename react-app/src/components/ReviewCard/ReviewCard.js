import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link, NavLink } from "react-router-dom"

function ReviewCard({product}) {
    return (
        <>
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
    </>
    );
}

export default ReviewCard;
