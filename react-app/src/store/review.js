import { loadSingleProduct } from './product'



export const postingReview = ({ content, productId }) => async (dispatch) => {
	const response = await fetch(`/api/reviews/`, {
		headers: { "Content-Type": 'application/json' }, //find right headers
		body: JSON.stringify({      //changes content to JSON to be able to passed around
			productId,
			content
		}),
		method: "POST"
	})
	if (response.ok) {
		const data = await response.json();
		await dispatch(loadSingleProduct(data.product_id))
	}
}

export const editingReview = ({ content, reviewId }) => async (dispatch) => {
	const response = await fetch(`/api/reviews/`, {
		headers: { "Content-Type": "application/json" }, //find right headers
		body: JSON.stringify({
			//changes content to JSON to be able to passed around
			reviewId, //camelcase matches in the routes that is corresponding to this one
			content,
		}),
		method: "PATCH",
	});
	if (response.ok) {
		const data = await response.json();
		await dispatch(loadSingleProduct(data.product_id));
	}
};

export const deletingReview = (reviewId) => async (dispatch) => {
	const response = await fetch(`/api/reviews/`, {
		headers: { "Content-Type": "application/json" }, //find right headers
		body: JSON.stringify({
			//changes content to JSON to be able to passed around
			reviewId, //if deleting only need the reference id
		}),
		method: "DELETE",
	});
	if (response.ok) {
		const data = await response.json();
		await dispatch(loadSingleProduct(data.product_id)); //make sure you passing product_id  since the thunk expecting product id make sure the thunks and route is getting the same information 
	}
};

//Reducer

// const initialState = {}

// export default function reviewReducer(state = initialState, action) {
//     switch (action.type) {
//         case POST_REVIEW:
//             return { ...state, Reviews:[...action.payload] }
//         default:
//             return state
//     }
// }