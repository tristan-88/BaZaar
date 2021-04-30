const SET_PRODUCTS = 'product/SET_PRODUCTS'
const REMOVE_PRODUCTS = 'product/REMOVE_PRODUCTS'
const FEATURE_PRODUCTS = 'product/FEATURE_PRODUCTS'


//Actions
const setProducts = (products) => ({
    type: SET_PRODUCTS,
    payload: products
})

const clearProducts = () => ({
    type: REMOVE_PRODUCTS
})


const featureProducts = (products) => ({
    type: FEATURE_PRODUCTS,
    payload: products
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

export const loadSingleProduct = (id) => async (dispatch) => {
    const res = await fetch(`/api/products/${id}`)
    const product = await res.json()
    if (res.ok) {
        dispatch(setProducts([product]))
    }
}

export const loadFeatureProducts = () => async (dispatch) => {
    const res = await fetch('/api/products/top5')
    const data = await res.json()

    if (res.errors) {
        return data
    }
    dispatch(featureProducts(data))
}


export const removeProducts = () => async (dispatch) => {
    dispatch(clearProducts())
}

const initialState = {
    products: [],
    featureProducts: [],
}

export default function cartReducer(state = initialState, action) {
    switch (action.type) {
        case SET_PRODUCTS:
            return {
                ...state,
                products: [...action.payload]
            }
        case FEATURE_PRODUCTS:
            return {
                ...state,
                featureProducts: [...action.payload]
            }
        case REMOVE_PRODUCTS:
            return null;
        default:
            return state
    }
}
