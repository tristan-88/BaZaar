const GET_REVIEWS = 'session/GET_REVIEWS'
const GET_REVIEW = 'session/GET_REVIEW'
const POST_REVIEW = 'session/POST_REVIEW'
const DELETE_REVIEW = 'session/DELETE_REVIEW'
const EDIT_REVIEW = 'session/EDIT_REVIEW'

//actions
const getReviews = (reviews) => ({
    type: GET_REVIEWS,
        payload: reviews
})

const postReview = () => ({
    type: POST_REVIEW,
})

//THUNKS

export const gettingReview = () => async (dispatch) => {
    const response = await fetch(`/api/reviews`)
    const reviews = await response.json()
    if (reviews.errors) {
        return reviews
    }
    dispatch(getReviews(reviews))
}

export const postingReview = (content, user_id) => async (dispatch) => {
    const formData = new FormData();
    formData.append('content', content)

    const response = await fetch(`/api/reviews/${user_id}`, {
        method: 'POST',
        body: formData
    })

    if (response.ok) {
        const data = await response.json();
        dispatch(postReview(data))
    }
}

//Reducer

const initialState = {
    Reviews:[]
}

export default function reviewReducer(state = initialState, action) {
    switch (action.type) {
        case GET_REVIEWS:
            return { ...state, Reviews:[...action.payload] }
        default:
            return state
    }
}