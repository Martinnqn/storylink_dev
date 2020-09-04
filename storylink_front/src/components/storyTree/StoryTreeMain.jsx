import React, { useState, useEffect } from 'react'
import StoryTree from './StoryTree.jsx'

const StoryTreeMain = () => {
    const [username, setUsername] = useState('')
    const [pub, setPub] = useState('')
    const [title, setTitle] = useState('')
    const [isShowed, setIsShowed] = useState(false)

    const show = () => {
        setIsShowed(true);
        const data = document.getElementById('view-tree-story').dataset;
        setPub(data.pubid);
    }

    const hideIndexTree = () => {
        setIsShowed(false);
    }

    useEffect(() => {
        const title = document.getElementById('title-pub-detail').textContent;
        setTitle(title);
        const data = document.getElementById('view-tree-story').dataset;
        setPub(data.pubid);
        setUsername(data.username);
    }, [pub]);


    const tree = (pub != '') ? <ul><StoryTree username={username} pubId={pub} type='story' title={title} /></ul> : null;

    const classD = (isShowed) ? '' : 'hided-menu-pub';

    return <div><a id="view-tree-story" data-pubid='' data-username='' className="btn-menu-pub"
        href="javascript: void(0)" onClick={show}>
        <span className="material-icons">account_tree</span>
    </a>
        <div className={"container " + classD} id="index-tree">
            <a id="close-index-tree" className="" href="javascript: void(0)" onClick={hideIndexTree}>
                <span className="material-icons">highlight_off</span>
            </a>
            {tree}
        </div>
    </div>
}

export default StoryTreeMain;
