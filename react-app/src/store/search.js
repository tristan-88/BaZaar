const LOAD_SEARCH = 'search/LOAD_SEARCH';

const load = list => ({
    type: LOAD_SEARCH,
    payload: list
})

export const getSearch = (search) => async dispatch => {
    const response = await fetch(`/api/search/${search}`);

    if (response.ok) {
        const list = await response.json();
        dispatch(load(list))
        return list;
    }
}

const initialState = {
    'products': [],
    'search': []

}

const searchReducer = (state = initialState, action) => {
    switch (action.type) {
        // case LOAD_SEARCH:
        //     const newState = {};
        //     action.payload.forEach((search) => {
        //         newState[search.id] = search;
        //     })
        //     return newState;
        case LOAD_SEARCH:
            return {
                'products': [...action.payload.Products],
                'stores': [...action.payload.Stores]
            }
        default:
            return state;
    }
}

export default searchReducer;
