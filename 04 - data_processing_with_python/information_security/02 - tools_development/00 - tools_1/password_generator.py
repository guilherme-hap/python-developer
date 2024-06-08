"""
    Programa para gerar senhas com um tamanho específico utilizando as bibliotecas
    'random' e 'string' para geração randômica.
"""
import random as rd
import string

LENGTH = 16
CHARS = string.ascii_letters + string.digits + '!@#$%¨&*()-=+_.;/?><:'

random = rd.SystemRandom()

print(''.join(random.choice(CHARS) for i in range(LENGTH)))
