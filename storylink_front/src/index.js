import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";
import "semantic-ui-css/semantic.min.css";
import { BrowserRouter as Router } from "react-router-dom";
import BaseContext from "./contexts/BaseContext";
import ManagerURL from "./components/url/ManagerURL";
import { API_VERSION } from "./contexts/StatusApp";

// MSAL imports
import { PublicClientApplication } from "@azure/msal-browser";
import { msalConfig } from "./components/AzureAuth/AuthConfig";

const msalInstance = new PublicClientApplication(msalConfig);

const managerURL = new ManagerURL(
  `http://dev-storylink.club:8000/api/v${API_VERSION}/`
);
const managerMediaFiles = new ManagerURL(`http://dev-storylink.club:8000/media/`);

ReactDOM.render(
  <Router>
    <BaseContext.Provider value={{ managerURL, managerMediaFiles }}>
      <App pca={msalInstance}/>
    </BaseContext.Provider>
  </Router>,
  document.getElementById("root")
);


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
