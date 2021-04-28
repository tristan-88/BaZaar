const SET_PRODUCTS = 'product/SET_PRODUCTS'
const REMOVE_PRODUCTS = 'product/REMOVE_PRODUCTS'


//Actions
const setProducts = (products) => ({
    type: SET_PRODUCTS,
    payload: products
})

const clearProducts = () => ({
    type: REMOVE_PRODUCTS
})


//Thunks
export const loadProducts = () => async (dispatch) => {
    const response = await fetch('/api/products')
    const data = await response.json();
    if (data.errors) {
        return data
    }
    dispatch(setProducts(data))
}

export const removeProducts = () => async (dispatch) => {
    dispatch(clearProducts())
}

const initialState = {}

export default function cartReducer(state = initialState, action) {
    switch (action.type) {
        case SET_PRODUCTS:
            return { ...action.payload }
        case REMOVE_PRODUCTS:
            return {};
        default:
            return state
    }
}
