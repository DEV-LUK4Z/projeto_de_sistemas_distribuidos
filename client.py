import socket

HOST = 'localhost'
PORT = 55552

print(f'HOST: {HOST}, PORT: {PORT}')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

mensagem = input("Enviar mensaem; ")
client.sendall(str.encode(mensagem))

data = client.recv(1024)
print("Mensagem ecoada do servidor: ", data.decode())