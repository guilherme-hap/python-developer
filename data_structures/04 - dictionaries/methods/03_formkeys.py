results = dict.fromkeys(["name", "phone_number"])  # {"name": None, "phone_number": None}
print(results)

results = dict.fromkeys(["name", "phone_number"], "empty")  # {"name": "empty", "phone_number": "empty"}
print(results)