import React, { useState, useEffect } from 'react';

function Pacman() {
    const [arrow, setArrow] = useState('');
    let powerPill = false;
    
    useEffect(()=>{
        document.addEventListener("keydown", (e) => {
            if(e.key === 'ArrowDown') {
              updateState(String.fromCharCode(8595));
            } else if(e.key === 'ArrowUp') {
              updateState(String.fromCharCode(8593))
            }
          }
    })
    
    return (
        <p>{arrow}</p>
        );
    
    
  
}

export default Pacman;
