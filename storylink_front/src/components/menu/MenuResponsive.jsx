/* eslint-disable max-classes-per-file */
/* eslint-disable react/no-multi-comp */

import { createMedia } from "@artsy/fresnel";
import React from "react";
import { DesktopMenu, MobileMenu } from "./Menus";

const { MediaContextProvider, Media } = createMedia({
  breakpoints: {
    mobile: 0,
    tablet: 768,
    computer: 1024,
  },
});

const ResponsiveMenu = () => (
  <MediaContextProvider>
    <Media greaterThan="mobile">
      <DesktopMenu />
    </Media>
    <Media at="mobile">
      <MobileMenu />
    </Media>
  </MediaContextProvider>
);

export default ResponsiveMenu;
