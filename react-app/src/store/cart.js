const SET_CART = 'cart/SET_CART'
const REMOVE_CART = 'cart/REMOVE_USER'
const INCREMENT_ITEM = 'cart/INCREMENT_ITEM'
const DECREMENT_ITEM = 'cart/DECREMENT_ITEM'

//Actions
const setCart = (cart) => ({
    type: SET_CART,
    payload: cart
})

const deleteCart = () => ({
    type: REMOVE_CART
})

const incrementItem = (productId) => ({
    type: INCREMENT_ITEM,
    payload: productId,
})
const decrementItem = (productId) => ({
    type: DECREMENT_ITEM,
    payload: productId,
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

export const addToCart = (cart_id, product_id) => async (dispatch) => {
    const formData = new FormData()
    formData.append('cart_id', cart_id)
    formData.append('product_id', product_id)
    const res = await fetch(`/api/carts/${cart_id}/add/${product_id}`, {
        method: 'POST',
        body: formData
    })
    let data = await res.json()
    if (data) {
        dispatch(setCart(data))
    }
}
export const incrementItemCount = (cart_id, product_id) => async (dispatch) => {
    const formData = new FormData()
    formData.append('cart_id', cart_id)
    formData.append('product_id', product_id)
    const res = await fetch(`/api/carts/${cart_id}/add/${product_id}`, {
        method: 'PUT',
        body: formData
    })
    let data = await res.json()
    if (data) {
        dispatch(incrementItem(product_id))
    }
}
export const decrementItemCount = (cart_id, product_id) => async (dispatch) => {
    const formData = new FormData()
    formData.append('cart_id', cart_id)
    formData.append('product_id', product_id)
    const res = await fetch(`/api/carts/${cart_id}/remove/${product_id}`, {
        method: 'PUT',
        body: formData
    })
    let data = await res.json()
    console.log("DATA", data)
    if (data) {
        dispatch(decrementItem(product_id))
    }
}

export const completeOrder = (cart_id) => async (dispatch) => {
    const res = await fetch(`/api/carts/${cart_id}/close`)
    let data = await res.json()
    if (res.ok) {
        dispatch(setCart(data))
    }
}

const initialState = {

}

export default function cartReducer(state = initialState, action) {
    let newState
    switch (action.type) {
        case SET_CART:
            return { ...action.payload }
        case REMOVE_CART:
            return null;
        case INCREMENT_ITEM:
            newState = Object.assign({}, state)
            for (let product of newState.products) {
                if (product.product_id === action.payload) {
                    product.quantity++
                    break
               }
            }
            return newState
        case DECREMENT_ITEM:
            newState = Object.assign({}, state)
            for (let i = 0; i < newState.products.length; i ++) {
                let product = newState.products[i]
                if (product.product_id === action.payload) {
                    product.quantity--
                    if (product.quantity === 0) {
                        newState.products.splice(i, 1)
                    }
                    break
               }
            }
            return newState
        default:
            return state
    }
}
