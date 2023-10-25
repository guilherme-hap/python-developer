class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self._birth_year = birth_year

    @property
    def age(self):
        _current_year = 2022
        return _current_year - self._birth_year


person = Person("Guilherme", 1994)
print(f"Name: {person.name} \tAge: {person.age}")