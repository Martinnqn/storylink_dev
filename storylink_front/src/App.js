import React from 'react';
import {
  Switch,
  Route,
} from "react-router-dom"

import './App.css';
import ResponsiveMenu from './components/MenuResponsive'
import Home from './components/Home'
import Profile from './components/Profile'
import Settings from './components/Setting'
import { Container } from 'semantic-ui-react';
import { urls as urlDomain } from './components/url/URLDomain'


function App() {

  return (
    <>
      <ResponsiveMenu />
      <Container style={{ marginTop: '7em' }}>
        <Switch>
          <Route exact path={urlDomain.home} component={Home} />
          <Route path={`${urlDomain.user_site}`} component={Profile} />
          <Route path={urlDomain.settings} component={Settings} />
        </Switch>
      </Container>
    </>
  );
}

export default App;
