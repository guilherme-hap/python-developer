texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # Adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5): # A função range funciona com até 3 argumentos: start, stop, step. Eles informar as condições de início, parada e incremento.
    print(numero, end=" ")