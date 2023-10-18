numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numbers)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numbers.discard(1)
numbers.discard(45)

print(numbers)  # {0, 2, 3, 4, 5, 6, 7, 8, 9}