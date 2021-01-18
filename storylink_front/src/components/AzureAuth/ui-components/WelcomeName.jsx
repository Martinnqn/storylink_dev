import { useEffect, useState } from "react";
import { useMsal } from "@azure/msal-react";
import React from "react";

const WelcomeName = () => {
    const { accounts } = useMsal();
    const [name, setName] = useState(null);

    useEffect(() => {
        if (accounts.length > 0) {
            setName(accounts[0].username);
        }
    }, [accounts]);

    if (name) {
        return <h6>Welcome, {name}</h6>;
    } else {
        return null;
    }
};

export default WelcomeName;