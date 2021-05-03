const LOAD_STORE = 'session/LOAD_STORE';
const REMOVE_STORE = 'session/REMOVE_STORE';


//Actions
const loadStore = (store) => ({
    type: LOAD_STORE,
    payload: store
})

const dropStore = () => ({
    type: REMOVE_STORE
})


//THUNKS

export const getStore = () => async (dispatch) => {
    const response = await fetch(`/api/stores/mystore`)
    const store = await response.json()
    if (store.errors) {
        return store
    }
    dispatch(loadStore(store))
}


export const createStore = (name, address, user_id, description, image) => async (dispatch) => {
    const formData = new FormData();
    formData.append('name', name)
    formData.append('address', address)
    formData.append('user_id', user_id)
    formData.append('description', description)
    formData.append('image', image)

    const response = await fetch('/api/stores/mystore', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(loadStore(data))
    }
}


export const removeStore = () => async (dispatch) => {
    dispatch(dropStore())
}


const initialState = null

//Reducer

export default function storeReducer(state = initialState, action) {
    switch (action.type) {
        case LOAD_STORE:
            return action.payload
        case REMOVE_STORE:
            return null;
        default:
            return state
    }
}
