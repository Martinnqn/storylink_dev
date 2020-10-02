import React, { useState } from "react";
import styled from "styled-components/macro";
import Story, { PlaceHolderStory, Chapter } from "./Publication";
import useInfiniteScroll from "react-infinite-scroll-hook";
import _ from "lodash";

const StoriesList = () => {
  const [page, setPage] = useState(1);
  const [cantPage, setCantPage] = useState(2);
  const [stories, setStories] = useState([]);
  const [loading, setLoading] = useState(false);

  /**Request Product endpoint and updates products list*/
  /*const fetchMoreData = () => {
    setLoading(true);
    fetch(`${URL_API}?page=${page}`)
      .then((res) => res.json())
      .then((res) => {
        setPage(page + 1);
        setLoading(false);
        if (res.page_count) {
          setCantPage(res.page_count);
        }
        setProducts([...products, ...res.products]);
      });
  };

  const infiniteRef = useInfiniteScroll({
    loading,
    hasNextPage: page <= cantPage,
    onLoadMore: fetchMoreData,
    scrollContainer: "window",
  });*/

  return (
    <MainContainer>
      <ContainerStoriesList>
        {_.times(6, (i) => (
          <PlaceHolderStory key={i} />
        ))}
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
