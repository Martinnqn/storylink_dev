import React, { useContext } from "react";
import UserContext from "../../contexts/UserContext";
import HeaderProfile from "./HeaderProfile";

const Profile = ({ match }) => {
  const { username, imgProfile } = useContext(UserContext);
  return (
    <>
      <HeaderProfile
        username={username}
        imgProfile={imgProfile}
        imgCover={imgProfile}
      />
      <div>{match.params.username}</div>
      <div>{match.params.username}</div>
      <div>{match.params.username}</div>
      <div>{match.params.username}</div>
      <div>{match.params.username}</div>
      <div>{match.params.username}</div>
      <div>{match.params.username}</div>
      <div>{match.params.username}</div>
      <div>{match.params.username}</div>
    </>
  );
};

export default Profile;
