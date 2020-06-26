import React, { useState, useEffect } from 'react'
import ReactDOM from 'react-dom'
import StoryTree from '../components/StoryTree.jsx'

const StoryTreeMain = () => {
    const [username, setUsername] = useState('')
    const [pub, setPub] = useState('')
    const [initRoot, setInitRoot] = useState(null)

    useEffect(() => {
        if (pub!=''){
            setInitRoot(<StoryTree username={username} pubId={pub} type='story' />)
        }
    },[pub]);

    const loadFirstChapters = () => {
        const data = document.getElementById('view-tree-story').dataset;
        setPub(data.pubid);
        setUsername(data.username)
    }

    return <div><a id="view-tree-story" data-pubid='' data-username='' className="btn-menu-pub"
        href="javascript: void(0)" onClick={loadFirstChapters}>
        <span className="material-icons">account_tree</span>
        </a>
        {initRoot}
        </div>
}


const treeView = document.getElementById('tree-react'); 
if (treeView!=undefined){
    ReactDOM.render(
        <StoryTreeMain />,
        treeView
        );    
}
