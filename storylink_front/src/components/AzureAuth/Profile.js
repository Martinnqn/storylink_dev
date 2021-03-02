import React, { useEffect, useState } from "react";

// Msal imports
import {
  MsalAuthenticationTemplate,
  useMsal,
  useAccount,
} from "@azure/msal-react";
import { InteractionType } from "@azure/msal-browser";
import { loginRequest, tokenRequest } from "./AuthConfig";

// Sample app imports
import { ProfileData } from "./ui-components/ProfileData";
import { Loading } from "./ui-components/Loading";
import { ErrorComponent } from "./ui-components/ErrorComponent";
import { Container } from "semantic-ui-react";
import apiConfig from "./Config";

// Material-ui imports

const ProfileContent = () => {
  const { instance, accounts, inProgress } = useMsal();
  const account = useAccount(accounts[0] || {});
  const [graphData, setGraphData] = useState(null);

  useEffect(() => {
    if (account && inProgress === "none") {
      console.log(account);
      instance
        .acquireTokenSilent({
          ...tokenRequest,
          account: account,
          authority: process.env.REACT_APP_AUTH_AUTHORITY,
        })
        .then((response) => {
          console.log(response);
          console.log(response.accessToken);
        });
    }
  }, [account, inProgress, instance]);

  return (
    <Container>
      {graphData ? <ProfileData graphData={graphData} /> : null}
    </Container>
  );
};

export function Profile() {
  const authRequest = {
    ...tokenRequest, //si hay problemas usar ...loginRequest
  };

  return (
    <MsalAuthenticationTemplate
      interactionType={InteractionType.Redirect}
      authenticationRequest={authRequest}
      errorComponent={ErrorComponent}
      loadingComponent={Loading}
    >
      <ProfileContent />
    </MsalAuthenticationTemplate>
  );
}
