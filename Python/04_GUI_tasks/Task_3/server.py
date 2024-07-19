import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,8888)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'end'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[New Connection] {addr} is connected to the server")
    
    connected = True
    while connected:
        msg_length = conn.recv(64).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
        
            print(f"[{addr}] {msg}")
        
    
    conn.close()
    
def start():
    server.listen()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        
print('[STARTING] server is starting...')
start()
