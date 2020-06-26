import React from 'react';

export const TitleTree = () => {

    const callSubTitle = (id) => {
        fetch("http://127.0.0.1:8000/user/{this.props.username}/publication/continuations-titles/"+id)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            items: result.items
          });
        },
        // Nota: es importante manejar errores aquí y no en 
        // un bloque catch() para que no interceptemos errores
        // de errores reales en los componentes.
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
    }

    render() {
        return (
            <li className="title-tree">
            <a href="javascript:void(0)" onclick={() => callSubTitle({this.props.id})}>{this.props.title}</a>
            </li>
        );
    }
}
