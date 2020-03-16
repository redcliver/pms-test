import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import {
  Inject,
  ScheduleComponent,
  Day,
  Week,
  WorkWeek,
  Month,
  Agenda,
  EventSettingsModel
} from "@syncfusion/ej2-react-schedule";
import { DataManager, WebApiAdaptor } from "@syncfusion/ej2-data";

import "./styles/material.css";
import "./styles/bootstrap.css";

import Header from "./layout/Header";
import Dashboard from "./layout/Dashboard";
import Form from "./layout/Form";
import Lista from "./layout/Lista";
import Tabela from "./layout/Tabela";

import fundo from "./images/fundo.jpg";

class App extends Component {
  remoteData = new DataManager({
    url: "https://js.syncfusion.com/demos/ejservices/api/Schedule/LoadData",
    adaptor: new WebApiAdaptor(),
    crossDomain: true
  });
  render() {
    const marginMain = {
      marginTop: "3vh"
    };

    const scheduleStyle = {
      color: "#E95420"
    };
    return (
      <div
        id="principal"
        style={{ backgroundImage: "url('./images/fundo.jpg')" }}
      >
        <Fragment>
          <Header />
          <div className="container">
            <div className="row">
              <div className="col-md-2 col-sm-12" style={marginMain}>
                <Lista />
                <br />
                <Tabela />
              </div>
              <div className="col-md-10 col-sm-12" style={marginMain}>
                <ScheduleComponent currentView="Month" style={scheduleStyle}>
                  <Inject services={[Day, Week, WorkWeek, Month, Agenda]} />
                </ScheduleComponent>
              </div>
            </div>
          </div>
        </Fragment>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
