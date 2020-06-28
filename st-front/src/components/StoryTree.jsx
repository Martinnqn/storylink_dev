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
        res
        .json()
        .then(res => {setData(res); console.log(res)})
        .catch(err => setErrors(err));
    }

    const callFirstChapters = () => {
        fetchData();
    }

    /*useEffect(() => {
        fetchData();
    },[props.pubId]);*/

    var childNodes= null;
    if (data.childs != undefined && data.childs.length > 0){
        childNodes = data.childs.map((child, index) =>
            <StoryTree username={props.username}
            pubId={child.pubId}
            title={child.title}
            type='chapter' />
        );
    }

    return <>
    <li onClick={callFirstChapters}>
    {props.title}
    {{childNodes} && <ul>{childNodes}</ul>}
    </li>
    </>;

}

export default StoryTree;