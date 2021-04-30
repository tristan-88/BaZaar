export const photoUpload = ( submission ) => async (dispatch) => {
    const { photo_url, caption } = submission
    const formData = new FormData() //packages up submission data nicely
    formData.append("caption", caption)  // every single non file upload
    // for multiple files
    //   if (images && images.length !== 0) {
    //     for (var i = 0; i < images.length; i++) {
    //       formData.append("images", images[i]);
    //     }
    //   }
    if(photo_url){
        formData.append("photo_url", photo_url)
    }
    const response = await fetch('/api/posts/', {  //not done routes yet
        method: "POST",
        headers: {
            'Content-Type': 'multipart/form-data'
        }, body: formData
    });
    if(response.ok){  //202
        const data = await response.json();
        return data
    }
    // if (data.errors) {
    //     return;
    // }
    // dispatch(setUser(data))
}
// thunks
export const authenticate = () => async (dispatch) => {
    const response = await fetch('/api/auth/', {
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const data = await response.json();
    if (data.errors) {
        return;
    }
    dispatch(setUser(data))
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
        return data;
    }
    dispatch(setUser(data));
    return {};
}
export const logout = () => async (dispatch) => {
    const response = await fetch("/api/auth/logout", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    dispatch(removeUser());
};
export const signUp = (username, email, password) => async (dispatch)=> {
    const response = await fetch("/api/auth/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username,
            email,
            password,
        }),
    });
    const data = await response.json();
    dispatch(setUser(data));
}
// reducer
const initialState = { user: null };
// useSelector(state => state.session.user)
export default function reducer(state = initialState, action) {
    switch (action.type) {
        case SET_USER:
            return { user: action.payload };
        case REMOVE_USER:
            return { user: null };
        default:
            return state;
    }
}

////


import React, { useEffect, useState } from "react";
//import { NavLink } from "react-router-dom";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { photoUpload } from "../../store/session"  // may change name of this function and store location! curly braces from export const
function PhotoUploadPage() {
  const [ caption, setCaption ] = useState("")
  const [ photoUrl, setPhotoUrl ] = useState("")
  const dispatch = useDispatch()
  const handleSubmit = async (e) => {
    e.preventDefault();
    const submission = { caption, photoUrl }
    let createdPhoto = await dispatch(photoUpload(submission)) // line ~42 of session.js data return
    if(createdPhoto){            // if photo created, modal, redirect, etc.
      // redirect to (/feed)
    }
  }
  return (
    <>
      <h1>Your Photo here</h1>
      <form onSubmit={handleSubmit} enctype="multipart/form">
        <div>
          <textarea
            type="text"
            value = {caption}
            placeholder = "Write what u want to say"
            onChange={ (e) => setCaption(e.target.value)}
          />
        </div>
        <div>
          <input
            name = "photo_url"
            type = "file"
            placeholder = "Upload"
            onChange = { (e) => setPhotoUrl(e.target.files[0])} // only accepts ONE photo if they try and upload multiple files
          />
        </div>
      </form>
    </>
  );
}
export default PhotoUploadPage;
