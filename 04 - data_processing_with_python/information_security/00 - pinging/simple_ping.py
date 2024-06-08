"""
    Programa que faz a verificação de resposta de um ping para um host específico na rede
    através da biblioteca os.
"""
import os

print("#" * 60)

ip_or_host = input("Enter the IP or host to verify: ")

print("-" * 60)

os.system(f'ping -n 6 {ip_or_host}')

print("-" * 60)
