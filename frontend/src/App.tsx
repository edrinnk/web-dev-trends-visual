import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  // test api
  // const [currentTime, setCurrentTime] = useState(0);
  // useEffect(() => {
  //   fetch('/time').then(response => response.json()).then(data => {
  //     setCurrentTime(data.time);
  //   })
  // }, []);

  const [exampleJson, setExampleJson] = useState(0);
  useEffect(() => {
    fetch('/exampleJson').then(response => response.json()).then(data => {
      // setExampleJson(data.response);
      setExampleJson(data);
    })
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        {/* test api */}
        {/* <p>The current time is: {currentTime}</p> */}

      </header>
    </div>
  );
}

export default App;
