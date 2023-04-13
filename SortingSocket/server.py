import socket
import pickle
a=10
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1025))
s.listen(5)
while True:
    clt,adr=s.accept()
    print(f"Connection to {adr} established")
    arr=[19,12,14,16,18,1,2,4,3]
    arr.sort()
    ser=pickle.dump(arr)
    clt.send(bytes(ser))