set_a = {1, 2, 3}
set_b = {4, 1, 2, 5, 6, 3}

result = set_a.issuperset(set_b)  # False
print(result)

result = set_b.issuperset(set_a)  # True
print(result)