import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import './index.css';
import App from './App';
import configureStore from './store';
import * as searchActions from './store/search';
import * as sessionActions from './store/session';
import * as cartActions from './store/cart';
import * as productActions from './store/product';
import * as storeActions from './store/store'


const store = configureStore();

if (process.env.NODE_ENV !== 'production') {
  window.searchActions = searchActions;
  window.sessionActions = sessionActions;
  window.cartActions = cartActions;
  window.productActions = productActions;
  window.storeActions = storeActions;
}

ReactDOM.render(

  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
