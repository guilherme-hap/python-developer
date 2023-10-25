class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_birth_date(cls, year, month, day, name):
        age = 2022 - year
        return cls(name, age) # Usar o cls para criar um método "de fábrica" evita instanciar duas vezes o mesmo objeto.

    @staticmethod
    def is_adult(age):
        return age >= 18


p = Person.create_birth_date(1994, 3, 21, "Guilherme")
print(p.name, p.age)

print(Person.is_adult(18))
print(Person.is_adult(8))