import React from 'react';
import { NavLink, useHistory } from 'react-router-dom'
import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'



const BigItemCard = (product) => {
  const history = useHistory()
  const dispatch = useDispatch()



  return (
    <>
      <div>
        <img src={product.photo_url}></img>
      </div>
    </>
  )
}