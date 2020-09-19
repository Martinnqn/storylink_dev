/** This file contain the Menus components for desktop and mobile screen. */

import React, { useState, useContext } from "react";
import { Link } from "react-router-dom";
import Logo from "../assets/story_minim.svg";
import FullLogo from "../assets/ostorylink_blank.png";
import SearchUser from "./SearchUser";
import imgUser from "../assets/img1.png";
import styled from "styled-components/macro";
import {
  Container,
  Dropdown,
  Grid,
  Header,
  Icon,
  Image,
  Item,
  Menu,
  Popup,
  Radio,
  Sticky,
  Transition,
  Visibility,
} from "semantic-ui-react";
import { urls as urlDomain } from "./url/URLDomain";
import { urls as urlUser } from "./url/URLUser";
import ManagerURL from "./url/ManagerURL";

import BaseContext from "../contexts/BaseContext";
import UserContext from "../contexts/UserContext";

const managerURL = new ManagerURL("http://localhost:3000/");

/**Menu for desktop screens */
const DesktopMenu = ({ logout }) => {
  const [calculations, setCalculations] = useState({
    direction: "up",
    height: 0,
    width: 0,
    topPassed: false,
    bottomPassed: false,
    pixelsPassed: 0,
    percentagePassed: 0,
    topVisible: false,
    bottomVisible: false,
    fits: false,
    passing: false,
    onScreen: false,
    offScreen: false,
  });

  const username = useContext(UserContext).username;
  const imgProfile = useContext(UserContext).imgProfile;

  const updateCalculations = (e, { calculations }) => {
    setCalculations(calculations);
  };

  return (
    username && (
      <Visibility onUpdate={updateCalculations}>
        <Transition
          visible={calculations.direction === "up"}
          animation="slide down"
          duration={300}
        >
          <Menu fixed="top" inverted>
            <Container style={{ height: 60 }}>
              <Menu.Menu position="left">
                <Menu.Item as={Link} to={urlDomain.home}>
                  <Image size="mini" src={Logo} />
                </Menu.Item>
                <Menu.Item>
                  <SearchUser at="desktop"></SearchUser>
                </Menu.Item>
              </Menu.Menu>
              <Menu.Menu icon="labeled">
                <Menu.Item as={Link} to={urlDomain.home}>
                  <Icon name="home" size="big" />
                </Menu.Item>
              </Menu.Menu>
              <Menu.Menu position="right">
                <Menu.Item
                  as={Link}
                  to={managerURL.getRelativePath(`${urlDomain.user_site}`, {
                    username: username,
                  })}
                >
                  <MenuItemImageProfile src={imgProfile} />
                  <Item.Header>{username}</Item.Header>
                </Menu.Item>
                <DesktopMenuItemCreate />
                <DesktopMenuItemSettings logout={logout} />
              </Menu.Menu>
            </Container>
          </Menu>
        </Transition>
      </Visibility>
    )
  );
};

/**Item for Create option in DesktopMenu */
const DesktopMenuItemCreate = () => {
  return (
    <Dropdown item icon="plus" text="">
      <Dropdown.Menu>
        <Dropdown.Header>Crear</Dropdown.Header>
        <Menu.Item as={Link} to={urlDomain.home}>
          <Icon name="sitemap" size="big" />
          <span>Storylink</span>
        </Menu.Item>
        <Dropdown.Divider />
        <Menu.Item as={Link} to={urlDomain.home}>
          <Icon name="group" size="big" />
          <span>Grupo</span>
        </Menu.Item>
      </Dropdown.Menu>
    </Dropdown>
  );
};

/**Item for Settings option in DesktopMenu */
const DesktopMenuItemSettings = ({ logout }) => {
  return (
    <Dropdown item simple icon="caret down" text="">
      <Dropdown.Menu>
        <Dropdown.Header>Configuración</Dropdown.Header>
        <Dropdown.Item>Perfil</Dropdown.Item>
        <Dropdown.Item>General</Dropdown.Item>
        <Dropdown.Divider />
        <Dropdown.Item>
          <Radio toggle label="Modo oscuro" />
        </Dropdown.Item>
        <Dropdown.Divider />
        <Dropdown.Item onClick={logout}>Cerrar sesión</Dropdown.Item>
      </Dropdown.Menu>
    </Dropdown>
  );
};

/**Menu for mobile screens */
const MobileMenu = () => {
  const username = useContext(UserContext).username;
  const imgProfile = useContext(UserContext).imgProfile;

  return (
    <Sticky>
      <Menu fixed="bottom" inverted widths={4}>
        <Menu.Item as={Link} to={urlDomain.settings}>
          <Icon name="sidebar" size="large" />
        </Menu.Item>
        <MobileMenuItemCreate />
        <Menu.Item as={Link} to={urlDomain.home}>
          <Icon name="home" size="large" />
        </Menu.Item>
        <Menu.Item
          as={Link}
          to={managerURL.getRelativePath(`${urlDomain.user_site}`, {
            username: username,
          })}
        >
          <MenuItemImageProfile src={imgProfile} />
        </Menu.Item>
      </Menu>
    </Sticky>
  );
};

/**Item for Create option in MobileMenu */
const MobileMenuItemCreate = () => {
  return (
    <Popup
      trigger={
        <Menu.Item>
          <Icon name="plus" size="large" />
        </Menu.Item>
      }
      flowing
      hoverable
      offset="0, 25px"
      position="top center"
    >
      <Header>Crear</Header>
      <Grid centered divided columns={2} relaxed>
        <Grid.Column textAlign="center">
          <Menu.Item as={Link} to="/">
            <Icon name="sitemap" size="big" />
            <br />
            <span>Storylink</span>
          </Menu.Item>
        </Grid.Column>
        <Grid.Column textAlign="center">
          <Menu.Item as={Link} to="/">
            <Icon name="group" size="big" />
            <br />
            <span>Grupo</span>
          </Menu.Item>
        </Grid.Column>
      </Grid>
    </Popup>
  );
};

/**Fixed top bar for mobile screen. This bar is hidden when scroll down occurs. */
const TopBarMobile = () => {
  const [calculations, setCalculations] = useState({
    direction: "up",
    height: 0,
    width: 0,
    topPassed: false,
    bottomPassed: false,
    pixelsPassed: 0,
    percentagePassed: 0,
    topVisible: false,
    bottomVisible: false,
    fits: false,
    passing: false,
    onScreen: false,
    offScreen: false,
  });

  const updateCalculations = (e, { calculations }) => {
    setCalculations(calculations);
  };

  return (
    <Visibility onUpdate={updateCalculations}>
      <Transition
        visible={calculations.direction === "up" || calculations.topVisible}
        animation="slide down"
        duration={300}
      >
        <Menu fixed="top" inverted>
          <Menu.Menu>
            <Menu.Item as="a" header>
              <Image size="small" src={FullLogo} />
            </Menu.Item>
            <Menu.Item as="a">
              <SearchUser />
            </Menu.Item>
          </Menu.Menu>
        </Menu>
      </Transition>
    </Visibility>
  );
};

/**Profile picture miniature for menus*/
const MenuItemImageProfile = styled(Item.Image).attrs((props) => ({
  circular: true,
  bordered: true,
  size: "mini",
}))`
  padding: 1px;
  background-color: white !important;
`;

export { DesktopMenu, MobileMenu, TopBarMobile };
