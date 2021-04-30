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
import HomePage from "./components/HomePage/HomePage";
import { authenticate } from "./store/session";

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
      </Switch>
    </BrowserRouter>
  );
}

export default App;
