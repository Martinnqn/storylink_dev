/**
 * Configuration object to be passed to MSAL instance on creation.
 * For a full list of MSAL.js configuration parameters, visit:
 * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/configuration.md
 * For more details on using MSAL.js with Azure AD B2C, visit:
 * https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/working-with-b2c.md
 */
import { LogLevel } from "@azure/msal-browser";

// Config object to be passed to Msal on creation
export const msalConfig = {
  auth: {
    clientId: process.env.REACT_APP_AUTH_CLIENT_ID,
    authority: process.env.REACT_APP_AUTH_AUTHORITY,
    tenant: process.env.REACT_APP_AUTH_TENANT,
    redirectUri: process.env.REACT_APP_AUTH_REDIRECT_URI,
    postLogoutRedirectUri: window.location.origin,
    knownAuthorities: [process.env.REACT_APP_AUTH_KNOWN_AUTHORITY,],
    protocolMode: process.env.REACT_APP_AUTH_PROTOCOL_MODE,
  },
  cache: {
    cacheLocation: process.env.REACT_APP_AUTH_CACHE_LOCATION, // This configures where your cache will be stored
    storeAuthStateInCookie: process.env.REACT_APP_AUTH_STORE_STATE_IN_COOKIE, // Set this to "true" if you are having issues on IE11 or Edge
  },
  system: {
    loggerOptions: {
      loggerCallback: (level, message, containsPii) => {
        if (containsPii) {
          return;
        }
        switch (level) {
          case LogLevel.Error:
            console.error(message);
            return;
          case LogLevel.Info:
            console.info(message);
            return;
          case LogLevel.Verbose:
            console.debug(message);
            return;
          case LogLevel.Warning:
            console.warn(message);
            return;
        }
      },
      piiLoggingEnabled: true,
    },
    windowHashTimeout: 60000,
    iframeHashTimeout: 6000,
    loadFrameTimeout: 0,
    asyncPopups: false,
  },
};

const scopesGraph = ["openid", "offline_access"];

const scopesStorylink = [
  "https://storylinkB2C.onmicrosoft.com/storylink-drf/Files.Read",
]; // e.g. "https://<your-tenant>.onmicrosoft.com/<your-api>/<your-scope>"

/**
 * Todos los scopes deben estar en el loginRequest, asi se obtiene un access_token para storylink-drf.
 *  NOTA: Supuestamente no se pueden mezclar scopes de diferentes recursos (excepcion "openid" y
 * "offline_access" son compatibles con cualquier recurso). Por el momento no es necesario mezclar recursos,
 *  ya que solo se usa storylink-drf. "openid" y "offline_access" no retornan un access_token.
 * El access_token retornado solo sirve para storylink-drf/<nombre-scope-en-loginRequest>
 */
export const loginRequest = {
  scopes: [...scopesGraph, ...scopesStorylink],
};

/**
 * Por ahora tokenRequest se usa en acquireTokenSilent para recuperar un access_token.
 */
export const tokenRequest = {
  scopes: scopesStorylink,
};
