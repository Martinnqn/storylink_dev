import React from "react";
import { Link } from "react-router-dom";
import { Button, Grid, Header, Image, Message } from "semantic-ui-react";
import Logo from "../assets/story_minim.svg";
import { urls as urlDomain } from "./url/URLDomain";

const NotFoundPage = () => {
  return (
    <Grid textAlign="center" verticalAlign="middle">
      <Grid.Column style={{ maxWidth: 450 }}>
        <Header as="h2" color="teal" textAlign="center">
          <Image src={Logo} /> Lo sentimos, sitio no encontrado
        </Header>
        <Message>
          <Button as={Link} to={urlDomain.home}>
            Regresar al home
          </Button>
        </Message>
      </Grid.Column>
    </Grid>
  );
};

export default NotFoundPage;
