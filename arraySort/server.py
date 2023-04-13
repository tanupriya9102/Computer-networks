import socket

# specify the IP address and port number for the server socket
IP_ADDRESS = socket.gethostname()
PORT = 12345

# create a TCP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the IP address and port number
server_socket.bind((IP_ADDRESS, PORT))

# listen for incoming connections
server_socket.listen()

print(f"Server is listening on {IP_ADDRESS}:{PORT}")

# accept incoming connections
while True:
    client_socket, address = server_socket.accept()
    print(f"Received connection from {address}")

    # receive the stream of integers from the client
    data = client_socket.recv(1024)
    integers = [int(i) for i in data.decode().split()]

    # sort the list of integers
    sorted_integers = sorted(integers)

    # send the sorted list of integers back to the client
    sorted_integers_bytes = " ".join(str(i) for i in sorted_integers).encode()
    client_socket.send(sorted_integers_bytes)

    # close the connection
    client_socket.close()
