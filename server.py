import socket
import datetime

# create a TCP server socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific port
serversocket.bind(('localhost', 8888))

# listen for incoming connections
serversocket.listen(1)
print('Server listening on port 8888...')

while True:
    # accept incoming connections
    (clientsocket, address) = serversocket.accept()
    print(f"Connection established from {address}")

    # get the current date, time, and day of the week
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    day = now.strftime("%A")

    # send the date, time, and day of the week to the client
    message = f"Today is {day}, {date} and the time is {time}"
    clientsocket.send(message.encode())

    # close the connection
    clientsocket.close()
