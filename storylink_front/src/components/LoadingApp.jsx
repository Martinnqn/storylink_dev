import React from "react";
import ReactDOM from "react-dom";
import {
  Button,
  Form,
  Grid,
  Header,
  Segment,
  Image,
  Message,
  Dimmer,
  Loader,
  Container,
} from "semantic-ui-react";
import Logo from "../assets/story_minim.svg";
import styled from "styled-components/macro";

const LoadingApp = () => (
  <GridLoader textAlign="center" verticalAlign="middle">
    <Grid.Column>
      <Image src={Logo} centered size="tiny" />
    </Grid.Column>
  </GridLoader>
);

const GridLoader = styled(Grid)`
  height: 100vh;
`;

export default LoadingApp;
