import socket

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode()
        temp, scale = data.split()
        temp = float(temp)
        if scale.upper() == "C":
            converted_temp = celsius_to_fahrenheit(temp)
            result = f"{converted_temp} F"
        elif scale.upper() == "F":
            converted_temp = fahrenheit_to_celsius(temp)
            result = f"{converted_temp} C"
        else:
            result = "Error: Invalid scale"
        client_socket.send(result.encode())
    except Exception as e:
        client_socket.send(f"Error: {str(e)}".encode())
    finally:
        client_socket.close()
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 65432))  
    server_socket.listen(5)
    print("TCP Temperature Converter Server started, waiting for clients...")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected by {addr}")
        handle_client(client_socket)
if __name__ == "__main__":
    start_server()
