/* eslint-disable max-classes-per-file */
/* eslint-disable react/no-multi-comp */

import { createMedia } from '@artsy/fresnel'
import React from 'react'
import { DesktopMenu, MobileMenu, TopBarMobile } from './Menus'
import PropTypes from 'prop-types'

const { MediaContextProvider, Media } = createMedia({
    breakpoints: {
        mobile: 0,
        tablet: 768,
        computer: 1024,
    },
})

const ResponsiveMenu = () => (
    <MediaContextProvider>
        <DesktopContainer></DesktopContainer>
        <MobileContainer></MobileContainer>
    </MediaContextProvider>
)

const DesktopContainer = () => {

    return (
        <Media greaterThan='mobile'>
            <DesktopMenu />
        </Media>
    )
}

const MobileContainer = () => {

    return (
        <Media at='mobile'>
            <TopBarMobile />
            <MobileMenu />
        </Media >
    )
}

export default ResponsiveMenu
