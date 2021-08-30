import "./App.css";
import React, { useState } from "react";
import Menu from "components/Menu/Menu";
import Game from "components/Game/Game";
import { BrowserRouter, Route, Switch } from "react-router-dom";
function App() {
  return (
    <Switch>
      <Route exact path="/" component={Menu} />
      <Route path="/game" component={Game} />
    </Switch>
  );
}

export default App;
