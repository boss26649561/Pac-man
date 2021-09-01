import "./Menu.css";
import pacman from "assets/pacman-menu.png"; // with import
import React, { useState } from "react";
import { Link } from "react-router-dom";
function Menu() {
  //State to know to show overlay menu or not
  const [config, setConfig] = useState(false);
  //State for mode
  const [mode, setMode] = useState("Default");
  return (
    <div className="App">
      <div className="header">
        <h1>Pac Man</h1>
      </div>
      <img src={pacman} alt="pacman" />
      <div className="buttons">
        <Link to="/game">
          <button>Start</button>
        </Link>
        <button>Config</button>
        <button>Exit</button>
      </div>
      <div className="footer">
        <h2>Year:2021 </h2>
        <h2>Course Code:3815ICT and 7805ICT</h2>
        <h2>Chun On Chan</h2>
        <h2>Guan-Tse Wu</h2>
        <h2>Sirawat Thiangthae</h2>
        <h2>Yan Li</h2>
      </div>
    </div>
  );
}

export default Menu;
