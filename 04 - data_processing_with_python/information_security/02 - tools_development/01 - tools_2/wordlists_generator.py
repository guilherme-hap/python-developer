"""
    Programa que utiliza a biblioteca 'itertools' para gerar uma lista com
    vários caracteres diferentes e sem repetição de palavras, muito
    utilizado em ataques de força bruta.
"""
import itertools

string = input("String to permute: ")

result = itertools.permutations(string, len(string))

for i in result:
    print(''.join(i))
