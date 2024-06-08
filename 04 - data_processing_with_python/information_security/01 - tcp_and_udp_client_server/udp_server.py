"""
    Programa para criação de um servidor UDP local, conexão e transmissão de dados
    com um cliente UDP usando a biblioteca 'socket' para conexão e encerramento.
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket client created successfully")

host = 'localhost'
port = 5432

s.bind((host, port))
message = "\nServer: Hello client"

while 1:
    data, address = s.recvfrom(4096)

    if data:
        print("Server sending message...")
        s.sendto(data + (message.encode()), address)
