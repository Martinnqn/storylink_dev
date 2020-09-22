import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";
import "semantic-ui-css/semantic.min.css";
import { BrowserRouter as Router } from "react-router-dom";
import BaseContext from "./contexts/BaseContext";
import ManagerURL from "./components/url/ManagerURL";

const API_VERSION = 1;
const managerURL = new ManagerURL(
  `http://192.168.1.39:8000/api/v${API_VERSION}/`
);
const managerMediaFiles = new ManagerURL(`http://192.168.1.39:8000/media/`);

ReactDOM.render(
  <Router>
    <BaseContext.Provider value={{ managerURL, managerMediaFiles }}>
      <App />
    </BaseContext.Provider>
  </Router>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
