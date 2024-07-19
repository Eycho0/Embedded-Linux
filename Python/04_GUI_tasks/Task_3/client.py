import socket

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,8888)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'end'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length == b' ' * (64 - len(send_length))
    client.send(send_length)
    client.send(message)
m = 'k'
while m!= DISCONNECT_MESSAGE:
    m = input("enter the message : ")
    send(m)
    
