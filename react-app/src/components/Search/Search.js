import * as searchActions from '../../store/search';
import React, { useState } from 'react';
import { useDispatch, useSelector} from 'react-redux';
import { useHistory } from 'react-router-dom';
import './Search.css';

function Search() {
    const dispatch = useDispatch();
    const history = useHistory();
    const [ search, setSearch ] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        dispatch(searchActions.getSearch(search))
        //need to use history here to route to the page that we need
        // history.push('the correct path we want here')
    }

    return (
        <div className='search-bar'>
            <form method="get" action="localhost:5000/api/search" onSubmit={(e) => handleSubmit(e)}>
                <button onClick={(e) => handleSubmit(e)} style={{background:'white', borderRadius:'50%', height:'30px', width:'30px'}}type='submit'><i class="fas fa-telescope"></i></button>
                <input
                    style={{width:'20rem', background:'#f2f1f9', border:'none', padding:'0.5rem'}}
                    value={search}
                    name='search'
                    placeholder='Search...'
                    onChange={(e) => setSearch(e.target.value)}
                />
            </form>
        </div>
    );
}


export default Search;
