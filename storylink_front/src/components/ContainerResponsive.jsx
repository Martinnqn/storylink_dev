/* eslint-disable max-classes-per-file */
/* eslint-disable react/no-multi-comp */

import { createMedia } from '@artsy/fresnel'
import React, { useState, Children } from 'react'
import { DesktopMenu, MobileMenu, SidebarMobile } from './Menus'
import MenuItemSearchUser from './SearchUser'
import logo from '../assets/story_minim.svg'
import PropTypes from 'prop-types'

import {
    Container,
    Icon,
    Menu,
    Segment,
    Sidebar,
    Dropdown,
    Image,
    Visibility,
    Transition,
    Header,
    Button,
} from 'semantic-ui-react'

const { MediaContextProvider, Media } = createMedia({
    breakpoints: {
        mobile: 0,
        tablet: 768,
        computer: 1024,
    },
})

const ResponsiveContainer = ({ children }) => (
    <MediaContextProvider>
        <DesktopContainer>{children}</DesktopContainer>
        <MobileContainer>{children}</MobileContainer>
    </MediaContextProvider>
)

const DesktopContainer = ({ children }) => {

    const [calculations, setCalculations] = useState({
        direction: 'up',
        height: 0,
        width: 0,
        topPassed: false,
        bottomPassed: false,
        pixelsPassed: 0,
        percentagePassed: 0,
        topVisible: false,
        bottomVisible: false,
        fits: false,
        passing: false,
        onScreen: false,
        offScreen: false,
    });

    const updateCalculations = (e, { calculations }) => {
        setCalculations(calculations);
    }

    return (
        <Media greaterThan='mobile'>
            <DesktopMenu direction={calculations.direction} updateCalculations={updateCalculations} />
            {children}
        </Media>
    )
}

const MobileContainer = ({ children }) => {

    const [sidebarOpened, setSidebarOpened] = useState(false)

    const handleSidebarHide = () => setSidebarOpened(false)
    const handleToggle = () => setSidebarOpened(true)

    return (
        <Media as={Sidebar.Pushable} at='mobile'>
            <SidebarMobile handleSidebarHide={handleSidebarHide} sidebarOpened={sidebarOpened}></SidebarMobile>

            <Sidebar.Pusher dimmed={sidebarOpened}>
                <MobileMenu handleToggle={handleToggle} />
                {children}
            </Sidebar.Pusher>
        </Media >
    )
}

export default ResponsiveContainer
