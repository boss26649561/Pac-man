import React from "react";
import Menu from "components/Menu/Menu";
import board from "components/board/board";
import { Route, Switch } from "react-router-dom";
function App() {
  return (
    <Switch>
      <Route exact path="/" component={Menu} />
      <Route path="/game" component={board} />
    </Switch>
  );
}

export default App;
