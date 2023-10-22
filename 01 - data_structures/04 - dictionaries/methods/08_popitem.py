contacts = {"guilherme@gmail.com": {"name": "Guilherme", "phone_number": "3333-2221"}}

result = contacts.popitem()  # ('guilherme@gmail.com', {'name': 'Guilherme', 'phone_number': '3333-2221'})
print(result)

# contatos.popitem()  # KeyError