import React, { useState } from 'react'
import {
    Menu,
    Input,
    Container
} from 'semantic-ui-react'

const SearchUser = ({ at }) => {
    const [loading, setLoading] = useState(false)
    const [isActive, setIsActive] = useState(false)

    return (
        <Menu.Item >
            <Input icon='search' iconPosition='left' placeholder='Buscar...' loading={loading} />
        </Menu.Item>
    )
}

export default SearchUser