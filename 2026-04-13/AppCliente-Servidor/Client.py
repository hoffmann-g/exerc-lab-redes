import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5081
TCP_PORT = 5082

with open('mensagem.txt', 'r') as arquivo:
    conteudo = arquivo.read().split(';')

print("1. Enviar via UDP")
print("2. Enviar via TCP")
escolha = input("Selecione uma opção: ")

if escolha == "1":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for frame in conteudo:
        sock.sendto(frame.encode("utf-8"), (UDP_IP, UDP_PORT))
        resposta, _ = sock.recvfrom(102400)
        print(f"Resposta do servidor: {resposta.decode('utf-8')}")
        time.sleep(1.0)
    sock.close()

elif escolha == "2":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((UDP_IP, TCP_PORT))
    for frame in conteudo:
        sock.send(frame.encode("utf-8"))
        resposta = sock.recv(102400)
        print(f"Resposta do servidor: {resposta.decode('utf-8')}")
        time.sleep(1.0)
    sock.close()

else:
    print("Opção inválida.")