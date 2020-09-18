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
import UserContext from "./contexts/UserContext";

import SignIn from "./components/accountManager/SignIn";

function App() {
  const [isLogged, setIsLogged] = useState(false);
  const [username, setUsername] = useState(null);
  const [imgProfile, setImgProfile] = useState(null);

  const managerURL = useContext(BaseContext).managerURL;

  useEffect(() => {
    fillProfile();
    setIsLogged(true);
  }, []);

  async function fillProfile() {
    const { data } = await CustomAxios.get(
      managerURL.getAbsolutePath(urlDomain.whoami)
    );
    setUsername(data[0].username);
    setImgProfile(data[0].link_img_perfil);
  }

  return isLogged ? (
    <>
      <UserContext.Provider value={{ username, imgProfile }}>
        <ResponsiveMenu />
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
    <SignIn handleIsLogged={setIsLogged} />
  );
}

export default App;
