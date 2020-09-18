import React, { useState, useEffect, useContext } from "react";
import { Switch, Route } from "react-router-dom";

import "./App.css";
import ResponsiveMenu from "./components/MenuResponsive";
import Home from "./components/Home";
import Profile from "./components/Profile";
import Settings from "./components/Setting";
import { Container } from "semantic-ui-react";
import { urls as urlDomain } from "./components/url/URLDomain";
import CustomAxios from "./components/http/CustomAxios";
import BaseContext from "./contexts/BaseContext";

import SignIn from "./components/accountManager/SignIn";

function App() {
  const [isLogged, setIsLogged] = useState(false);
  const [username, setUsername] = useState(null);
  const [imgProfile, setImgProfile] = useState(null);

  const managerURL = useContext(BaseContext);

  useEffect(() => {
    fillProfile();
    setIsLogged(true);
  }, []);

  async function fillProfile() {
    const { data } = await CustomAxios.get(
      managerURL.getPath(urlDomain.whoami)
    );
    setUsername(data.username);
    setImgProfile(data.imgProfile);
  }

  return isLogged ? (
    <>
      <ResponsiveMenu />
      <Container style={{ marginTop: "7em" }}>
        <Switch>
          <Route exact path={urlDomain.home} component={Home} />
          <Route path={`${urlDomain.user_site}`} component={Profile} />
          <Route path={urlDomain.settings} component={Settings} />
        </Switch>
      </Container>
    </>
  ) : (
    <SignIn handleIsLogged={setIsLogged} />
  );
}

export default App;
