contacts = {"guilherme@gmail.com": {"name": "Guilherme", "phone_number": "3333-2221"}}

# contatos["chave"]  # KeyError

result = contacts.get("key")  # None
print(result)

result = contacts.get("key", {})  # {}
print(result)

result = contacts.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"name": "Guilherme", "phone_number": "3333-2221"}
print(result)