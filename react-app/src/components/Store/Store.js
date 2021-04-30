import React, { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux'
import './Store.css'


const Store = () => {
    const store = useSelector(state => state.session?.user?.store) 

    return (
        <>
            <div>
                
            </div>
            </>
    )

}

export default Store