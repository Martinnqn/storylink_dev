import React from 'react'
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
} from 'semantic-ui-react'

const DesktopMenu = ({ direction, updateCalculations }) => {
    console.log(direction)
    return (
        <Visibility onUpdate={updateCalculations}>
            <Transition visible={direction === "up"} animation='slide down' duration={300}>
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
        </Visibility>)
}

const MobileMenu = ({ handleToggle }) => (
    <Menu inverted pointing>
        <Menu.Item as='a' header>
            <Image size='mini' src={logo} />
        </Menu.Item>
        <Menu.Item as='a'>
            <SearchUser />
        </Menu.Item>
        <Menu.Item onClick={handleToggle} position='right'>
            <Icon name='sidebar' />
        </Menu.Item>
    </Menu>
)
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
    >
        <Menu.Item as='a' active>
            <Icon name='home' />
                    Home
                </Menu.Item>
        <Menu.Item as='a'>
            <Icon name='settings' />
        Configuracion
        </Menu.Item>
        <Menu.Item as='a'>Cerrar Sesion</Menu.Item>
    </Sidebar>
)

export { DesktopMenu, MobileMenu, SidebarMobile }