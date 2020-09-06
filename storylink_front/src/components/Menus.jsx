import React, { useState } from 'react'
import logo from '../assets/story_minim.svg'
import SearchUser from './SearchUser'

import {
    Container,
    Icon,
    Menu,
    Sidebar,
    Dropdown,
    Image,
    Visibility,
    Transition,
    Sticky,
} from 'semantic-ui-react'

const DesktopMenu = () => {

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
        <Visibility onUpdate={updateCalculations}>
            <Transition visible={calculations.direction === "up"} animation='slide down' duration={300}>
                <Menu fixed='top' inverted>
                    <Container>
                        <Menu.Menu position='left'>
                            <Menu.Item as='a' header>
                                <Image size='mini' src={logo} />
                            </Menu.Item>
                            <Menu.Item as='a'>
                                <SearchUser at='d esktop'></SearchUser>
                            </Menu.Item>
                        </Menu.Menu>
                        <Menu.Item as='a'>Home</Menu.Item>
                        <Menu.Item as='a'>Home</Menu.Item>
                        <Menu.Menu position='right'>
                            <Dropdown item simple icon='settings' text='Configuracion'>
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
        </Visibility>
    )
}

const MobileMenu = ({ handleToggle }) => {

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
        <Visibility onUpdate={updateCalculations}>
            <Transition visible={calculations.direction === "up"} animation='slide down' duration={300}>
                <Menu fixed='top' inverted>
                    <Menu.Menu>
                        <Menu.Item as='a' header>
                            <Image size='mini' src={logo} />
                        </Menu.Item>
                        <Menu.Item as='a'>
                            <SearchUser />
                        </Menu.Item>
                    </Menu.Menu>
                </Menu>
            </Transition>
            <Transition visible={calculations.direction === "up"} duration={300}>
                <Sticky>
                    <Menu fixed='bottom' inverted animation='slide up'>
                        <Menu.Menu>
                            <Menu.Item onClick={handleToggle}>
                                <Icon name='home' />
                            </Menu.Item>
                            <Menu.Item onClick={handleToggle}>
                                <Icon name='sidebar' />
                            </Menu.Item>
                        </Menu.Menu>
                    </Menu>
                </Sticky>
            </Transition>
        </Visibility>
    )
}

const SidebarMobile = ({ handleSidebarHide, sidebarOpened }) => (
    <Sidebar
        as={Menu}
        animation='overlay'
        inverted
        onHide={handleSidebarHide}
        vertical
        visible={sidebarOpened}
        width='thin'
        icon='labeled'
        fluid
    >

        <Menu.Item as='a'>
            <Icon name='settings' />
        Configuracion
        </Menu.Item>
        <Menu.Item as='a'>Cerrar Sesion</Menu.Item>
    </Sidebar>
)

export { DesktopMenu, MobileMenu, SidebarMobile }