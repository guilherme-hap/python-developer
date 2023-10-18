# Filter list
numbers = [1, 30, 21, 2, 9, 65, 34]
# Primeiro parâmetro é o retorno, depois vem a expressão de iteração e, opcionalmente, podem ser adicionados mais elementos
pairs = [number for number in numbers if number % 2 == 0]
print(pairs)

# Modify values
numbers = [1, 30, 21, 2, 9, 65, 34]
square = [number ** 2 for number in numbers]
print(square)