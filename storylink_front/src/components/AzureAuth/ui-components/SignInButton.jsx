import React, { useState } from "react";
import { useMsal } from "@azure/msal-react";
import { Button, Menu, MenuItem } from "semantic-ui-react";
import { loginRequest } from "../AuthConfig";

export const SignInButton = () => {
  const { instance } = useMsal();

  const handleLogin = () => {
    instance.loginRedirect(loginRequest);
  };

  return (
    <Menu.Menu position="right">
      <Menu.Item onClick={() => handleLogin()} key="loginRedirect">
        Iniciar Sesion
      </Menu.Item>
    </Menu.Menu>
  );
};
