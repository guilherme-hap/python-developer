contacts = {
    "guilherme@gmail.com": {"name": "Guilherme", "phone_number": "3333-2221"},
    "giovanna@gmail.com": {"name": "Giovanna", "phone_number": "3443-2121"},
    "chappie@gmail.com": {"name": "Chappie", "phone_number": "3344-9871"},
    "melaine@gmail.com": {"name": "Melaine", "phone_number": "3333-7766"},
}

del contacts["guilherme@gmail.com"]["phone_number"]
del contacts["chappie@gmail.com"]

# {'guilherme@gmail.com': {'name': 'Guilherme', 'phone_number': '3333-2221'}, {'name': 'Giovanna', 'phone_number': '3443-2121'}, {'name': 'Melaine', 'phone_number': '3333-7766'}}  # noqa
print(contacts)