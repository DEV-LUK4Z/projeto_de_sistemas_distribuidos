import socket
import pickle
#import threading

def main():
    HOST = 'localhost'
    PORT = 7777

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("\nAguardando Conexão...")

    try:
        client, adrres = server.accept()
        print(f'\nCLIENTE CONECTADO: {adrres}')
    except:
        return print("\nERRO DE CONEXÃO!")

    perguntas = [
    ("Qual a capital do Brasil?", ["a) Brasília", "b) Castanhal", "c) Salvador", "d) Bélem"], "a"),
    ("Qual é a capital da França?", ["a) Londres", "b) Paris", "c) Berlim", "d) Roma"], "b"),
    ("Qual é a montanha mais alta do mundo?", ["a) Mont Blanc", "b) K2", "c) Everest", "d) Kilimanjaro"], "c"),
    ("Qual é o maior planeta do sistema solar?", ["a) Terra", "b) Júpiter", "c) Saturno", "d) Netuno"], "b")
    ]
        
    for pergunta, opcoes, resposta_correta in perguntas:
        # Enviando a pergunta ao cliente
        pergunta_enviada = "{0}\n{1}\n".format(pergunta, '\n'.join(opcoes))
        client.send(pickle.dumps(pergunta_enviada))

        # Recebendo a resposta e verificando se está correta
        res_cliente = client.recv(1024).decode().strip()
        if res_cliente.lower() == resposta_correta:
            print(f'Resposta correta: {res_cliente}')
            res_servidor = "\nRESPOSTA CORRETA!\n" + ("-"*30)
        else:
            print(f'Resposta errada: {res_cliente}')
            res_servidor = "\nRESPOSTA INCORRETA!\n" + ("-"*50)

        # Enviando o resultado ao cliente
        client.send(pickle.dumps(res_servidor))

        # Aguardar confirmação do cliente para avançar para a próxima pergunta
        confirmacao = client.recv(1024).decode().strip()

    client.close()
    print("\nQuiz finalizado.")

if __name__ == "__main__":
    main()