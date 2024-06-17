"""
    Programa utilitário que implementa funções de inserção, atualização,
    consulta e deleção para a tabela 'Person'
"""
from models import Person


# Insere pessoas na tabela pessoa
def insert_person():
    person = Person(name="Guilherme", age="19")
    print(person)
    person.save()


# Consulta pessoas na tabela pessoa
def query_person():
    person = Person.query.all()
    print(person)


# Atualiza pessoas na tabela pessoa
def update_person():
    person = Person.query.filter_by(name="Guilherme").first()
    person.age = 22
    person.save()


# Deleta pessoas na tabela pessoa
def delete_person():
    person = Person.query.filter_by(name="Guilherme").first()
    person.delete()


if __name__ == '__main__':
    insert_person()
    update_person()
    query_person()
    delete_person()
    query_person()
