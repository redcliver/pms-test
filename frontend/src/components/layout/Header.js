import React, { Component } from "react";

export class Header extends Component {
  render() {
    const navStyle = {
      boxShadow: " 0px 4px 7px -3px rgba(0, 0, 0, 0.8",
      borderBottom: "2px solid rgb(179, 48, 0)",
      backgroundColor: "#E95420"
    };
    return (
      <nav className="navbar navbar-expand-lg navbar-dark" style={navStyle}>
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarTogglerDemo03"
          aria-controls="navbarTogglerDemo03"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <a className="navbar-brand" href="#">
          <img
            style={{ maxHeight: "30px" }}
            src="https://www.seazone.com.br/images/logo.png"
          />
        </a>

        <div className="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul className="navbar-nav mr-auto mt-2 mt-lg-0"></ul>
        </div>
      </nav>
    );
  }
}

export default Header;
