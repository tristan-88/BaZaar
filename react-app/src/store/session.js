import { removeCart } from './cart';
import { removeStore } from './store';

const SET_USER = 'session/SET_USER'
const REMOVE_USER = 'session/REMOVE_USER'

//Actions
const setUser = (user) => ({
  type: SET_USER,
  payload: user
})

const removeUser = (user) => ({
  type: REMOVE_USER,
})


//Thunks
export const authenticate = () => async (dispatch) => {
  const response = await fetch('/api/auth/', {
    headers: {
      'Content-Type': 'application/json'
    }
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data))
  }

}

export const login = (email, password) => async (dispatch) => {
  const response = await fetch('/api/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      email,
      password
    })
  });
  const data = await response.json();

  if (data.errors) {
    return data
  }
  dispatch(setUser(data))
  return {}
}

export const logout = () => async (dispatch) => {
  await fetch("/api/auth/logout", {
    headers: {
      "Content-Type": "application/json",
    }
  });

  dispatch(removeUser())
  dispatch(removeCart())
  dispatch(removeStore())
};


export const signUp = (firstname, lastname, username, email, image, password, address) => async (dispatch) => {
  const formData = new FormData();
  formData.append('first_name', firstname)
  formData.append('last_name', lastname)
  formData.append('username', username)
  formData.append('email', email)
  formData.append('image', image)
  formData.append('password', password)
  formData.append('address', address)


  const response = await fetch('/api/auth/signup', {
    method: "POST",
    body: formData
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data))
  }
};

const initialState = { user: null };

export default function reducer(state = initialState, action) {

  switch (action.type) {
    case SET_USER:
      return { user: action.payload };
    case REMOVE_USER:
      return { user: null };
    default:
      return state
  }

}
