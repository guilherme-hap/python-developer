"""

"""
from models import Person


def insert_person():
    person = Person(name="Guilherme", age="19")
    print(person)
    person.save()


def query_person():
    person = Person.query.all()
    print(person)


def update_person():
    person = Person.query.filter_by(name="Guilherme").first()
    person.age = 22
    person.save()


def delete_person():
    person = Person.query.filter_by(name="Guilherme").first()
    person.delete()


if __name__ == '__main__':
    insert_person()
    update_person()
    query_person()
    delete_person()
    query_person()
