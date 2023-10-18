set_a = {1, 2, 3, 4, 5}
set_b = {6, 7, 8, 9}
set_c = {1, 0}

result = set_a.isdisjoint(set_b)  # True
print(result)

result = set_a.isdisjoint(set_c)  # False
print(result)