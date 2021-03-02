import React, { useContext } from "react";
import { Redirect, Route, Switch } from "react-router";

import { urls as urlDomain } from "../url/URLDomain";
import SignIn from "./SignIn";
import { useIsAuthenticated } from "@azure/msal-react";

const AuthRoute = (props) => {
  const isAuthenticated = useIsAuthenticated();

  if (isAuthenticated) {
    return <Route {...props} />;
  } else {
    return (
      <Switch>
        <Route exact path={urlDomain.home} render={() => <SignIn />} />
        <Redirect to={urlDomain.home} />
      </Switch>
    );
  }
};

export default AuthRoute;
