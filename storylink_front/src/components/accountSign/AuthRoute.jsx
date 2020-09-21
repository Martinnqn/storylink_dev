import React, { useContext } from "react";
import { Redirect, Route, Switch } from "react-router";

import STATUS from "../../contexts/StatusApp";
import AppContext from "../../contexts/AppContext";

import { urls as urlDomain } from "../url/URLDomain";
import SignIn from "./SignIn";

const AuthRoute = (props) => {
  const statusApp = useContext(AppContext).statusApp;

  if (statusApp === STATUS.loggedIn) {
    return <Route {...props} />;
  } else {
    return (
      <Switch>
        <Route exact path={urlDomain.home} render={() => <SignIn />} />
        <Redirect to={urlDomain.home} />;
      </Switch>
    );
  }
};

export default AuthRoute;
