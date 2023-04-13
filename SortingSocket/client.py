import socket
import pickle
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1025)) #here port number
msg=s.recv(1024)
print(msg.decode())
        
   

