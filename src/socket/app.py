import socket

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def handle_client(client_socket):
    try:
        # Receive data from the client (1024 bytes max)
        data = client_socket.recv(1024).decode()
        
        # Parse temperature and scale from received data
        temp, scale = data.split()
        temp = float(temp)
        
        # Perform the conversion
        if scale.upper() == "C":
            converted_temp = celsius_to_fahrenheit(temp)
            result = f"{converted_temp} F"
        elif scale.upper() == "F":
            converted_temp = fahrenheit_to_celsius(temp)
            result = f"{converted_temp} C"
        else:
            result = "Error: Invalid scale"
        
        # Send the result back to the client
        client_socket.send(result.encode())
    except Exception as e:
        client_socket.send(f"Error: {str(e)}".encode())
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 65432))  # Listen on all available interfaces
    server_socket.listen(5)  # Allow up to 5 simultaneous connections
    print("TCP Temperature Converter Server started, waiting for clients...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected by {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
