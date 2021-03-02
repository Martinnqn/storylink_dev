import axios from "axios";
import { API_VERSION } from "../../contexts/StatusApp";
import { tokenRequest as tokenReqDefault } from "../AzureAuth/AuthConfig";

import { AccountInfo, IPublicClientApplication } from "@azure/msal-browser";

class ManagerAxios {
  private DOMAIN = `http://dev-storylink.club:8000/api/v${API_VERSION}/`;
  private instance: IPublicClientApplication;
  private account: AccountInfo;
  private tokenRequest: any;

  constructor(
    instance: IPublicClientApplication,
    acc: AccountInfo,
    tokenRequest?: any
  ) {
    this.instance = instance;
    this.account = acc;
    tokenRequest = tokenRequest || tokenReqDefault;
  }

  public get(url: string, tokenRequest?: any): any {
    let res;
    this.instance
      .acquireTokenSilent({
        ...tokenRequest,
        account: this.account,
        authority: process.env.REACT_APP_AUTH_AUTHORITY,
      })
      .then((response) => {
        console.log(response);
        console.log(response.accessToken);
        if (response.accessToken) {
          let headers = {
            Authorization: `Bearer ${response.accessToken}`,
            Accept: "application/json",
          };
          res = axios.get(url, { headers: headers });
        }
      });
    return res;
  }
}

export default ManagerAxios;
