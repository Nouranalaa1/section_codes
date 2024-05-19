#Server
import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine name
    host = socket.gethostname()
    port = 9999
    
    # Bind to the port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections
    server_socket.listen(5)
    
    print(f"Server started at {host} on port {port}. Waiting for connection...")
    
    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        
        print(f"Got a connection from {addr}")
        
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {data}")
        
        # Send a thank you message to the client
        response = "Thank you for connecting"
        client_socket.send(response.encode('utf-8'))
        
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()

#Client
import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine name
    host = socket.gethostname()
    port = 9999
    
    # Connection to hostname on the port
    client_socket.connect((host, port))
    
    # Send a message to the server
    message = "Hello, Server!"
    client_socket.send(message.encode('utf-8'))
    
    # Receive data from the server
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {data}")
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()

 
