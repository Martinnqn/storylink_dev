import ReactDOM from 'react-dom'
import React from 'react'
import 'semantic-ui-css/semantic.min.css'
import Root from '../components/Root.jsx'


const root = document.getElementById('root');
if (root != undefined) {
  ReactDOM.render(
    <Root />,
    root
  );
}

/*
import StoryTreeMain from '../components/storyTree/StoryTreeMain.jsx'

const treeView = document.getElementById('tree-react');
if (treeView != undefined) {
  ReactDOM.render(
    <StoryTreeMain />,
    treeView
  );
}
*/