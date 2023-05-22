import socket
import pickle

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 1234  # Porta para conexão

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print('Aguardando conexão do cliente...')

# Aceita a conexão do cliente
client_socket, addr = server_socket.accept()
print('Cliente conectado:', addr)

# Define a pergunta, as opções e a resposta correta
pergunta = "Qual é a capital do Brasil?"
opcoes = ["1 - Belém", "2 - Salvador", "3 - Brasília", "4 - Castanhal"]
resposta_correta = 3

# Envia a pergunta e as opções para o cliente
client_socket.send(pergunta.encode())
client_socket.send(pickle.dumps(opcoes))

# Recebe a resposta do cliente
resposta_cliente = int(client_socket.recv(1024).decode())

# Verifica se a resposta está correta
if resposta_cliente == resposta_correta:
    resultado = "Resposta correta!"
else:
    resultado = "Resposta incorreta!"

# Envia o resultado para o cliente
client_socket.send(resultado.encode())

# Fecha a conexão
client_socket.close()
server_socket.close()