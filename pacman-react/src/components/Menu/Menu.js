import "./Menu.css";
import pacman from "assets/pacman-menu.png"; // with import
import React, { useState } from "react";
import { Link } from "react-router-dom";
function App() {
  //State to know to show overlay menu or not
  const [config, setConfig] = useState(false);
  //State for mode
  const [mode, setMode] = useState("Default");
  return (
    <div className="App">
      <img src={pacman} alt="pacman" />
      <div className="buttons">
        <Link to="/game">
          <button>Start</button>
        </Link>
        <button>Config</button>
        <button>Exit</button>
      </div>
      <h2>test</h2>
    </div>
  );
}

export default App;
