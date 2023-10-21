contacts = {"guilherme@gmail.com": {"name": "Guilherme", "phone_number": "3333-2221"}}

contacts.update({"guilherme@gmail.com": {"name": "Gui"}})
print(contacts)  # {'guilherme@gmail.com': {'name': 'Gui'}}

contacts.update({"giovanna@gmail.com": {"name": "Giovanna", "phone_number": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'name': 'Giovanna', 'phone_number': '3322-8181'}}
print(contacts)