import React, { Component } from "react";
import { FaSearchPlus } from "react-icons/fa";

export class Lista extends Component {
  render() {
    const btnStyle = {
      backgroundColor: "#E95420",
      borderColor: "rgb(179, 48, 0)"
    };
    return (
      <div>
        <h5>Lista de imóveis</h5>
        <button
          type="button"
          className="btn btn-primary marginBotton20"
          data-toggle="modal"
          data-target="#exampleModal"
          style={btnStyle}
        >
          Imóvel &nbsp;
          <FaSearchPlus />
        </button>
        <ul className="list-group"></ul>
        <div
          className="modal fade"
          id="exampleModal"
          tabIndex="-1"
          role="dialog"
          aria-labelledby="exampleModalLabel"
          aria-hidden="true"
        >
          <div className="modal-dialog" role="document">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title" id="exampleModalLabel">
                  Novo Imóvel
                </h5>
                <button
                  type="button"
                  className="close"
                  data-dismiss="modal"
                  aria-label="Close"
                >
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div className="modal-body">...</div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  data-dismiss="modal"
                >
                  Fechar
                </button>
                <button
                  type="button"
                  className="btn btn-primary"
                  style={btnStyle}
                >
                  Adicionar
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Lista;
