import socket

# specify the IP address and port number for the server socket
IP_ADDRESS = socket.gethostname()
PORT = 12345

# create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server's IP address and port number
client_socket.connect((IP_ADDRESS, PORT))

# send a stream of integers to the server
integers = [4, 2, 6, 1, 3]
integer_bytes = " ".join(str(i) for i in integers).encode()
client_socket.send(integer_bytes)

# receive the sorted list of integers from the server
data = client_socket.recv(1024)
sorted_integers = [int(i) for i in data.decode().split()]

# print the sorted list of integers
print(f"Sorted integers: {sorted_integers}")

# close the connection
client_socket.close()
