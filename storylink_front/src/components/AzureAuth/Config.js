const apiConfig = {
    tenant: '8f366d86-6d3f-43f5-81e1-d84cd7bd349b',
    signInPolicy: 'B2C_1_reactjs_susin',
    applicationId: 'cbca2d38-fa68-4236-bdba-f97fc0cffb9d',
    authority: 'https://storylinkB2C.b2clogin.com/storylinkB2C.onmicrosoft.com/B2C_1_reactjs_susin',
    cacheLocation: 'localStorage',
    scopes: ['offline_access', 'openid'],
    redirectUri: 'http://localhost:3000/',
    postLogoutRedirectUri: window.location.origin,
  };

  export default apiConfig;