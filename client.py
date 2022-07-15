import socket, threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

nickname = input("Choose your nickname: ")
print("Type DISCONNECT to exit")

client = socket.socket()
client.connect(ADDR)

def receive():
  while True:
    try:
      message = client.recv(1024).decode(FORMAT)
      if message == 'NICKNAME':
        client.send(nickname.encode(FORMAT))

      else:
        print(message)

    except:
      print("An error occured!")
      client.close()

def write():
  while True:
    message = '{}: {}'.format(nickname, input(''))
    client.send(message.encode(FORMAT))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start() 
