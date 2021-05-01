const GET_STORE = 'session/GET_STORE'


//Actions
const getStore = (store) => ({
    type: GET_STORE,
        payload: store
})


//THUNKS

export const gettingStore = (store_id) => async (dispatch) => {
    const response = await fetch(`/api/stores/mystore`)
    const store = await response.json()
    if (store.errors) {
        return store
    }
    dispatch(getStore(store))

}

const initialState = {}

//Reducer

export default function storeReducer(state = initialState, action) {
    switch (action.type) {
        case GET_STORE:
            return action.payload
        default:
            return state
    }
}