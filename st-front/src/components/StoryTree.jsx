import React, { useState, useEffect } from 'react';
import getCookie from './handleCookie';

const StoryTree = (props) => {

    const [hasError, setErrors] = useState(false);
    const [data, setData] = useState([]);
    const [pub, setPub] = useState('')

    async function fetchData() {
        var url = '';
        if ('story'==props.type){
            url = "/user/"+props.username+"/publication/continuations-titles/"+props.pubId;
        }else{
            url = "/user/"+props.username+"/publication/continuations-chapter-titles/"+props.pubId;
        }
        const res = await fetch(url, {method: "GET",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        credentials: 'same-origin',
    });
        console.log(res)
        res
        .json()
        .then(res => {setData(res); console.log(res)})
        .catch(err => setErrors(err));
    }

    const callFirstChapters = () => {
        console.log("ddsdasdas")
        if (props.pubId!=undefined){
            fetchData();
        }
    }

    useEffect(() => {
        if (props.pubId!=""){
        console.log("props.pubId")
        console.log(props.pubId)
        fetchData();
        }
    },[props.pubId]);

    var childNodes='';
    if (data.childs != undefined && data.childs.length > 0){
        childNodes = data.childs.map(function(child, index) {
            <li>
            <StoryTree username={this.props.username}
            pubId={child.pubId}
            type='chapter' />
            </li>
        });
        childNodes = <ul>childNodes</ul>
    }

    return <>
    <li onClick={callFirstChapters}>
    {data.title}
    </li>
    {childNodes}
    </>;

}

export default StoryTree;