contacts = {
    "guilherme@gmail.com": {"name": "Guilherme", "phone_number": "3333-2221"},
    "giovanna@gmail.com": {"name": "Giovanna", "phone_number": "3443-2121"},
    "chappie@gmail.com": {"name": "Chappie", "phone_number": "3344-9871"},
    "melaine@gmail.com": {"name": "Melaine", "phone_number": "3333-7766"},
}

result = "guilherme@gmail.com" in contacts  # True
print(result)

result = "megui@gmail.com" in contacts  # False
print(result)

result = "age" in contacts["guilherme@gmail.com"]  # False
print(result)

result = "phone_number" in contacts["giovanna@gmail.com"]  # True
print(result)