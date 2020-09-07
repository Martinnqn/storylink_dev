import React, { useState } from 'react'
import Logo from '../assets/story_minim.svg'
import LogoCompleto from '../assets/ostorylink_blank.png'
import SearchUser from './SearchUser'
import imgUser from '../assets/img1.png'
import {
    Button,
    Container,
    Dropdown,
    Grid,
    Header,
    Icon,
    Image,
    Item,
    Menu,
    Popup,
    Radio,
    Sidebar,
    Sticky,
    Transition,
    Visibility,
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
                    <Container style={{ height: 60 }} >
                        <Menu.Menu position='left'>
                            <Menu.Item as={Link} to='/'>
                                <Image size='mini' src={Logo} />
                            </Menu.Item>
                            <Menu.Item>
                                <SearchUser at='desktop'></SearchUser>
                            </Menu.Item>
                        </Menu.Menu>
                        <Menu.Menu icon='labeled'>
                            <Menu.Item as={Link} to='/'>
                                <Icon name='home' size='big' />
                            </Menu.Item>
                        </Menu.Menu>
                        <Menu.Menu position='right'>
                            <Menu.Item as={Link} to='/user/Username'>
                                <Item.Image size='mini' src={imgUser} />
                                <Item.Header>Username</Item.Header>
                            </Menu.Item>
                            <Dropdown item icon='plus' text=''>
                                <Dropdown.Menu>
                                    <Dropdown.Header>Crear</Dropdown.Header>
                                    <Menu.Item as={Link} to='/'>
                                        <Icon name='sitemap' size='big' />
                                        Storylink
                                    </Menu.Item>
                                    <Dropdown.Divider />
                                    <Menu.Item as={Link} to='/'>
                                        <Icon name='group' size='big' />
                                        Grupo
                                    </Menu.Item>
                                </Dropdown.Menu>
                            </Dropdown>
                            <Dropdown item simple icon='caret down' text=''>
                                <Dropdown.Menu>
                                    <Dropdown.Header>Configuración</Dropdown.Header>
                                    <Dropdown.Item>Perfil</Dropdown.Item>
                                    <Dropdown.Item>General</Dropdown.Item>
                                    <Dropdown.Divider />
                                    <Dropdown.Item>
                                        <Radio toggle label='Modo oscuro' />
                                    </Dropdown.Item>
                                    <Dropdown.Divider />
                                    <Dropdown.Item>Cerrar sesión</Dropdown.Item>
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

    const handleItemPlus = () => {

    }

    return (
        <Sticky>
            <Menu fixed='bottom' inverted widths={4}>
                <Menu.Item as={Link} to='/settings'>
                    <Icon name='sidebar' size='large' />
                </Menu.Item>
                <Popup trigger={<Menu.Item ><Icon name='plus' size='large' />
                </Menu.Item>}
                    flowing hoverable offset='0, 25px' position='top center'>
                    <Header>Crear</Header>
                    <Grid centered divided columns={2} relaxed>
                        <Grid.Column textAlign='center'>
                            <Menu.Item as={Link} to='/'>
                                <Icon name='sitemap' size='big' />
                                <br />
                                Storylink
                            </Menu.Item>
                        </Grid.Column>
                        <Grid.Column textAlign='center'>
                            <Menu.Item as={Link} to='/' >
                                <Icon name='group' size='big' />
                                <br />
                                Grupo
                            </Menu.Item>
                        </Grid.Column>
                    </Grid>
                </Popup>
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
                            <Image size='small' src={LogoCompleto} />
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