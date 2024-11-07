from flask import Flask
from flask_socketio import SocketIO, emit
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('convert_temperature')
def handle_convert_temperature(data):
    print("Received conversion request:", data)
    try:
        temperature = float(data['temperature'])
        scale = data['scale'].upper()
        
        if scale == "C":
            converted_temp = celsius_to_fahrenheit(temperature)
            result = {"converted_temperature": converted_temp, "scale": "F"}
        elif scale == "F":
            converted_temp = fahrenheit_to_celsius(temperature)
            result = {"converted_temperature": converted_temp, "scale": "C"}
        else:
            result = {"error": "Invalid scale"}
        
        print("Sending conversion result:", result)
        emit('conversion_result', result)
    except Exception as e:
        emit('conversion_result', {"error": str(e)})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
