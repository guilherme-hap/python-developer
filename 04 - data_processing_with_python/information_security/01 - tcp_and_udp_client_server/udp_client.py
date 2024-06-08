"""
    Programa para criação de um cliente UDP e conexão com um servidor UDP local
    para transmissão de dados usando a biblioteca 'socket' para conexão e encerramento.
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket client created successfully")

host = 'localhost'
port = 5433
message = "Hello server"

try:
    print(f"Client: {message}")
    s.sendto(message.encode(), (host, 5432))

    data, server = s.recvfrom(4096)
    data = data.decode()

    print(f"Client: {data}")
finally:
    print("Client: Closing connection")
    s.close()
