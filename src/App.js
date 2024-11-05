import React, { useState, useEffect } from 'react';
import { io } from 'socket.io-client';
import './App.css';
const socket = io("http://127.0.0.1:5000");
const App = () => {
    const [temperature, setTemperature] = useState('');
    const [scale, setScale] = useState('C');
    const [convertedTemperature, setConvertedTemperature] = useState(null);

    useEffect(() => {
        // Listen for the conversion result from the server
        socket.on('conversion_result', (data) => {
            setConvertedTemperature(data.converted_temperature + " " + data.scale);
        });

        // Cleanup the event listener on component unmount
        return () => {
            socket.off('conversion_result');
        };
    }, []);

    const handleConvert = () => {
        socket.emit('convert_temperature', {
            temperature: parseFloat(temperature),
            scale: scale
        });
    };

    return (
        <div>
            <h1>Temperature Converter</h1>
            <input
                type="number"
                value={temperature}
                onChange={(e) => setTemperature(e.target.value)}
                placeholder="Enter temperature"
            />
            <select value={scale} onChange={(e) => setScale(e.target.value)}>
                <option value="C">Celsius</option>
                <option value="F">Fahrenheit</option>
            </select>
            <button onClick={handleConvert}>Convert</button>

            {convertedTemperature && (
                <h2>Converted Temperature: {convertedTemperature}</h2>
            )}
        </div>
    );
};

export default App;
