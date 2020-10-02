import React, { useState, useEffect } from "react";
import { Placeholder } from "semantic-ui-react";
import styled from "styled-components/macro";

const Story = ({ dataStory, cantInCart }) => {
  const { photo, title, content, id } = dataStory;

  return (
    <CardPublication>
      <Img src={photo} alt={title} />
      <TitleProduct>{title}</TitleProduct>
      <Footer></Footer>
    </CardPublication>
  );
};

const CardPublication = styled.div`
  text-align: center;
  background: white;
  width: 100%;
  max-height: 500px;
  border-radius: 3px;
  margin-bottom: 22px;
`;

const Img = styled.img`
  width: 100%;
  height: 300px;
`;

const TitleProduct = styled.p`
  line-height: 20px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  font-size: 14px;
  margin-top: 8px;
  margin-bottom: 8px;
`;

const Footer = styled.div`
  display: flex;
  justify-content: space-around;
  align-items: baseline;
`;

/**
 * Product PlaceHolder.
 */
export const PlaceHolderStory = () => (
  <CardPublication>
    <Placeholder>
      <Placeholder.Header>
        <Placeholder.Image style={{ height: "200px" }} />
      </Placeholder.Header>
      <Placeholder.Paragraph>
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
        <Placeholder.Line length="full" />
      </Placeholder.Paragraph>
    </Placeholder>
  </CardPublication>
);

export default Story;
