import socket

HOST = 'localhost'
PORT = 55552

print(f'\nHOST: {HOST}\nPORT: {PORT}')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print("\nServidor aguardando conexão com o cliente")

client, address = server.accept()

while True:
    data = client.recv(1024).decode()
    if not data:
        print("\nConexão Encerrada!")
        client.close()
        break
    print(f'\nMensagem do cliente: {data}')
    client.sendall(data.encode())