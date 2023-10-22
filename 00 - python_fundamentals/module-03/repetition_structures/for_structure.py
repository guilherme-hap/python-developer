text = input("Enter a text: ")
VOWELS = "AEIOU"


# Exemplo utilizando um iterável
for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end="")
else:
    print()  # Adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for number in range(0, 51, 5): # A função range funciona com até 3 argumentos: start, stop, step. Eles informar as condições de início, parada e incremento.
    print(number, end=" ")