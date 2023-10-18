list = [1, "Python", [40, 30, 20]]

new_list = list.copy()

print(list)  # [1, "Python", [40, 30, 20]]

new_list.append("New")

print(new_list) # [1, 'Python', [40, 30, 20], 'New']

print(list) # [1, "Python", [40, 30, 20]]