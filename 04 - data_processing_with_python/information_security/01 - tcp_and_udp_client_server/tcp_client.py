"""
    Programa para criação de um cliente TCP e conexão com tratamento de erros
    usando as bibliotecas 'socket' e 'sys' para conexão e encerramento.
"""
import socket
import sys


def main():
    """
        Função para criação e conexão de um cliente TCP.
        :return: None
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Connection failed")
        print(f"Error {e}")
        sys.exit()

    print("Socket created successfully")

    target_host = input("Enter the IP or host to connect: ")
    target_port = input("Enter the port to connect: ")

    try:
        s.connect((target_host, int(target_port)))
        print(f"TCP client connected successfully to host {target_host } on port {target_port}")
        s.shutdown(2)
    except socket.error as e:
        print(f"Not possible to connect to host {target_host} on port {target_port}")
        print(f"Error {e}")
        sys.exit()


if __name__ == "__main__":
    main()
