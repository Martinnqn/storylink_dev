import React from "react";

export const ProfileData = ({graphData}) => {
    return (
        <div>
        <p>{graphData?.displayName}</p>
        <p>{graphData?.jobTitle}</p>
        <p>{/*graphData?.businessPhones[0]*/}</p>
        <p>{graphData?.mail}</p>
        <p>{graphData?.officeLocation}</p>
        </div>
    );
};

