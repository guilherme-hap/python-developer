set_a = {1, 2, 3}
set_b = {4, 1, 2, 5, 6, 3}

result = set_a.issubset(set_b)  # True
print(result)

result = set_b.issubset(set_a)  # False
print(result)