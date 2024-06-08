"""
    Programa para treinar os conceitos de endereçamento IP em diversas classes
    utilizando a biblioteca 'ipaddress'.
"""
import ipaddress

IP = '192.168.0.100/26'

network = ipaddress.ip_network(IP, strict=False)

for ip in network:
    print(ip)

print(network)
