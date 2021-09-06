import React, { useState, useEffect } from "react";
import styled from "styled-components";
import Spritesheet from "react-responsive-spritesheet";
import Sprite from "assets/pSpriteSheet.png";
import pacman from "assets/pacman1.png";
import blinky from "assets/blinky.png";
import pinky from "assets/pinky.png";

const StyledBoard = styled.section`
  background-color: black;
  width: 32rem;
  height: 32rem;
  position: relative;
`;
const Pacman = styled.div`
  background-image: url(${pacman});
  width: 2rem;
  height: 2rem;
  left: ${({ x }) => x + "rem"};
  top: ${({ y }) => y + "rem"};
  position: absolute;
`;
const Blinky = styled.div`
  background-image: url(${blinky});
  width: 2rem;
  height: 2rem;
  left: ${({ x }) => x + "rem"};
  top: ${({ y }) => y + "rem"};
  position: absolute;
`;
const Pinky = styled.div`
  background-image: url(${pinky});
  width: 2rem;
  height: 2rem;
  left: ${({ x }) => x + "rem"};
  top: ${({ y }) => y + "rem"};
  position: absolute;
`;
function increment(x) {
  return x + 2;
}
function decrement(x) {
  return x - 2;
}
const actionXMap = {
  ArrowLeft: decrement,
  ArrowRight: increment,
};
const actionYMap = {
  ArrowDown: increment,
  ArrowUp: decrement,
};
const XMap = {
  0: decrement,
  1: increment,
};
const YMap = {
  2: increment,
  3: decrement,
};

function Board({}) {
  const [PacX, setX] = useState(0);
  const [PacY, setY] = useState(0);
  const [BlinkyX, setBX] = useState(14);
  const [BlinkyY, setBY] = useState(20);
  const [PinkyX, setPX] = useState(16);
  const [PinkyY, setPY] = useState(20);

  function handleKeyPress(e) {
    const actionX = actionXMap[e.key];
    const actionY = actionYMap[e.key];
    actionX && setX(actionX);
    actionY && setY(actionY);
  }

  function randomMove() {
    const BlinkyMove = Math.floor(Math.random() * 4);
    const PinkyMove = Math.floor(Math.random() * 4);
    if (BlinkyMove === 0 || BlinkyMove === 1) {
      const BlinkMoveX = XMap[BlinkyMove];
      BlinkMoveX && setBX(BlinkMoveX);
    }
    if (BlinkyMove === 2 || BlinkyMove === 3) {
      const BlinkMoveY = YMap[BlinkyMove];
      BlinkMoveY && setBY(BlinkMoveY);
    }
    if (PinkyMove === 0 || PinkyMove === 1) {
      const PinkMoveX = XMap[PinkyMove];
      PinkMoveX && setPX(PinkMoveX);
    }
    if (PinkyMove === 2 || PinkyMove === 3) {
      const PinkMoveY = YMap[PinkyMove];
      PinkMoveY && setPY(PinkMoveY);
    }
  }

  useEffect(() => {
    document.addEventListener("keydown", handleKeyPress);
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      randomMove();
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <StyledBoard onKeyPress={handleKeyPress}>
      <Pacman x={PacX} y={PacY}></Pacman>
      <Blinky x={BlinkyX} y={BlinkyY}></Blinky>
      <Pinky x={PinkyX} y={PinkyY}></Pinky>
    </StyledBoard>
  );
}

export default Board;
