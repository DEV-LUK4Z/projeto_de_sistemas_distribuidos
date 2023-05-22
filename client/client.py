import socket
import pickle

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 50001  # Porta para conexão

# Cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("\nConectado ao servidor")

# Recebe a pergunta e as opções do servidor
pergunta = client_socket.recv(1024).decode()
opcoes = pickle.loads(client_socket.recv(1024))

# Exibe a pergunta e as opções para o usuário
print(pergunta)
for opcao in opcoes:
    print(opcao)

# Solicita ao usuário a resposta
resposta = int(input("\nDigite o número da opção correta >> "))
client_socket.send(str(resposta).encode())

# Recebe o resultado do servidor
resultado = client_socket.recv(1024).decode()

# Verifica se a resposta está incorreta e exibe a mensagem correspondente
if resultado == "Resposta incorreta!":
    print("\n",resultado)
else:
    print("\n",resultado)

# Fecha a conexão
client_socket.close()