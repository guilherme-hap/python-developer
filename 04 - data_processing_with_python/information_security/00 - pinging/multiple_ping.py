"""
    Programa que faz a verificação de resposta de múltiplos pings para hosts específicos na rede
    lendo um arquivo com os hosts de destino. Foram usadas as bibliotecas 'os' para funções de
    sistema e 'time' para funções de temporização.
"""
import os
import time

with open('hosts.txt', encoding='UTF-8') as file:
    dump = file.read()
    dump = dump.splitlines()

    print(dump)

    for ip in dump:
        print(f"Verifying IP {ip}")
        print("-" * 60)
        os.system(f'ping -n 2 {ip}')
        print("-" * 60)
        time.sleep(5)
