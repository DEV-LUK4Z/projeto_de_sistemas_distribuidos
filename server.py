import socket

HOST = 'localhost'
PORT = 55552

print(f'HOST: {HOST}, PORT: {PORT}')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Servidor aguardando conexão com o cliente\n")

conect, address = server.accept()
print("Conectado a:", address, "\n")

while True:
    data = conect.recv(1024).decode()
    if not data:
        print("Conexão Encerrada!")
        conect.close()
        break
    conect.sendall(data.encode())