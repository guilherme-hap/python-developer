contacts = {
    "guilherme@gmail.com": {"name": "Guilherme", "phone_number": "3333-2221"},
    "giovanna@gmail.com": {"name": "Giovanna", "phone_number": "3443-2121"},
    "chappie@gmail.com": {"name": "Chappie", "phone_number": "3344-9871"},
    "melaine@gmail.com": {"name": "Melaine", "phone_number": "3333-7766"},
}

for key in contacts:
    print(key, contacts[key])

print("=" * 100)

for key, value in contacts.items():
    print(key, value)