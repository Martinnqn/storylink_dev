import React, { useState, useEffect } from 'react'
import ReactDOM from 'react-dom'
import StoryTree from '../components/StoryTree.jsx'

const StoryTreeMain = () => {
    const [username, setUsername] = useState('')
    const [pub, setPub] = useState('')
    const [title, setTitle] = useState('')
    
    const loadFirstChapters = () => {
        const title = document.getElementById('title-pub-detail').textContent;
        setTitle(title);
        const data = document.getElementById('view-tree-story').dataset;
        setPub(data.pubid);
        setUsername(data.username)
    }

    const tree = (pub!='') ? <ul><StoryTree username={username} pubId={pub} type='story' title={title}/></ul> : null;

    return <div><a id="view-tree-story" data-pubid='' data-username='' className="btn-menu-pub"
    href="javascript: void(0)" onClick={loadFirstChapters}>
    <span className="material-icons">account_tree</span>
    </a>
    {tree}
    </div>
}


const treeView = document.getElementById('tree-react'); 
if (treeView!=undefined){
    ReactDOM.render(
        <StoryTreeMain />,
        treeView
        );    

}
const asd = document.getElementById('content-filter'); 

ReactDOM.render(
    <ol>
  <li>Remove the skin from the garlic, and chop coarsely.</li>
  <li>Remove all the seeds and stalk from the pepper, and chop coarsely.</li>
  <li>Add all the ingredients into a food processor.</li>
  <li>Process all the ingredients into a paste.
    <ul>
      <li>If you want a coarse "chunky" hummus, process it for a short time.</li>
      <li>If you want a smooth hummus, process it for a longer time.</li>
    </ul>
  </li>
</ol>,
    asd
    );