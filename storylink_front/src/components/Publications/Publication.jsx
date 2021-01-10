import React, { useState, useEffect } from "react";
import { Divider, Placeholder } from "semantic-ui-react";
import styled from "styled-components/macro";

const Story = ({ dataStory }) => {
  const { img_content_link, title, text_content, id } = dataStory;
  console.log(dataStory);
  return (
    <PublicationCard>
      <div>
        <ContrastHeader img={img_content_link}>
          <PublicationTitle>{title}</PublicationTitle>
        </ContrastHeader>
      </div>
      <PublicationBody>
        <PublicationContent>{text_content}</PublicationContent>
      </PublicationBody>
      <Footer></Footer>
    </PublicationCard>
  );
};

const PublicationCard = styled.div`
  background: white;
  width: 100%;
  max-height: 500px;
  border-radius: 15px;
  margin-bottom: 22px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.12);
  overflow: hidden;
`;

const ContrastHeader = styled.div`
  background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
    url(${(prop) => prop.img});
  background-size: cover;
  position: relative;
  width: 100%;
  height: 300px;
`;

const PublicationBody = styled.div`
  line-height: 20px;
  margin-top: 8px;
  margin-bottom: 8px;
`;

const PublicationTitle = styled.p`
  color: white;
  text-align: center;
  line-height: 20px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  font-size: 22px;
  margin-top: 8px;
  margin-bottom: 8px;
  position: absolute;
  bottom: 8px;
`;

const PublicationContent = styled.p`
  line-height: 20px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
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
  <PublicationCard>
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
  </PublicationCard>
);

export default Story;
