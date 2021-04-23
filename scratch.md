
# Renamed default branch
If you have a local clone, you can update it by running:
git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a


# app/seeds/users.py
add: RESTART IDENTITY in db.session.execute
add: 'TRUNCATE users RESTART IDENTITY CASCADE;' in db.session.execute

# store/index.js
import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session';
​
const rootReducer = combineReducers({
    session
});
​
let enhancer;
​
if (process.env.NODE_ENV === 'production') {
    enhancer = applyMiddleware(thunk);
} else {
    const logger = require('redux-logger').default;
    const composeEnhancers =
        window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
    enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}
​
const configureStore = (preloadedState) => {
    return createStore(rootReducer, preloadedState, enhancer);
};
​
export default configureStore;

# store/session.js
const SET_USER = 'session/SET_USER';
const REMOVE_USER = "session/REMOVED_USER";

const setUser = (user) =>({
    type: SET_USER,
    payload: user

})

const removeUser = () => ({
    type: REMOVE_USER
})

const initialState = { user: null}

//useSelector(state => state.session.user)

export default function reducer (state=initialState, action){
    switch(action.type){
        case SET_USER:
            return {user:action.payload};
        case REMOVE_USER:
            return {user:null};
        default:
            return state;
    }
}

# react-app/src/store/session.js

on export const authenticate change it to thunk

change all of the export functions 

export const login = (email, password) => async (dispatch) =>{
    .... drop the async to another level with "dispatch"
    const data = await response.json()
    dispatch(setUser(data)/removeUser() => logout)
}