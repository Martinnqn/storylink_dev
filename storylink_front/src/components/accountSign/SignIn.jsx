import Axios from "axios";
import React, { useState, useContext, useEffect } from "react";
import {
  Button,
  Form,
  Grid,
  Header,
  Segment,
  Image,
  Message,
  Icon,
} from "semantic-ui-react";
import Logo from "../../assets/story_minim.svg";
import AppContext from "../../contexts/AppContext";
import BaseContext from "../../contexts/BaseContext";
import STATUS from "../../contexts/StatusApp";
import { updateTokens } from "../http/CustomAxios";
import { urls as urlDomain } from "../url/URLDomain";
import SignUp from "./SignUp";

const SignIn = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [showSignUp, SetShowSignUp] = useState(false);

  const [title, setTitle] = useState("Iniciando sesion");
  const [msg, setMsg] = useState("");
  const [isInfo, setIsInfo] = useState(true);
  const [svProblem, setSvProblem] = useState(false);
  const [showMessageSinging, setShowMessageSinging] = useState(false);

  const setStatus = useContext(AppContext).setStatus;
  const managerURL = useContext(BaseContext).managerURL;

  useEffect(() => {
    if (!isInfo) {
      setTitle("No es posible iniciar sesion.");
      if (!svProblem) {
        setMsg("El usuario o contrasena no son correctos.");
      } else {
        setMsg("Tenemos un problema con nuestro servicio de inicio de sesion.");
      }
    } else {
      setTitle("Iniciando sesion");
      setMsg("");
    }
  }, [isInfo, svProblem]);
/*
  async function login(username, password) {
    setShowMessageSinging(true);
    setIsInfo(true);
    const res = Axios.post(
      managerURL.getAbsolutePath(urlDomain.token_obtain_pair),
      {
        headers: {
          "Content-Type": "text/plain",
        },
        username: `${username}`,
        password: `${password}`,
      }
    );
    res
      .then((data) => {
        if (data.status === 200) {
          updateTokens(data.data);
          setStatus(STATUS.loggedIn);
        }
      })
      .catch((error, b) => {
        if (error.response?.status === 401) {
          setIsInfo(false);
        } else if (error.response?.status === 400) {
          setIsInfo(false);
        } else {
          setIsInfo(false);
          setSvProblem(true);
        }
      });
  }*/

  return (
    <Grid textAlign="center" style={{ height: "100vh" }} verticalAlign="middle">
      <SignUp open={showSignUp} handleOpen={SetShowSignUp} />
      <Grid.Column style={{ maxWidth: 450 }}>
        <Header as="h2" color="teal" textAlign="center">
          <Image src={Logo} /> Log-in to your account
        </Header>
        <Form size="large">
          {showMessageSinging && (
            <Singing
              title={title}
              body={msg}
              isInfo={isInfo}
              isNegative={!isInfo}
            />
          )}
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
            
          </Segment>
        </Form>
        <Message>
          <Button onClick={() => SetShowSignUp(true)}>Crear cuenta</Button>
        </Message>
      </Grid.Column>
    </Grid>
  );
};

const Singing = ({ title, body, isInfo, isNegative }) => {
  return (
    <Message icon info={isInfo} negative={isNegative}>
      {!isNegative && <Icon name="circle notched" loading />}
      <Message.Content>
        <Message.Header>{title}</Message.Header>
        {body}
      </Message.Content>
    </Message>
  );
};

export default SignIn;
