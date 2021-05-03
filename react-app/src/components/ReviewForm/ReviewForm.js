import React, { useState } from 'react';
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from "react-router-dom";
import { postingReview, editingReview, deletingReview} from '../../store/review'
import './ReviewForm.css'

const ReviewForm = () => {
	const dispatch = useDispatch()
	const product = useSelector(state => state.products.products)
    const [content, setContent] = useState('');
	const productId = product[0].id
	const creatReview = async (e) => {
		e.preventDefault();
		await dispatch(postingReview({ content, productId }))
    }

    return (
			<>
				<form onSubmit={creatReview}>
					<div>
						<label>Content</label>
						<input
							type="text"
							onChange={(e) => {
								setContent(e.target.value);
							}}
							value={content}
						></input>
						<button type="submit">submit</button>
					</div>
				</form>
			</>
		);
}

export default ReviewForm