import React, { Component } from 'react';

export class StoryTree extends Component {

    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: []
        };
    }

    componentDidMount() {
        fetch("/continuations-titles/{this.props.pk}")
        .then(res => res.json())
        .then(
            (result) => {
                this.setState({
                    isLoaded: true,
                    items: result.items
                });
            },
            (error) => {
                this.setState({
                    isLoaded: true,
                    error
                });
            }
            )
    }

    render() {
        const { error, isLoaded, items } = this.state;
        if (error) {
          return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
          return <div>Cargando...</div>;
      } else {
          return (
            <ul>
            {items.map(item => (
                <li key={item.name}>
                {item.name}
                </li>
                ))}
            </ul>
            );
      }
  }
}
