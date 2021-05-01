import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux'
import { BrowserRouter, Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginForm/LoginForm";
import SignUpForm from "./components/auth/SignUpForm/SignUpForm";
import NavBar from "./components/NavBar/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
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
        <Route exact path="/login" >
          <LoginForm />
        </Route>
        <Route exact path="/sign-up" >
          <SignUpForm />
        </Route>
        <Route exact path="/products/:id">
          <SingleProductPage />
        </Route>
        <ProtectedRoute exact path="/users" >
          <User />
        </ProtectedRoute>
        <ProtectedRoute exact path="/users/:userId" >
          <User />
        </ProtectedRoute>
        <Route exact path="/" >
          <HomePage />
        </Route>
        <ProtectedRoute exact path='/store'>
          <Store />
        </ProtectedRoute>
        <ProtectedRoute exact path='/cart'>
          <Cart />
        </ProtectedRoute >
      </Switch>
    </BrowserRouter>
  );
}

export default App;
