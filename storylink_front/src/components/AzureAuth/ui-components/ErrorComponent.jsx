import React, { useEffect, useState } from "react";

export const ErrorComponent = ({error}) => {
    return <h6>An Error Occurred: {error.errorCode}</h6>;
}