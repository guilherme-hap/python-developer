contact = {"name": "Guilherme", "phone_number": "3333-2221"}

contact.setdefault("name", "Giovanna")  # "Guilherme"
print(contact)  # {'name': 'Guilherme', 'phone_number': '3333-2221'}

contact.setdefault("age", 28)  # 28
print(contact)  # {'name': 'Guilherme', 'phone_number': '3333-2221', 'age': 28}