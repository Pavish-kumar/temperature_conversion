import React, { useState } from 'react';
import './App.css'; 
function App() {
  const [celsius, setCelsius] = useState('');
  const [fahrenheit, setFahrenheit] = useState('');

  const convertToFahrenheit = (celsius) => {
    return (celsius * 9/5) + 32;
  };

  const convertToCelsius = (fahrenheit) => {
    return (fahrenheit - 32) * 5/9;
  };

  const handleCelsiusChange = (e) => {
    const value = e.target.value;
    setCelsius(value);
    if (value !== '') {
      setFahrenheit(convertToFahrenheit(value).toFixed(2));
    } else {
      setFahrenheit('');
    }
  };

  const handleFahrenheitChange = (e) => {
    const value = e.target.value;
    setFahrenheit(value);
    if (value !== '') {
      setCelsius(convertToCelsius(value).toFixed(2));
    } else {
      setCelsius('');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Temperature Converter</h1>
        <div className="converter-container">
          <div className="input-group">
            <label htmlFor="celsius">Celsius</label>
            <input
              id="celsius"
              type="number"
              value={celsius}
              onChange={handleCelsiusChange}
              placeholder="Enter °C"
            />
          </div>
          <div className="input-group">
            <label htmlFor="fahrenheit">Fahrenheit</label>
            <input
              id="fahrenheit"
              type="number"
              value={fahrenheit}
              onChange={handleFahrenheitChange}
              placeholder="Enter °F"
            />
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;