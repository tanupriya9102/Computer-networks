# import socket

# # create a socket object
# clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # connect the client socket to the server
# clientsocket.connect(('localhost', 8000))

# # send some data
# clientsocket.send(b'Hello, server!')

# # receive some data
# data = clientsocket.recv(1024)
# print(data)
import socket

# create a TCP client socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
clientsocket.connect(('localhost', 8888))

# receive the server's response
response = clientsocket.recv(1024).decode()
print(response)

# close the connection
clientsocket.close()
