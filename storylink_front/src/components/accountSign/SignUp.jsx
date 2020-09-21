import React, { useState } from "react";
import {
  Button,
  Form,
  Grid,
  Header,
  Segment,
  Image,
  Modal,
} from "semantic-ui-react";
import Logo from "../../assets/story_minim.svg";
import CustomAxios from "../http/CustomAxios";
import { urls as urlDomain } from "../url/URLDomain";

const SignUp = ({ open, handleOpen }) => {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [name, setName] = useState("");
  const [lastname, setLastname] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");

  return (
    <Modal
      closeIcon
      size="small"
      open={open}
      onClose={() => handleOpen(false)}
      closeOnDimmerClick={false}
      dimmer="blurring"
    >
      <Modal.Content>
        <Grid textAlign="center" verticalAlign="middle">
          <Grid.Column style={{ maxWidth: 450 }}>
            <Header as="h2" color="teal" textAlign="center">
              <Image src={Logo} /> Registrarse
            </Header>
            <Form size="large">
              <Segment stacked>
                <Form.Input
                  fluid
                  placeholder="Correo electrónico"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
                <Form.Input
                  fluid
                  placeholder="Nombre de usuario"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                />
                <Form.Input
                  fluid
                  placeholder="Nombre"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                />
                <Form.Input
                  fluid
                  placeholder="Apellido"
                  value={lastname}
                  onChange={(e) => setLastname(e.target.value)}
                />
                <Form.Input
                  fluid
                  icon="lock"
                  iconPosition="left"
                  placeholder="Constraseña"
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
                <Form.Input
                  fluid
                  icon="lock"
                  iconPosition="left"
                  placeholder="Confirmar constraseña"
                  type="password"
                  value={password2}
                  onChange={(e) => setPassword2(e.target.value)}
                />
                <Button color="teal" fluid size="large">
                  Crear cuenta
                </Button>
              </Segment>
            </Form>
          </Grid.Column>
        </Grid>
      </Modal.Content>
    </Modal>
  );
};

export default SignUp;
