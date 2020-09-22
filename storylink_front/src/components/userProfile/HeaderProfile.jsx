import React from "react";
import {
  Container,
  Divider,
  Grid,
  GridColumn,
  Header,
  Image,
  Item,
  Menu,
  Popup,
  Radio,
  Segment,
  Sticky,
  Transition,
  Visibility,
} from "semantic-ui-react";
import styled from "styled-components/macro";
import MenuProfile from "./MenuProfile";

const HeaderProfile = ({ username, imgProfile, imgCover }) => {
  return (
    <GridHeader>
      <Grid.Row>
        <ColumnCover>
          <CoverPicture src={imgCover} />
        </ColumnCover>
      </Grid.Row>
      <Grid.Row>
        <OverlapProfilePicture src={imgProfile} />
      </Grid.Row>
      <Grid.Row>
        <Header as="h2" content={username} />
      </Grid.Row>
      <Divider />
      <Grid.Row>
        <MenuProfile />
      </Grid.Row>
    </GridHeader>
  );
};

const GridHeader = styled(Grid).attrs((props) => ({
  columns: 1,
  centered: true,
}))`
  &&& {
    background: rgb(246, 253, 255);
    background: linear-gradient(
      0deg,
      rgba(246, 253, 255, 1) 0%,
      rgba(255, 238, 207, 1) 100%
    );
    margin-top: -40px;
    height: 400px;
  }
`;

const ColumnCover = styled(Grid.Column).attrs((props) => ({}))`
  &&& {
    max-height: 325px;
    max-width: 750px;
    overflow: hidden;
  }
`;

const CoverPicture = styled(Image).attrs((props) => ({
  centered: true,
  rounded: true,
}))`
  &&& {
    width: 100%;
    height: 100%;
    background-color: white;
  }
`;

const OverlapProfilePicture = styled(Image).attrs((props) => ({
  circular: true,
  bordered: true,
  centered: true,
  size: "small",
}))`
  &&& {
    margin-top: -150px;
    min-height: 150px;
    min-width: 150px;
    padding: 1px;
    background-color: white;
  }
`;

export default HeaderProfile;
