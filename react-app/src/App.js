import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux'
import { BrowserRouter, Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginForm/LoginForm";
import SignUpForm from "./components/auth/SignUpForm/SignUpForm";
import NavBar from "./components/NavBar/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList/UsersList";
import SingleProductPage from "./components/SingleProductPage/SingleProductPage"
import User from "./components/User/User";
import Cart from "./components/Cart/Cart"
import HomePage from "./components/HomePage/HomePage";
import { authenticate } from "./store/session";
import Store from './components/Store/Store'

function App() {
  const dispatch = useDispatch()
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <Route path="/products/:id">
          <SingleProductPage />
        </Route>
        <ProtectedRoute path="/users" exact={true}>
          <UsersList />
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId" exact={true}>
          <User />
        </ProtectedRoute>
        <Route path="/" exact={true}>
          <HomePage />
        </Route>
        <ProtectedRoute>
          <Store path='/store' exact={true} />
        </ProtectedRoute>
        <ProtectedRoute>
          <Cart path='/cart' exact={true} />
        </ProtectedRoute >
        <Route exact path >
          <SearchResultPage />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
