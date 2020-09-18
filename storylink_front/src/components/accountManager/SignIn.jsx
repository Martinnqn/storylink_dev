import React, { useState, useContext } from "react";
import ReactDOM from "react-dom";
import {
  Button,
  Form,
  Grid,
  Header,
  Segment,
  Image,
  Message,
} from "semantic-ui-react";
import Logo from "../../assets/story_minim.svg";
import CustomAxios from "../http/CustomAxios";
import { urls as urlDomain } from "../url/URLDomain";

import BaseContext from "../../contexts/BaseContext";

const SignIn = ({ handleIsLogged, handleUsername, handleImg }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const managerURL = useContext(BaseContext);

  async function login(e) {
    const { data } = await CustomAxios.post(
      managerURL.getPath(urlDomain.token_obtain_pair),
      {
        username: username,
        password: password,
      }
    );

    if (data?.access !== "") {
      localStorage.setItem("accessToken", data.access);
    }
    if (data?.refresh !== "") {
      localStorage.setItem("refreshToken", data.refresh);
    }
    handleIsLogged(true);
  }

  return (
    <Grid textAlign="center" style={{ height: "100vh" }} verticalAlign="middle">
      <Grid.Column style={{ maxWidth: 450 }}>
        <Header as="h2" color="teal" textAlign="center">
          <Image src={Logo} /> Log-in to your account
        </Header>
        <Form size="large">
          <Segment stacked>
            <Form.Input
              fluid
              icon="user"
              iconPosition="left"
              placeholder="username"
              onChange={(e) => setUsername(e.target.value)}
            />
            <Form.Input
              fluid
              icon="lock"
              iconPosition="left"
              placeholder="Password"
              type="password"
              onChange={(e) => setPassword(e.target.value)}
            />
            <Button color="teal" fluid size="large" onClick={login}>
              Login
            </Button>
          </Segment>
        </Form>
        <Message>
          New to us? <a href="#">Sign Up</a>
        </Message>
      </Grid.Column>
    </Grid>
  );
};

export default SignIn;
