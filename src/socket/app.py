from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow CORS for all origins

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@socketio.on('convert_temperature')
def handle_conversion(data):
    temp = data.get("temperature")
    scale = data.get("scale")

    if scale == "C":
        converted_temp = celsius_to_fahrenheit(temp)
        result = {"converted_temperature": converted_temp, "scale": "F"}
    elif scale == "F":
        converted_temp = fahrenheit_to_celsius(temp)
        result = {"converted_temperature": converted_temp, "scale": "C"}
    else:
        result = {"error": "Invalid scale"}

    emit('conversion_result', result)  # Send the result back to the client

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
