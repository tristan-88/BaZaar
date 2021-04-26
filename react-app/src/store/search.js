const LOAD = 'search/LOAD';

const load = list => ({
    type: LOAD,
    payload: list
})

export const getSearch = () => async dispatch => {
    const response = await fetch(`/api/search/`);

    if (response.ok) {
        const list = await response.json();
        dispatch(load(list))
        return list;
    }
}

const searchReducer = (state = {}, action) => {
    switch (action.type) {
        case LOAD:
        const newState = {};
        action.payload.forEach((search) => {
            newState[search.id] = search;
        })
        return newState;
        default:
            return state;
    }
}

export default searchReducer;
