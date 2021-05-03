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
		<div className="form-body">
			<div className="form-container">
                <form onSubmit={editReview}>
                    <div className="form-inputs">
					<label>Edit Review: </label>
					<input
						type="text"
						onChange={(e) => {
							setContent(e.target.value);
						}}
						value={content}
                        ></input>
                    </div>
                    <div class="button-div"><button type="submit">submit</button>
                    </div>
					
				</form>
				<div class="button-div"><button onClick={() => deleteReview(reviewId)}>Delete</button></div>
				
			</div>
		</div>
	);
};

export default EditForm;
