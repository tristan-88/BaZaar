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
        <div>
            <form method="get" action="localhost:5000/api/search" onSubmit={(e) => handleSubmit(e)}>
                <button onClick={(e) => handleSubmit(e)} type='submit'><i class="fas fa-telescope"></i></button>
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
