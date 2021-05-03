import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link, NavLink } from "react-router-dom"
import './ReviewCard.css'
import ReviewForm from "../ReviewForm/ReviewForm";
import EditForm from "../ReviewForm/EditForm";

function ReviewCard({ review, user }) {
  const [isShown, setShown] = useState(false);

	useEffect(() => {
		if (!isShown) return;

		const closeShown = () => {
			setShown(false);
		};

		// document.addEventListener("click", closeShown);
		// return () => document.removeEventListener("click", closeShown)
	}, [isShown]);

	const handleSubmit = () => {
		setShown(true);
	};

	return (
		<>
			{
				<div className="single-review">
					{/* <div className="user_created"> */}
					<div className="top">
						<p className="name">{review.username}</p>
						{review.created_at}
					</div>
					{/* </div> */}
					<div className="content">
						<p>{review.content}</p>
          </div>
          <button onClick={handleSubmit}>EDIT REVIEW</button>
          {isShown && review.user_id === user.id ? (
						<EditForm reviewId={review.id} />
					) : null}
				
				</div>
			}
		</>
	);
}

export default ReviewCard;
