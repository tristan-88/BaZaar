import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import {
	postingReview,
	editingReview,
	deletingReview,
} from "../../store/review";
import "./ReviewForm.css";

const EditForm = ({reviewId}) => {
	const dispatch = useDispatch();
	const [content, setContent] = useState("");

    const editReview = async (e) => {
        console.log(reviewId)
		e.preventDefault();
        await dispatch(editingReview({ content, reviewId }));
    };
    
    const deleteReview = async (reviewId) => {
        await dispatch(deletingReview(reviewId))
    }

	return (
        <>
                <form onSubmit={editReview}>
                    <label>Edit Review: </label>
                    <input type="text" onChange={(e) => {
                        setContent(e.target.value);
                    }} value={content}></input>
                    <button type="submit">
                    submit
                    </button>
                    
                </form>
                <button onClick={() => deleteReview(reviewId)}>Delete</button>
		</>
	);
};

export default EditForm;
