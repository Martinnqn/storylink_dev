import React from 'react';

const Profile = ({ match }) => (
    <>
        <div>Profile</div>
        <div>Profile</div>
        <div>Profile</div>
        <div>Profile</div>
        <div>Profile</div>
        <div>Profile</div>
        <div>Profile</div>
        <div>Profile</div>
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
)

export default Profile