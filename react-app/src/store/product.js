const SET_PRODUCTS = 'product/SET_PRODUCTS'
const REMOVE_PRODUCTS = 'product/REMOVE_PRODUCTS'
const ADD_PRODUCTS = 'products/ADD_PRODUCTS'
const ADD_PHOTOS = 'products/ADD_PHOTOS'
const GET_PHOTOS = 'products/GET_PHOTOS'
const FEATURE_PRODUCTS = 'product/FEATURE_PRODUCTS'
const FILTERED_PRODUCTS = 'product/FILTERED_PRODUCTS'

//Action
const setProducts = (products) => ({
    type: SET_PRODUCTS,
    payload: products
})

const clearProducts = () => ({
    type: REMOVE_PRODUCTS
})

const createProduct = (product) => ({
    type: ADD_PRODUCTS,
    payload: product
})

const addPhotos = (photos) => ({
    type: ADD_PHOTOS,
    payload: photos
})

const getPhotos = (photos) => ({
    type: GET_PHOTOS,
    payload: photos
})

const filteredProducts = (products) => ({
    type: FILTERED_PRODUCTS,
    payload: products
})

const featureProducts = (products) => ({
    type: FEATURE_PRODUCTS,
    payload: products
})


//Thunks
export const addProductPhotos = (image, product_id) => async (dispatch) => {
    const formData = new FormData();
    formData.append('image', image)
    formData.append('product_id', product_id)

    const response = await fetch('/api/photos', {
        method: "POST",
        body: formData
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(addPhotos(data))
    }
}

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

export const loadFilteredProducts = (id) => async (dispatch) => {
    let res = await fetch(`/api/products/bytag/${id}`)
    let products = await res.json()
    if (res.ok) {
        dispatch(filteredProducts(products))
    }
}


export const addProduct = (name, store_id, price, quantity, description, image) => async (dispatch) => {
    const formData = new FormData();
    formData.append('name', name)
    formData.append('store_id', store_id)
    formData.append('price', price)
    formData.append('quantity', quantity)
    formData.append('description', description)

    const response = await fetch('/api/products', {
        method: "POST",
        body: formData
    })

    if (response.ok) {
        const data = await response.json();
        let product_id = data.id
        await dispatch(addProductPhotos(image, product_id))
        await dispatch(loadProducts())
    }
}


//Hello guys <3

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
        case FILTERED_PRODUCTS:
            return {
                ...state,
                filteredProducts: [...action.payload]
            }
        case REMOVE_PRODUCTS:
            return null;
        default:
            return state
    }
}
