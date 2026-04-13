import socket
import threading

UDP_IP = "127.0.0.1"
UDP_PORT = 5081
TCP_PORT = 5082

def servidor_udp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"Servidor UDP rodando na porta {UDP_PORT}")
    while True:
        data, addr = sock.recvfrom(102400)
        data = data.decode('utf-8')
        print(f"Recebido do cliente: {data}")
        data = data.upper()
        sock.sendto(data.encode("utf-8"), addr)
        print(f"Enviado de volta: {data}")

def servidor_tcp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((UDP_IP, TCP_PORT))
    sock.listen(1)
    print(f"Servidor TCP rodando na porta {TCP_PORT}")
    while True:
        conn, addr = sock.accept()
        try:
            while True:
                data = conn.recv(102400)
                if not data: break
                data = data.decode('utf-8')
                print(f"Recebido do cliente: {data}")
                data = data.upper()
                conn.send(data.encode("utf-8"))
                print(f"Enviado de volta: {data}")
        finally:
            conn.close()

t1 = threading.Thread(target=servidor_udp)
t2 = threading.Thread(target=servidor_tcp)
t1.start()
t2.start()