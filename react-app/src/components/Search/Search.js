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
        <div>
            <form method="get" action="/api/search" onSubmit={handleSubmit}>
                <button type='submit'><i class="fas fa-telescope"></i></button>
                <input
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
