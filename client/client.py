import socket

HOST = 'localhost'
PORT = 55552

print(f'\nHOST: {HOST}\nPORT: {PORT}')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("\nCONECTADO!\n")

mensagem = input("Enviar mensagem >> ")
client.sendall(str.encode(mensagem))

data = client.recv(1024)
print(f'\nMensagem ecoada do servidor: {data.decode()}')