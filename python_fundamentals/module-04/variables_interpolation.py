name = "Guilherme"
age = 28
job = "Programmer"
language = "Python"
balance = 45.435

data = {
    "name": "Guilherme",
    "age": 28
}

print("Name: %s Age: %d" % (name, age))

print("Name: {} Age: {}".format(name, age))

print("Name: {1} Age: {0}".format(age, name))
print("Name: {1} Age: {0} Name: {1} {1}".format(age, name))

print("Name: {name} Age: {age}".format(name=name, age=age))
print("Name: {nome} Age: {idade} {nome} {nome} {idade}".format(idade=age, nome=name))
print("Name: {name} Age: {age}".format(**data))

print(f"Name: {name} Age: {age}")
print(f"Name: {name} Age: {age} Balance: {balance:.2f}")
print(f"Name: {name} Age: {age} Balance: {balance:10.1f}")