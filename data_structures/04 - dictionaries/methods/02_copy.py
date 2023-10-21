contacts = {"guilherme@gmail.com": {"name": "Guilherme", "phone_number": "3333-2221"}}

copy = contacts.copy()
copy["guilherme@gmail.com"] = {"name": "Gui"}

print(contacts["guilherme@gmail.com"])  # {"name": "Guilherme", "phone_number": "3333-2221"}

print(copy["guilherme@gmail.com"])  # {"name": "Gui"}