import React, { useState, useContext } from "react";
import styled from "styled-components/macro";
import Story, { PlaceHolderStory, Chapter } from "./Publication";
import useInfiniteScroll from "react-infinite-scroll-hook";
import _ from "lodash";
import CustomAxios from "../http/CustomAxios";
import { urls as urlDomain } from "../url/URLDomain";
import BaseContext from "../../contexts/BaseContext";
import { Divider, Segment } from "semantic-ui-react";

const StoriesList = () => {
  const [page, setPage] = useState(1);
  const [cantPage, setCantPage] = useState(2);
  const [stories, setStories] = useState([]);
  const [loading, setLoading] = useState(false);
  const managerURL = useContext(BaseContext).managerURL;

  /**Request Product endpoint and updates products list*/
  const getStories = () => {
    setLoading(true);
    const res = CustomAxios.get(
      managerURL.getAbsolutePath(urlDomain.stories_home)
    );
    res.then((res) => {
      setPage(page + 1);
      setLoading(false);
      setStories([...stories, ...res.data]);
    });
  };

  const infiniteRef = useInfiniteScroll({
    loading,
    hasNextPage: page < cantPage,
    onLoadMore: getStories,
    scrollContainer: "window",
  });

  return (
    <MainContainer>
      <ContainerStoriesList ref={infiniteRef}>
        {loading && _.times(6, (i) => <PlaceHolderStory key={i} />)}
        {stories.map((story) => {
          return (
            <>
              <Story key={story.id} dataStory={story} />
            </>
          );
        })}
      </ContainerStoriesList>
    </MainContainer>
  );
};

const ContainerStoriesList = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
`;

const MainContainer = styled.div`
  max-width: 970px;
  margin: auto;
`;

export default StoriesList;
