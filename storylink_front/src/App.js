import React, { useState, useEffect, useContext } from "react";
import { Switch, Route } from "react-router-dom";

import "./App.css";
import ResponsiveMenu from "./components/MenuResponsive";
import LoadingApp from "./components/LoadingApp";
import Home from "./components/Home";
import Profile from "./components/Profile";
import Settings from "./components/Setting";
import { Container } from "semantic-ui-react";
import { urls as urlDomain } from "./components/url/URLDomain";
import CustomAxios from "./components/http/CustomAxios";
import BaseContext from "./contexts/BaseContext";
import UserContext from "./contexts/UserContext";

import SignIn from "./components/accountManager/SignIn";

const STATUS = {
  loading: "Loading",
  loggedIn: "Logged",
  loggedOut: "NoLogged",
};

function App() {
  const [statusApp, setStatus] = useState(STATUS.loading);
  const [username, setUsername] = useState(null);
  const [imgProfile, setImgProfile] = useState(null);

  const managerURL = useContext(BaseContext).managerURL;

  useEffect(() => {
    fillProfile();
  }, [statusApp]);

  function fillProfile() {
    if (localStorage.getItem("refreshToken") != null) {
      const res = CustomAxios.get(managerURL.getAbsolutePath(urlDomain.whoami));
      res
        .then(({ data }) => {
          setUsername(data[0].username);
          setImgProfile(data[0].link_img_perfil);
        })
        .then(() => {
          setStatus(STATUS.loggedIn);
        });
    } else {
      setStatus(STATUS.loggedOut);
    }
  }

  async function login(username, password) {
    const { data } = await CustomAxios.post(
      managerURL.getAbsolutePath(urlDomain.token_obtain_pair),
      {
        username: username,
        password: password,
      }
    );

    if (data?.access !== "") {
      localStorage.setItem("accessToken", data.access);
    }
    if (data?.refresh !== "") {
      localStorage.setItem("refreshToken", data.refresh);
    }
    setStatus(STATUS.loggedIn);
  }

  async function logout() {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    setStatus(STATUS.loggedOut);
  }

  return statusApp === STATUS.loading ? (
    <LoadingApp />
  ) : statusApp === STATUS.loggedIn ? (
    <>
      <UserContext.Provider value={{ username, imgProfile }}>
        <ResponsiveMenu logout={logout} />
        <Container style={{ marginTop: "7em" }}>
          <Switch>
            <Route exact path={urlDomain.home} component={Home} />
            <Route exact path={`${urlDomain.user_site}`} component={Profile} />
            <Route exact path={urlDomain.settings} component={Settings} />
          </Switch>
        </Container>
      </UserContext.Provider>
    </>
  ) : (
    <SignIn login={login} />
  );
}

export default App;
