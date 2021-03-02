import React, { useState, useEffect, useContext } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import AuthRoute from "./components/accountSign/AuthRoute";
import styled from "styled-components/macro";

import "./App.css";
import ResponsiveMenu from "./components/menu/MenuResponsive";
import LoadingApp from "./components/LoadingApp";
import Home from "./components/Home";
//import Profile from "./components/userProfile/Profile";
import { Profile } from "./components/AzureAuth/Profile";
import Settings from "./components/Setting";
import { Container } from "semantic-ui-react";
import { urls as urlDomain } from "./components/url/URLDomain";
import BaseContext from "./contexts/BaseContext";
import UserContext from "./contexts/UserContext";
import AppContext from "./contexts/AppContext";

import STATUS from "./contexts/StatusApp";
import NotFoundPage from "./components/NotFoundPage";

// MSAL imports
import { useMsal, useIsAuthenticated } from "@azure/msal-react";
import { loginRequest, tokenRequest } from "./components/AzureAuth/AuthConfig";

function App() {
  const [statusApp, setStatus] = useState(STATUS.loading);
  const [username, setUsername] = useState(null);
  const [imgProfile, setImgProfile] = useState(null);
  const managerURL = useContext(BaseContext).managerURL;
  const managerMediaFiles = useContext(BaseContext).managerMediaFiles;
  const { instance, accounts, inProgress } = useMsal();
  const isAuthenticated = useIsAuthenticated();

  useEffect(() => {
    const fillProfile = () => {
      if (accounts.length > 0) {
        instance
        .acquireTokenSilent({
          ...tokenRequest,
          account: accounts[0],
          authority: process.env.REACT_APP_AUTH_AUTHORITY,
        })
        .then((response) => {
          console.log(response);
          console.log(response.accessToken);
        });
        setUsername(accounts[0].given_name);
        //setImgProfile(managerMediaFiles.getAbsolutePath(data[0].link_img_perfil));
      }
    };
    if (isAuthenticated) {
      fillProfile();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isAuthenticated]);

  return (
    <AppContext.Provider value={{ statusApp, setStatus }}>
      <UserContext.Provider value={{ username, imgProfile }}>
        <ResponsiveMenu />
        <ContainerApp>
          <Switch>
            <AuthRoute exact path={urlDomain.home} component={Home} />
            <AuthRoute
              exact
              path={`${urlDomain.user_site}`}
              component={Profile}
            />
            <AuthRoute exact path={urlDomain.settings} component={Settings} />
            <Route component={NotFoundPage} />
          </Switch>
        </ContainerApp>
      </UserContext.Provider>
    </AppContext.Provider>
  );
}

const ContainerApp = styled(Container).attrs((props) => ({
  fluid: true,
}))`
  margin-top: 7em;
  padding-bottom: 10em;

  /*&&& {
    margin-left: 0 !important;
    margin-right: 0 !important;
  }*/
`;

export default App;
