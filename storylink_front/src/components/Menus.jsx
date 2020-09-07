import React, { useState } from 'react'
import logo from '../assets/story_minim.svg'
import SearchUser from './SearchUser'
import imgUser from '../assets/img1.png'
import {
    Container,
    Icon,
    Item,
    Menu,
    Sidebar,
    Dropdown,
    Image,
    Visibility,
    Transition,
    Sticky,
} from 'semantic-ui-react'

import {
    Link,
} from "react-router-dom"


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
                            <Menu.Item as={Link} to='/home'>
                                <Image size='mini' src={logo} />
                            </Menu.Item>
                            <Menu.Item>
                                <SearchUser at='desktop'></SearchUser>
                            </Menu.Item>
                        </Menu.Menu>
                        <Menu.Item as={Link} to='/'>Home</Menu.Item>
                        <Menu.Menu position='right'>
                            <Menu.Item as={Link} to='/user/Username'>
                                <Item.Header>Username</Item.Header>
                                <Item.Image size='mini' src={imgUser} />
                            </Menu.Item>
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

const MobileMenu = () => {
    return (
        <Sticky>
            <Menu fixed='bottom' inverted widths={4}>

                <Menu.Item as={Link} to='/settings'>
                    <Icon name='sidebar' size='large' />
                </Menu.Item>
                <Menu.Item as={Link} to='/'>
                    <Icon name='home' size='large' />
                </Menu.Item>
                <Menu.Item as={Link} to='/user/UsernameMobile'>
                    <Item.Image size='mini' src={imgUser} />
                </Menu.Item>
            </Menu>
        </Sticky>
    )
}

const TopBarMobile = () => {

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
            <Transition visible={calculations.direction === "up" || calculations.topVisible}
                animation='slide down' duration={300}>
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

export { DesktopMenu, MobileMenu, TopBarMobile }