import * as searchActions from '../../store/search';
import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import './Search.css';

function Search() {
    const dispatch = useDispatch();
    const history = useHistory();
    const [search, setSearch] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        await dispatch(searchActions.getSearch(search))
        history.push('/search')
    }

    return (
        <div  id="search-bar-container">
            <form className='search-bar-container' method="get" style={{border:'none', width: "700px"}} action="/api/search" onSubmit={(e)=> handleSubmit(e)}>
                <input
                    style={{width:'30rem', height:'1.5rem', background:'#edf6f9', border:"none", padding:'0.5rem'}}
                    value={search}
                    placeholder='Search...'
                    onChange={(e) => setSearch(e.target.value)}
                />
                <button onClick={(e) => handleSubmit(e)} style={{
                    background:"#edf6f9", borderRadius:"50%", height:"30px", width:"30px", outline:'none'}}
                    type="submit"><i className="fas fa-search" id="fas fa-search" style={{color:'#f58a07', border:'none',outline:'none'}}></i>
                    </button>
            </form>
        </div>
    );
}


export default Search;
