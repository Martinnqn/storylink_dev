/**
 * Enter here the user flows and custom policies for your B2C application
 * To learn more about user flows, visit: https://docs.microsoft.com/en-us/azure/active-directory-b2c/user-flow-overview
 * To learn more about custom policies, visit: https://docs.microsoft.com/en-us/azure/active-directory-b2c/custom-policy-overview
 */
const b2cPolicies = {
    names: {
        signUpSignIn: "B2C_1_reactjs_susin",
        forgotPassword: "",
        editProfile: ""
    },
    authorities: {
        signUpSignIn: {
            authority: "https://storylinkB2C.b2clogin.com/storylinkB2C.onmicrosoft.com/B2C_1_reactjs_susin",
        },
        forgotPassword: {
            authority: "https://storylinkB2C.b2clogin.com/storylinkB2C.onmicrosoft.com/b2c_1_reset",
        },
        editProfile: {
            authority: "https://storylinkB2C.b2clogin.com/storylinkB2C.onmicrosoft.com/b2c_1_edit_profile"
        }
    },
    authorityDomain: "storylinkB2C.b2clogin.com"
}

export default b2cPolicies;