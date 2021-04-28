const SET_CART = 'cart/SET_CART'
const REMOVE_CART = 'cart/REMOVE_USER'

//Actions
const setCart = (cart) => ({
    type: SET_CART,
    payload: cart
})

const deleteCart = () => ({
    type: REMOVE_CART
})


//Thunks
export const createCart = () => async (dispatch) => {
    const response = await fetch('/api/carts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    const data = await response.json();
    if (data.errors) {
        return data
    }
    dispatch(setCart(data))
}

export const removeCart = () => async (dispatch) => {
    dispatch(deleteCart())
}

const initialState = {}

export default function cartReducer(state = initialState, action) {
    switch (action.type) {
        case SET_CART:
            return { ...action.payload }
        case REMOVE_CART:
            return {};
        default:
            return state
    }
}
