import React from "react";
import { Label, Menu } from "semantic-ui-react";
import { Link } from "react-router-dom";
import { urls as urlDomain } from "../url/URLDomain";

const MenuProfile = ({}) => {
  return (
    <Menu position="center" secondary>
      <Menu.Item as={Link} to={urlDomain.home}>
        Perfil
      </Menu.Item>
      <Menu.Item as={Link} to={urlDomain.home}>
        Seguidos
      </Menu.Item>
      <Menu.Item as={Link} to={urlDomain.home}>
        Seguidores
      </Menu.Item>
      <Menu.Item as={Link} to={urlDomain.home}>
        Grupos
      </Menu.Item>
    </Menu>
  );
};

export default MenuProfile;
