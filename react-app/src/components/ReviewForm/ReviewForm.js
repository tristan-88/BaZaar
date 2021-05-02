import React, { useState } from 'react';
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from "react-router-dom";
import { postingReview } from '../../store/review'
import '/ReviewForm.css'

const ReviewForm = () => {
    const dispatch = useDispatch()
    const [content, setContent] = useState('');

    const creatReview = async (e) => {
        e.preventDefault();
        await dispatch(postingReview(content))
    }

    return (
        <>
            <form onSubmit={creatReview}>
                <div>
                    <label>Content</label>
                </div>

            </form>
            </>
    )
}

export default ReviewForm