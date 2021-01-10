import React, { useState, useEffect, useContext } from "react";
import { Switch, Route } from "react-router-dom";
import AuthRoute from "./components/accountSign/AuthRoute";
import styled from "styled-components/macro";

import "./App.css";
import ResponsiveMenu from "./components/menu/MenuResponsive";
import LoadingApp from "./components/LoadingApp";
import Home from "./components/Home";
import Profile from "./components/userProfile/Profile";
import Settings from "./components/Setting";
import { Container } from "semantic-ui-react";
import { urls as urlDomain } from "./components/url/URLDomain";
import CustomAxios from "./components/http/CustomAxios";
import BaseContext from "./contexts/BaseContext";
import UserContext from "./contexts/UserContext";
import AppContext from "./contexts/AppContext";

import STATUS from "./contexts/StatusApp";
import NotFoundPage from "./components/NotFoundPage";

function App() {
  const [statusApp, setStatus] = useState(STATUS.loading);
  const [username, setUsername] = useState(null);
  const [imgProfile, setImgProfile] = useState(null);
  const managerURL = useContext(BaseContext).managerURL;
  const managerMediaFiles = useContext(BaseContext).managerMediaFiles;

  useEffect(() => {
    const fillProfile = () => {
      const res = CustomAxios.get(managerURL.getAbsolutePath(urlDomain.whoami));
      res
        .then(({ data, status }) => {
          if (status === 200) {
            setUsername(data[0].username);
            setImgProfile(
              managerMediaFiles.getAbsolutePath(data[0].link_img_perfil)
            );
            setStatus(STATUS.loggedIn);
          }
        })
        .catch(({ error }) => {
          setStatus(STATUS.loggedOut);
        });
    };
    if (statusApp !== STATUS.loggedOut) {
      fillProfile();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [statusApp]);

  async function logout() {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    setStatus(STATUS.loggedOut);
  }

  return statusApp === STATUS.loading ? (
    <LoadingApp />
  ) : (
    <AppContext.Provider value={{ statusApp, setStatus }}>
      <UserContext.Provider value={{ username, imgProfile }}>
        <ResponsiveMenu logout={logout} />
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
