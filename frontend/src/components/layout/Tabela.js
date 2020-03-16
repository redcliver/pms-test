import React, { Component } from "react";

export class Tabela extends Component {
  render() {
    return (
      <div>
        <ul className="list-group">
          <li className="list-group-item d-flex justify-content-between align-items-center">
            1 - Rua abcteste, 395
            <span className="badge badge-primary badge-pill">2</span>
          </li>
          <li className="list-group-item d-flex justify-content-between align-items-center">
            2 - Rua José da Silva, 563
            <span className="badge badge-primary badge-pill">2</span>
          </li>
          <li className="list-group-item d-flex justify-content-between align-items-center">
            3 - Rua João Pedro, 145
            <span className="badge badge-primary badge-pill">1</span>
          </li>
        </ul>
      </div>
    );
  }
}

export default Tabela;
