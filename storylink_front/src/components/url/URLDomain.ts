//import { include } from 'named-urls'
import { urls as urlUser } from "./URLUser";

export const urls = {
  home: "/",
  hall_s: "success/:success",
  hall_a: "activated/:activated",
  admin_site: "admin/site/",
  user_site: urlUser,
  social_site: "social/",
  auth: "accounts/",
  custom_login: "accounts/login/",
  sign_up: "signup/",
  term_priv: "terminos_privacidad/",
  form_new_mail: "re_email",
  form_new_username: "re_username",
  fill_profile: "fillprofile/:uidb64",
  fill_profile_verified: "fillprofile/:uidb64/:email_verified",
  activate: "activate/:uidb64/:token",
  settings: "settings/", //just for react router. For see settings menu.
  token_obtain_pair: "token/",
  token_refresh: "token/refresh/",
  token_verify: "token/verify/",
  whoami: "whoami/",
};
