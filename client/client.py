import socket
import pickle
#import threading

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
        print("\nCONECTADO AO SERVIDOR!")
    except:
        return print("\nERRO DE CONEXÃO!")

    while True:
        try:
            pergunta = pickle.loads(client.recv(1024))
            if not pergunta:
                break
            else:
                resposta = input(pergunta + "\nEscolha uma opção >> ")
                client.send(resposta.encode())

                res_servidor = pickle.loads(client.recv(1024))
                print(res_servidor)
            
            # Enviar confirmação para avançar para a próxima pergunta
            client.send("confirmacao".encode())
        except EOFError:
            break

    client.close()
    print("\nQuizz Finalizado")

if __name__ == "__main__":
    main()