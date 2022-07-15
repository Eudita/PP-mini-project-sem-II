import socket, threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
server = socket.socket()
server.bind(ADDR)
server.listen()

clients = []
nicknames = []

def broadcast(message):
  for client in clients:
    client.send(message)

def handle(client):
  while True:
    message = client.recv(1024)
    msg = message.decode(FORMAT)

    if msg != DISCONNECT_MESSAGE:
      broadcast(message)

    elif msg == DISCONNECT_MESSAGE:
      broadcast(f'{nickname} left the chat'.encode(FORMAT))
      index = clients.index(client)
      clients.remove(client)
      client.close()
      nickname = nicknames[index]
      nicknames.remove(nickname)
      break


def start():
  while True:
    client, address = server.accept()

    print(f"Connected with {format(str(address))}")
    client.send('NICKNAME'.encode(FORMAT))

    nickname = client.recv(1024).decode(FORMAT)
    nicknames.append(nickname)
    clients.append(client)

    print(f"Nickname is {format(nickname)}")
    
    broadcast(f"{format(nickname)} joined".encode(FORMAT))
    client.send('Connected to server!'.encode(FORMAT))

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()
start()
