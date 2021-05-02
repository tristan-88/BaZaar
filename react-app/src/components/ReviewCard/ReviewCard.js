import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link, NavLink } from "react-router-dom"
import './ReviewCard.css'

function ReviewCard({product}) {
    return (
        <>
        {product.reviews.length && product.reviews.map((review) => (
          <div className='single-review'>
            {/* <div className="user_created"> */}
              <div className="top">
                <p className="name">{review.username}</p>{review.created_at} 
              </div>
              {/* </div> */}
              <div className="content">
                <p>{review.content}</p>
              </div>
            </div>
          ))}
    </>
    );
}

export default ReviewCard;
