/* eslint-disable max-classes-per-file */
/* eslint-disable react/no-multi-comp */

import { createMedia } from '@artsy/fresnel'
import React, { useState, Children } from 'react'
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

const ResponsiveMenu = ({ children }) => (
    <MediaContextProvider>
        <MenuTop />
        <MobileContainer>{children}</MobileContainer>
    </MediaContextProvider>
)

const MenuTop = () => {

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
            <Visibility onUpdate={updateCalculations}>
            </Visibility>
            <Transition visible={calculations.direction === "up"} animation='slide down' duration={300}>
                <Menu fixed='top' inverted>
                    <Container>
                        <Menu.Menu position='left'>
                            <Menu.Item as='a' header>
                                <Image size='mini' src={logo} />
                            </Menu.Item>
                        </Menu.Menu>
                        <Menu.Item as='a'>Home</Menu.Item>
                        <Menu.Item as='a'>Home</Menu.Item>
                        <Menu.Menu position='right'>
                            <Dropdown item simple text='Configuracion'>
                                <Dropdown.Menu>
                                    <Dropdown.Item>List Item</Dropdown.Item>
                                    <Dropdown.Item>List Item</Dropdown.Item>
                                    <Dropdown.Divider />
                                    <Dropdown.Header>Header Item</Dropdown.Header>
                                    <Dropdown.Item>
                                        <i className='dropdown icon' />
                                        <span className='text'>Submenu</span>
                                        <Dropdown.Menu>
                                            <Dropdown.Item>List Item</Dropdown.Item>
                                            <Dropdown.Item>List Item</Dropdown.Item>
                                        </Dropdown.Menu>
                                    </Dropdown.Item>
                                    <Dropdown.Item>List Item</Dropdown.Item>
                                </Dropdown.Menu>
                            </Dropdown>
                        </Menu.Menu>
                    </Container>
                </Menu>
            </Transition>
        </Media>
    )
}

const MobileContainer = ({ children }) => {

    const [sidebarOpened, setSidebarOpened] = useState(false)

    const handleSidebarHide = () => setSidebarOpened(false)
    const handleToggle = () => setSidebarOpened(true)
    const a = window.outerHeight
    return (
        <Media as={Sidebar.Pushable} at='mobile'>

            <Sidebar.Pusher dimmed={sidebarOpened}>
                <Segment
                    inverted
                    textAlign='center'
                    style={{ padding: '1em 0em' }}
                    vertical
                >
                    <Container>
                        <Menu inverted pointing secondary size='large'>
                            <Menu.Item onClick={handleToggle}>
                                <Icon name='sidebar' />
                            </Menu.Item>
                        </Menu>
                    </Container>
                </Segment>
            </Sidebar.Pusher>
            <Sidebar
                as={Menu}
                animation='overlay'
                inverted
                onHide={handleSidebarHide}
                vertical
                visible={sidebarOpened}
                style={{ position: 'absolute', top: 0, left: -50 }}
            >
                <Menu.Item as='a' active>
                    Home
                    </Menu.Item>
                <Menu.Item as='a'>Work</Menu.Item>
                <Menu.Item as='a'>Log in</Menu.Item>
                <Menu.Item as='a'>Sign Up</Menu.Item>
            </Sidebar>
        </Media>
    )
}

export default ResponsiveMenu
