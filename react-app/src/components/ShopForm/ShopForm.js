import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import { createStore } from '../../store/store';
import './ShopForm.css';

const ShopForm = () => {
    const dispatch = useDispatch()
    const user_id = useSelector(state => state.session.user)
    const [name, setName] = useState('');
    const [address, setAddress] = useState('');
    const [description, setDescription] = useState('');
    const [image, setImage] =useState(null);

    const shopCreate = async (e) => {
        e.preventDefault();
        await dispatch(createStore(name, address, user_id, description, image))
    }

    const updateName = (e) => {
        setName(e.target.value);
    }

    const updateAddress = (e) => {
        setAddress(e.target.value);
    }

    const updateDescription = (e) => {
        setDescription(e.target.value)
    }

    const updateImage = (e) => {
        const file = e.target.files[0];
        setImage(file);
    }

    return (
        <div className="form-body">
            <div className="form-container">
                <form onSubmit={shopCreate}>
                    <div className="form-inputs">
            <div>
                <label>Name</label>
                <input
                type="text"
                name="name"
                onChange={updateName}
                value={name}
                ></input>
            </div>
            <div>
                <label>Description</label>
                <input
                type="text"
                name="description"
                onChange={updateDescription}
                value={description}
                ></input>
            </div>
            <div>
                <label>Address</label>
                <input
                type="text"
                name="address"
                onChange={updateAddress}
                value={address}
                ></input>
            </div>
            <div>
                <label>Shop Photo</label>
                <input
                type="file"
                accept="image/*"
                onChange={updateImage}
                ></input>
                        </div>
                    </div>
                        <div className="button-div">
                        <button type="submit">Create Shop</button>
                   </div> 
            </form>
            </div>
        </div>
    )
}

export default ShopForm;
